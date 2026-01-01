/**
 * Configuration for the Simulated Annealing algorithm.
 *
 * The algorithm uses a multi-phase approach:
 * - Phase 1: Eliminate hard constraint violations
 * - Phase 1.5: Intensification (optional) - Aggressively target remaining hard violations
 * - Phase 2: Optimize soft constraints
 *
 * Advanced features:
 * - Tabu Search: Prevents cycling by tracking visited states
 * - Reheating: Escapes local minima by temporarily increasing temperature
 * - Intensification: Focused optimization for stubborn violations
 * - Adaptive operator selection: Learns effective operators
 *
 * @template TState - The state type for your problem domain
 */
export interface SAConfig<TState> {
  /**
   * Initial temperature for the annealing process.
   *
   * Higher values allow more exploration of the solution space at the start.
   * Typical values: 100 to 10000
   *
   * @default 1000
   *
   * @remarks
   * - Too high: Wastes iterations on random exploration
   * - Too low: Gets stuck in local minima quickly
   */
  initialTemperature: number;

  /**
   * Minimum temperature (stopping criterion).
   *
   * The algorithm stops when temperature drops below this value.
   * Typical values: 0.001 to 1
   *
   * @default 0.01
   */
  minTemperature: number;

  /**
   * Cooling rate (temperature decay factor).
   *
   * Temperature is multiplied by this value each iteration: `T = T * coolingRate`
   * Must be between 0 and 1 (exclusive).
   * Typical values: 0.95 to 0.999
   *
   * @default 0.995
   *
   * @remarks
   * - Higher (closer to 1): Slower cooling, more iterations, better results
   * - Lower (closer to 0): Faster cooling, fewer iterations, may miss optimal solution
   */
  coolingRate: number;

  /**
   * Maximum number of iterations (stopping criterion).
   *
   * The algorithm stops after this many iterations, even if temperature hasn't reached `minTemperature`.
   * Typical values: 10000 to 100000
   *
   * @default 50000
   */
  maxIterations: number;

  /**
   * Penalty weight for hard constraint violations.
   *
   * Hard constraints are penalized with: `hardViolations * hardConstraintWeight`
   * Should be much larger than soft constraint weights to prioritize hard constraints.
   * Typical values: 1000 to 100000
   *
   * @default 10000
   *
   * @remarks
   * This ensures hard constraints are satisfied before optimizing soft constraints.
   */
  hardConstraintWeight: number;

  /**
   * State cloning function.
   *
   * Provides a deep copy of the state to avoid mutating the current solution.
   *
   * @param state - State to clone
   * @returns Deep copy of the state
   *
   * @example
   * ```typescript
   * // Simple JSON-based cloning
   * cloneState: (state) => JSON.parse(JSON.stringify(state))
   *
   * // Custom cloning for better performance
   * cloneState: (state) => ({
   *   ...state,
   *   schedule: state.schedule.map(entry => ({ ...entry }))
   * })
   * ```
   */
  cloneState: (state: TState) => TState;

  /**
   * Number of iterations without improvement before triggering reheating.
   *
   * If set, the algorithm will "reheat" (increase temperature) when stuck in a local minimum.
   *
   * @default undefined (no reheating)
   *
   * @remarks
   * Reheating helps escape local minima by temporarily increasing exploration.
   * Typical values: 1000 to 5000
   */
  reheatingThreshold?: number;

  /**
   * Factor to multiply temperature by when reheating.
   *
   * Temperature increases by: `T = T * reheatingFactor`
   *
   * @default 2.0
   *
   * @remarks
   * Typical values: 1.5 to 3.0
   */
  reheatingFactor?: number;

  /**
   * Maximum number of reheating events allowed.
   *
   * Prevents infinite reheating loops.
   *
   * @default 3
   */
  maxReheats?: number;

  // ============================================
  // TABU SEARCH CONFIGURATION
  // ============================================
  //
  // Tabu Search prevents the algorithm from revisiting recently explored states,
  // which helps avoid cycling and escape local minima more effectively.
  //
  // How it works:
  // 1. Each state is assigned a lightweight signature (hash)
  // 2. Signatures are stored in a tabu list with the iteration they were added
  // 3. Before accepting a move, check if the new state is in the tabu list
  // 4. States remain tabu for 'tabuTenure' iterations, then are removed
  // 5. List is automatically trimmed if it exceeds 'maxTabuListSize'
  //
  // When to use:
  // - Problems with many local minima
  // - Search gets stuck oscillating between similar solutions
  // - Complex constraint landscapes
  //
  // When to skip:
  // - Simple, convex problems
  // - Quick testing/prototyping
  // - Problems with extremely large state spaces

  /**
   * Enable Tabu Search to prevent cycling back to recently visited states.
   *
   * When enabled, the algorithm tracks recent states using lightweight signatures
   * and prevents revisiting the same solutions, which helps escape local minima.
   *
   * This is particularly useful when you observe:
   * - Fitness oscillating between a few values
   * - Same violations recurring
   * - Getting stuck despite having good move operators
   *
   * @default false
   */
  tabuSearchEnabled?: boolean;

  /**
   * Number of iterations a state stays in the tabu list (tabu tenure).
   *
   * Higher values:
   * - More diverse search
   * - Less cycling
   * - May miss good solutions near tabu states
   *
   * Lower values:
   * - Less diverse search
   * - Faster convergence
   * - May still cycle occasionally
   *
   * Recommended: 50 for most problems, 100-150 for very complex problems
   *
   * @default 50
   */
  tabuTenure?: number;

  /**
   * Maximum size of the tabu list for memory management.
   *
   * When the list exceeds this size, oldest entries are removed automatically.
   * This prevents unbounded memory usage during long optimization runs.
   *
   * Larger values allow:
   * - Better cycling prevention
   * - More memory usage (~100 bytes per entry)
   *
   * Smaller values use less memory but may allow cycling.
   *
   * Memory calculation: maxTabuListSize * 100 bytes
   * - 1000 entries ≈ 100 KB
   * - 5000 entries ≈ 500 KB
   *
   * @default 1000
   */
  maxTabuListSize?: number;

  // ============================================
  // INTENSIFICATION CONFIGURATION
  // ============================================
  //
  // Intensification is an aggressive Phase 1.5 that targets remaining hard violations
  // when Phase 1 doesn't achieve zero violations. It uses focused operator selection
  // and multiple restart attempts to eliminate stubborn violations.
  //
  // How it works:
  // 1. Triggered when Phase 1 ends with hardViolations > 0
  // 2. Each attempt runs for intensificationIterations with focused operator selection
  // 3. Uses targeted operators (fix/swap/change) 70% of time, all operators 30%
  // 4. Aggressively accepts moves that reduce hard violations
  // 5. Reheats if stagnation detected (300 iterations without improvement)
  // 6. Stops early when all hard violations eliminated
  // 7. Up to maxIntensificationAttempts restart attempts
  //
  // When to use (enabled by default):
  // - Problems with complex, conflicting constraints
  // - Hard constraints are difficult to satisfy
  // - Phase 1 frequently ends with remaining violations
  //
  // When to disable:
  // - Simple problems where Phase 1 consistently reaches zero violations
  // - Quick approximate solutions are acceptable
  // - Soft constraints are more important than hard constraint feasibility

  /**
   * Enable Phase 1.5 Intensification mode.
   *
   * When Phase 1 ends with remaining hard violations, this mode
   * aggressively targets those violations with dedicated iterations and
   * focused operator selection.
   *
   * Intensification features:
   * - Uses targeted operators (fix/swap/change) 70% of time
   * - Aggressive acceptance for reducing hard violations
   * - Multiple restart attempts with temperature reset
   * - Reheating when stagnation detected
   * - Early exit when all violations eliminated
   *
   * This is particularly helpful for problems with many conflicting constraints
   * or where reaching feasibility is the main challenge.
   *
   * @default true
   */
  enableIntensification?: boolean;

  /**
   * Maximum iterations for each intensification attempt.
   *
   * Each intensification attempt runs this many iterations focusing
   * on eliminating remaining hard violations. If all violations are
   * eliminated before reaching this limit, the attempt stops early.
   *
   * Higher values:
   * - More thorough search for feasibility
   * - Slower single attempts
   *
   * Lower values:
   * - Faster attempts
   * - May miss solutions that require more iterations
   *
   * Recommended: 2000 for most problems, 5000+ for very complex problems
   *
   * @default 2000
   */
  intensificationIterations?: number;

  /**
   * Maximum number of intensification restart attempts.
   *
   * Each attempt resets the temperature and focuses on remaining hard violations.
   * The process stops when either:
   * - All hard violations are eliminated (success)
   * - Maximum attempts reached (may have remaining violations)
   *
   * Multiple attempts help because each restart can explore different regions
   * of the solution space due to the temperature reset.
   *
   * Recommended:
   * - 2-3 attempts for most problems
   * - 4-5 attempts for very difficult problems
   *
   * @default 3
   */
  maxIntensificationAttempts?: number;

  /**
   * Logging configuration
   */
  logging?: LoggingConfig;
}

/**
 * Logging configuration for the optimization process
 */
export interface LoggingConfig {
  /**
   * Enable or disable logging
   *
   * @default true
   */
  enabled?: boolean;

  /**
   * Logging level
   *
   * - `'debug'`: Detailed information for debugging
   * - `'info'`: General information about optimization progress
   * - `'warn'`: Warnings (e.g., no improvement for many iterations)
   * - `'error'`: Errors only
   * - `'none'`: No logging
   *
   * @default 'info'
   */
  level?: 'debug' | 'info' | 'warn' | 'error' | 'none';

  /**
   * Log progress every N iterations
   *
   * @default 1000
   */
  logInterval?: number;

  /**
   * Output destination
   *
   * - `'console'`: Log to console only
   * - `'file'`: Log to file only
   * - `'both'`: Log to both console and file
   *
   * @default 'console'
   */
  output?: 'console' | 'file' | 'both';

  /**
   * File path for file-based logging
   *
   * Only used if `output` is `'file'` or `'both'`
   *
   * @default './sa-optimization.log'
   */
  filePath?: string;
}
