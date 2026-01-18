/**
 * Generic Simulated Annealing optimizer for constraint satisfaction problems.
 *
 * This class implements a multi-phase simulated annealing algorithm:
 * - Phase 1: Eliminate hard constraint violations (60% of maxIterations)
 * - Phase 1.5: Intensification - Aggressively target remaining hard violations (optional)
 * - Phase 2: Optimize soft constraints while maintaining hard constraint satisfaction
 *
 * Features:
 * - Tabu Search: Prevents cycling by tracking recently visited states
 * - Adaptive Operator Selection: Learns which operators work best
 * - Reheating: Escapes local minima by temporarily increasing temperature
 * - Intensification: Focused optimization to eliminate stubborn hard violations
 *
 * @template TState - The state type for your problem domain
 */

import type { Constraint } from './interfaces/Constraint.js';
import type { MoveGenerator } from './interfaces/MoveGenerator.js';
import type { SAConfig } from './interfaces/SAConfig.js';
import type { Solution, OperatorStats } from './types/Solution.js';
import type { Violation } from './types/Violation.js';

export class SimulatedAnnealing<TState> {
  private initialState: TState;
  private constraints: Constraint<TState>[];
  private hardConstraints: Constraint<TState>[];
  private softConstraints: Constraint<TState>[];
  private moveGenerators: MoveGenerator<TState>[];
  private config: SAConfig<TState> & {
    reheatingFactor: number;
    maxReheats: number;
    tabuSearchEnabled: boolean;
    tabuTenure: number;
    maxTabuListSize: number;
    enableIntensification: boolean;
    intensificationIterations: number;
    maxIntensificationAttempts: number;
    logging: Required<NonNullable<SAConfig<TState>['logging']>>;
  };
  // Operator statistics
  private operatorStats: OperatorStats = {};

  // Tabu list: stores move signatures with the iteration they were added
  private tabuList: Map<string, number> = new Map();

  constructor(
    initialState: TState,
    constraints: Constraint<TState>[],
    moveGenerators: MoveGenerator<TState>[],
    config: SAConfig<TState>
  ) {
    this.initialState = initialState;
    this.constraints = constraints;
    this.moveGenerators = moveGenerators;

    // Separate hard and soft constraints
    this.hardConstraints = constraints.filter((c) => c.type === 'hard');
    this.softConstraints = constraints.filter((c) => c.type === 'soft');

    // Merge config with defaults
    this.config = this.mergeWithDefaults(config);

    // Initialize operator stats
    for (const generator of moveGenerators) {
      this.operatorStats[generator.name] = {
        attempts: 0,
        improvements: 0,
        accepted: 0,
        successRate: 0,
      };
    }

    this.log('info', 'Simulated Annealing initialized', {
      hardConstraints: this.hardConstraints.length,
      softConstraints: this.softConstraints.length,
      moveGenerators: this.moveGenerators.length,
      config: {
        initialTemperature: this.config.initialTemperature,
        minTemperature: this.config.minTemperature,
        coolingRate: this.config.coolingRate,
        maxIterations: this.config.maxIterations,
      },
    });
  }

  /**
   * Run the optimization algorithm
   *
   * Algorithm Phases:
   * 1. Phase 1: Eliminate hard constraint violations (60% of maxIterations)
   *    - Focuses on reducing hard violations
   *    - Uses tabu search if enabled to prevent cycling
   *    - Reheats if stuck in local minima
   *
   * 2. Phase 1.5: Intensification (if enableIntensification = true and hardViolations > 0)
   *    - Aggressively targets remaining hard violations
   *    - Uses focused operator selection (70% targeted, 30% random)
   *    - Multiple restart attempts (maxIntensificationAttempts)
   *    - Stops early when all hard violations eliminated
   *
   * 3. Phase 2: Optimize soft constraints
   *    - Maintains hard constraint satisfaction (strict enforcement)
   *    - Optimizes soft constraint satisfaction
   *    - Uses tabu search if enabled
   *
   * @returns Best solution found with detailed statistics
   */
  solve(): Solution<TState> {
    this.log('info', 'Starting optimization...');
    this.log('info', 'Phase 1: Eliminating hard constraint violations');

    let currentState = this.config.cloneState(this.initialState);
    let bestState = this.config.cloneState(currentState);

    const initialResult = this.calculateFitnessAndViolations(currentState);
    let currentFitness = initialResult.fitness;
    let bestFitness = currentFitness;

    let currentHardViolations = initialResult.hardViolations;
    let bestHardViolations = currentHardViolations;

    let temperature = this.config.initialTemperature;
    let iteration = 0;
    let iterationsWithoutImprovement = 0;
    let reheats = 0;

    this.log('info', 'Initial state', {
      fitness: currentFitness.toFixed(2),
      hardViolations: currentHardViolations,
    });

    // Phase 1: Eliminate hard constraints
    const phase1MaxIterations = Math.floor(this.config.maxIterations * 0.6);
    let phase1Iteration = 0;

    while (
      temperature > this.config.initialTemperature / 10 &&
      phase1Iteration < phase1MaxIterations &&
      bestHardViolations > 0
    ) {
      const { newState, operatorName } = this.generateNeighbor(currentState, temperature);

      if (!newState) {
        // No applicable move generators
        break;
      }

      // Tabu Search: Check if this state was recently visited
      if (this.config.tabuSearchEnabled) {
        const newSignature = this.getStateSignature(newState);
        if (this.isTabu(newSignature, iteration)) {
          // Skip tabu states
          phase1Iteration++;
          iteration++;
          continue;
        }
      }

      this.operatorStats[operatorName]!.attempts++;

      const { fitness: newFitness, hardViolations: newHardViolations } = this.calculateFitnessAndViolations(newState);

      // Phase 1 acceptance: prioritize reducing hard violations
      const acceptProb = this.acceptanceProbabilityPhase1(
        currentHardViolations,
        newHardViolations,
        currentFitness,
        newFitness,
        temperature
      );

      if (Math.random() < acceptProb) {
        this.operatorStats[operatorName]!.accepted++;

        if (newFitness < currentFitness) {
          this.operatorStats[operatorName]!.improvements++;
        }

        // Add current state to tabu list (prevent cycling back)
        if (this.config.tabuSearchEnabled) {
          const currentSignature = this.getStateSignature(currentState);
          this.addToTabuList(currentSignature, iteration);
        }

        currentState = newState;
        currentFitness = newFitness;
        currentHardViolations = newHardViolations;

        // Update best solution
        if (
          newHardViolations < bestHardViolations ||
          (newHardViolations === bestHardViolations && newFitness < bestFitness)
        ) {
          bestState = this.config.cloneState(currentState);
          bestFitness = newFitness;
          bestHardViolations = newHardViolations;
          iterationsWithoutImprovement = 0;

          this.log('debug', `[Phase 1] New best: Hard violations = ${bestHardViolations}, Fitness = ${bestFitness.toFixed(2)}, Operator = ${operatorName}`);
        } else {
          iterationsWithoutImprovement++;
        }
      } else {
        iterationsWithoutImprovement++;
      }

      // Reheating
      if (
        this.config.reheatingThreshold !== undefined &&
        iterationsWithoutImprovement >= this.config.reheatingThreshold &&
        this.config.maxReheats !== undefined &&
        reheats < this.config.maxReheats &&
        temperature < this.config.initialTemperature / 100
      ) {
        const reheatingFactor = this.config.reheatingFactor ?? 2.0;
        temperature *= reheatingFactor;
        reheats++;
        iterationsWithoutImprovement = 0;

        this.log('info', `[Phase 1] Reheating #${reheats}: Temperature = ${temperature.toFixed(2)}, Hard violations = ${bestHardViolations}`);
      }

      temperature *= this.config.coolingRate;
      phase1Iteration++;
      iteration++;

      const logInterval = this.config.logging.logInterval ?? 1000;
      if (phase1Iteration % logInterval === 0) {
        this.log('info', `[Phase 1] Iteration ${phase1Iteration}: Temp = ${temperature.toFixed(2)}, Hard violations = ${currentHardViolations}, Best = ${bestHardViolations}`);
      }
    }

    this.log('info', `Phase 1 complete: Hard violations = ${bestHardViolations}`);

  // ============================================
  // PHASE 1.5: INTENSIFICATION
  // ============================================
  // If hard violations remain and intensification is enabled,
  // aggressively target remaining violations with multiple restart attempts.
  //
  // Intensification features:
  // - Focused operator selection (70% targeted: fix/swap/change, 30% random)
  // - Aggressive acceptance logic for reducing hard violations
  // - Multiple restart attempts with temperature reset
  // - Reheating when stagnation detected (300 iterations without improvement)
  // - Early exit when all hard violations eliminated
    
    if (bestHardViolations > 0 && this.config.enableIntensification) {
      this.log('info', 'Phase 1.5: Intensification - targeting remaining hard violations');
      
      let intensificationAttempt = 0;
      
      while (bestHardViolations > 0 && intensificationAttempt < this.config.maxIntensificationAttempts) {
        intensificationAttempt++;
        this.log('info', `[Intensification] Attempt ${intensificationAttempt}/${this.config.maxIntensificationAttempts}`);
        
        // Reset temperature for fresh exploration
        let intensificationTemp = this.config.initialTemperature;
        let intensificationIterations = 0;
        let stagnationCounter = 0;
        const stagnationLimit = 300;
        
        // Start from best known state
        currentState = this.config.cloneState(bestState);
        currentFitness = bestFitness;
        currentHardViolations = bestHardViolations;
        
        while (intensificationIterations < this.config.intensificationIterations && bestHardViolations > 0) {
          // Include ALL operators during intensification, but weight targeted ones higher
          // This fixes the bug where ChangeTimeSlotAndRoom (12.8% success rate) was excluded
          const allGenerators = this.moveGenerators.filter((gen) => gen.canApply(currentState));
          const targetedGenerators = allGenerators.filter((gen) => {
            const name = gen.name.toLowerCase();
            // Include 'change' to capture ChangeTimeSlotAndRoom which is highly effective
            return name.includes('fix') || name.includes('swap') || name.includes('change');
          });
          
          // Use targeted operators 70% of time, all operators 30% (more exploration)
          const generators = targetedGenerators.length > 0 && Math.random() < 0.7
            ? targetedGenerators
            : allGenerators;
          
          if (generators.length === 0) {
            break;
          }
          
          // Random selection during intensification (more exploration)
          const selectedGenerator = generators[Math.floor(Math.random() * generators.length)]!;
          const clonedState = this.config.cloneState(currentState);
          const newState = selectedGenerator.generate(clonedState, intensificationTemp);
          
          if (!newState) {
            intensificationIterations++;
            continue;
          }
          
          this.operatorStats[selectedGenerator.name]!.attempts++;
          
          const { fitness: newFitness, hardViolations: newHardViolations } = this.calculateFitnessAndViolations(newState);
          
          // Intensification acceptance: heavily favor reducing hard violations
          let accept = false;
          
          if (newHardViolations < currentHardViolations) {
            // Always accept if hard violations decrease
            accept = true;
            this.operatorStats[selectedGenerator.name]!.improvements++;
            stagnationCounter = 0;
          } else if (newHardViolations === currentHardViolations) {
            // Accept with moderate probability if hard violations same
            if (newFitness < currentFitness) {
              accept = true;
              this.operatorStats[selectedGenerator.name]!.improvements++;
              stagnationCounter = 0;
            } else {
              // Accept worse with probability based on temperature
              const acceptProb = Math.exp((currentFitness - newFitness) / intensificationTemp);
              accept = Math.random() < acceptProb;
              stagnationCounter++;
            }
          } else {
            // Occasionally accept worse moves to escape local minima (simulated annealing style)
            // This helps break out of deadlock situations
            // Reduced from 5% to 2% to prevent destabilization (saw 1→20 violations in trials)
            const worsenProb = Math.exp(-1 / (intensificationTemp / 10000));
            if (Math.random() < worsenProb * 0.02) {
              accept = true;
              this.log('debug', '[Intensification] Accepting worsening move to escape local minimum');
            }
            stagnationCounter++;
          }
          
          if (accept) {
            this.operatorStats[selectedGenerator.name]!.accepted++;
            currentState = newState;
            currentFitness = newFitness;
            currentHardViolations = newHardViolations;
            
            // Update best if improved
            if (newHardViolations < bestHardViolations || 
                (newHardViolations === bestHardViolations && newFitness < bestFitness)) {
              bestState = this.config.cloneState(currentState);
              bestFitness = newFitness;
              bestHardViolations = newHardViolations;
              
              this.log('debug', `[Intensification] New best: Hard violations = ${bestHardViolations}, Fitness = ${bestFitness.toFixed(2)}`);
            }
          }
          
          // Reheat if stagnating
          if (stagnationCounter >= stagnationLimit) {
            intensificationTemp = this.config.initialTemperature * 0.5;
            stagnationCounter = 0;
            this.log('debug', '[Intensification] Stagnation detected, reheating');
          }
          
          // Cool down (slower than normal)
          intensificationTemp *= 0.999;
          intensificationIterations++;
          iteration++;
          
          // Log progress
          if (intensificationIterations % 500 === 0) {
            this.log('info', `[Intensification] Iter ${intensificationIterations}: Hard violations = ${currentHardViolations}, Best = ${bestHardViolations}`);
          }
        }
        
        // If this attempt succeeded, break early
        if (bestHardViolations === 0) {
          this.log('info', `[Intensification] SUCCESS! All hard violations eliminated in attempt ${intensificationAttempt}`);
          break;
        }
      }
      
      if (bestHardViolations > 0) {
        this.log('warn', `[Intensification] Could not eliminate all hard violations. Remaining: ${bestHardViolations}`);
      }
    }

    // Phase 2: Optimize soft constraints
    this.log('info', 'Phase 2: Optimizing soft constraints');

    currentState = this.config.cloneState(bestState);
    currentFitness = bestFitness;
    iterationsWithoutImprovement = 0;

    while (temperature > this.config.minTemperature && iteration < this.config.maxIterations) {
      const { newState, operatorName } = this.generateNeighbor(currentState, temperature);

      if (!newState) {
        break;
      }

      // Tabu Search: Check if this state was recently visited
      if (this.config.tabuSearchEnabled) {
        const newSignature = this.getStateSignature(newState);
        if (this.isTabu(newSignature, iteration)) {
          // Skip tabu states
          iteration++;
          continue;
        }
      }

      this.operatorStats[operatorName]!.attempts++;

      const { fitness: newFitness, hardViolations: newHardViolations } = this.calculateFitnessAndViolations(newState);

      // STRICT Phase 2: NEVER accept solutions that increase hard violations
      const acceptProb = this.acceptanceProbabilityPhase2(
        bestHardViolations,
        newHardViolations,
        currentFitness,
        newFitness,
        temperature
      );

      if (Math.random() < acceptProb) {
        this.operatorStats[operatorName]!.accepted++;

        if (newFitness < currentFitness) {
          this.operatorStats[operatorName]!.improvements++;
        }

        // Add current state to tabu list (prevent cycling back)
        if (this.config.tabuSearchEnabled) {
          const currentSignature = this.getStateSignature(currentState);
          this.addToTabuList(currentSignature, iteration);
        }

        currentState = newState;
        currentFitness = newFitness;

        // Track if this improves or maintains hard violations
        if (newHardViolations < bestHardViolations) {
          bestHardViolations = newHardViolations;
          this.log('debug', `[Phase 2] Hard violations reduced to ${bestHardViolations}`);
        }

        if (newFitness < bestFitness) {
          bestState = this.config.cloneState(currentState);
          bestFitness = newFitness;
          iterationsWithoutImprovement = 0;

          this.log('debug', `[Phase 2] New best: Fitness = ${bestFitness.toFixed(2)}, Hard violations = ${newHardViolations}, Operator = ${operatorName}`);
        } else {
          iterationsWithoutImprovement++;
        }
      } else {
        iterationsWithoutImprovement++;
      }

      // Reheating
      if (
        this.config.reheatingThreshold !== undefined &&
        iterationsWithoutImprovement >= this.config.reheatingThreshold &&
        this.config.maxReheats !== undefined &&
        reheats < this.config.maxReheats &&
        temperature < this.config.initialTemperature / 100
      ) {
        const reheatingFactor = this.config.reheatingFactor ?? 2.0;
        temperature *= reheatingFactor;
        reheats++;
        iterationsWithoutImprovement = 0;

        this.log('info', `[Phase 2] Reheating #${reheats}: Temperature = ${temperature.toFixed(2)}, Fitness = ${bestFitness.toFixed(2)}`);
      }

      temperature *= this.config.coolingRate;
      iteration++;

      const logInterval2 = this.config.logging.logInterval ?? 1000;
      if (iteration % logInterval2 === 0) {
        this.log('info', `[Phase 2] Iteration ${iteration}: Temp = ${temperature.toFixed(2)}, Current = ${currentFitness.toFixed(2)}, Best = ${bestFitness.toFixed(2)}`);
      }
    }

    // Calculate final statistics
    this.updateOperatorStats();

    const violations = this.getViolations(bestState);
    const hardViolations = violations.filter((v) => v.constraintType === 'hard').length;
    const softViolations = violations.filter((v) => v.constraintType === 'soft').length;

    this.log('info', 'Optimization complete', {
      iterations: iteration,
      reheats: reheats,
      finalTemperature: temperature.toFixed(4),
      fitness: bestFitness.toFixed(2),
      hardViolations: hardViolations,
      softViolations: softViolations,
    });

    this.logOperatorStats();

    return {
      state: bestState,
      fitness: bestFitness,
      hardViolations: hardViolations,
      softViolations: softViolations,
      iterations: iteration,
      reheats: reheats,
      finalTemperature: temperature,
      violations: violations,
      operatorStats: this.operatorStats,
    };
  }

  /**
   * Calculate fitness for a state (wrapper for backward compatibility)
   */
  private calculateFitness(state: TState): number {
    return this.calculateFitnessAndViolations(state).fitness;
  }

  /**
   * Count hard constraint violations (wrapper for backward compatibility)
   */
  private countHardViolations(state: TState): number {
    return this.calculateFitnessAndViolations(state).hardViolations;
  }

  /**
   * OPTIMIZED: Calculate both fitness AND hard violation count in a single pass
   * 
   * This eliminates the redundant constraint evaluation that was causing
   * ~28% performance overhead (hard constraints were evaluated twice per iteration).
   * 
   * @returns Object with fitness score and hard violation count
   */
  private calculateFitnessAndViolations(state: TState): { fitness: number; hardViolations: number } {
    let hardPenalty = 0;
    let softPenalty = 0;
    let hardViolationCount = 0;

    // Evaluate hard constraints ONCE - calculate both penalty and violation count
    for (const constraint of this.hardConstraints) {
      const score = constraint.evaluate(state);
      if (score < 1) {
        hardPenalty += (1 - score);

        // Count violations using getViolations() if available
        if (constraint.getViolations) {
          const violations = constraint.getViolations(state);
          hardViolationCount += violations.length;
        } else {
          // Fallback: infer count from score
          // Many constraints use: score = 1 / (1 + violationCount)
          const inferredCount = Math.round((1 / score) - 1);
          hardViolationCount += Math.max(1, inferredCount);
        }
      }
    }

    // Evaluate soft constraints
    for (const constraint of this.softConstraints) {
      const score = constraint.evaluate(state);
      const weight = constraint.weight ?? 10;
      if (score < 1) {
        softPenalty += (1 - score) * weight;
      }
    }

    const fitness = hardPenalty * this.config.hardConstraintWeight + softPenalty;

    return { fitness, hardViolations: hardViolationCount };
  }

  /**
   * Generate neighbor state using adaptive operator selection
   */
  private generateNeighbor(
    state: TState,
    temperature: number
  ): { newState: TState | null; operatorName: string } {
    // Filter applicable move generators
    const applicableGenerators = this.moveGenerators.filter((gen) => gen.canApply(state));

    if (applicableGenerators.length === 0) {
      return { newState: null, operatorName: '' };
    }

    // Adaptive selection based on success rates
    const selectedGenerator = this.selectMoveGenerator(applicableGenerators);
    const clonedState = this.config.cloneState(state); 
    const newState = selectedGenerator.generate(clonedState, temperature);

    return { newState, operatorName: selectedGenerator.name };
  }

   /**
    * Pure Roulette Wheel Selection (100% fitness-proportionate)
    *
    * Formula: P(i) = fitness(i) / Σ fitness(j)
    *
    * Reference: Muklason et al. (2024) - Tabu-Simulated Annealing Hyper-Heuristics
    *
    * @param generators - All applicable move generators
    * @returns Selected generator
    */
   private selectGeneratorRouletteWheel(generators: MoveGenerator<TState>[]): MoveGenerator<TState> {
     // Use success rate as fitness
     const fitnesses = generators.map(gen =>
       this.operatorStats[gen.name]?.successRate || 1.0 / generators.length
     );

     const totalFitness = fitnesses.reduce((sum, f) => sum + f, 0);

     if (totalFitness === 0) {
       // Uniform random if no data
       return generators[Math.floor(Math.random() * generators.length)]!;
     }

     // Pure Roulette Wheel selection
     let random = Math.random() * totalFitness;
     for (let i = 0; i < generators.length; i++) {
       random -= fitnesses[i]!;
       if (random <= 0) {
         return generators[i]!;
       }
     }

     return generators[generators.length - 1]!;
   }

   /**
    * Hybrid Selection (30% random + 70% weighted)
    *
    * Modification from Roulette Wheel to guarantee exploration
    *
    * Reference: Cowling et al. (2002) - Hyper-heuristics with diversity preservation
    *
    * @param generators - All applicable move generators
    * @returns Selected generator
    */
   private selectGeneratorHybrid(generators: MoveGenerator<TState>[]): MoveGenerator<TState> {
     // 30%: forced random (exploration)
     if (Math.random() < 0.3) {
       return generators[Math.floor(Math.random() * generators.length)]!;
     }

     // 70%: weighted based on success rates
     const weights = generators.map((gen) => {
       const stats = this.operatorStats[gen.name]!;
       return stats.successRate || 0.5; // Default to 0.5 if no data yet
     });

     const totalWeight = weights.reduce((sum, w) => sum + w, 0);

     if (totalWeight === 0) {
       return generators[Math.floor(Math.random() * generators.length)]!;
     }

     // Weighted random selection
     let random = Math.random() * totalWeight;
     for (let i = 0; i < generators.length; i++) {
       random -= weights[i]!;
       if (random <= 0) {
         return generators[i]!;
       }
     }

     return generators[generators.length - 1]!;
   }

   /**
    * Select move generator based on configured mode
    *
    * Delegates to either hybrid (default) or roulette-wheel selection.
    *
    * @param generators - All applicable move generators
    * @returns Selected generator
    */
   private selectMoveGenerator(generators: MoveGenerator<TState>[]): MoveGenerator<TState> {
     const mode = this.config.operatorSelectionMode ?? 'hybrid';

     if (mode === 'roulette-wheel') {
       return this.selectGeneratorRouletteWheel(generators);
     } else {
       return this.selectGeneratorHybrid(generators);
     }
   }

  // ============================================
  // TABU SEARCH METHODS
  // ============================================
  //
  // Tabu Search prevents the algorithm from cycling back to recently visited states.
  // This helps escape local minima by maintaining a short-term memory of the search.
  //
  // How it works:
  // 1. Each state is assigned a lightweight signature (hash)
  // 2. Signatures are stored in a tabu list with their iteration number
  // 3. Before accepting a move, check if the new state is tabu
  // 4. States remain tabu for 'tabuTenure' iterations
  // 5. Old entries are automatically removed when list exceeds 'maxTabuListSize'
  //
  // Configuration:
  // - tabuSearchEnabled: Enable/disable tabu search (default: false)
  // - tabuTenure: Number of iterations a state stays tabu (default: 50)
  // - maxTabuListSize: Maximum tabu entries stored (default: 1000)

  /**
   * Generate a lightweight signature for a state
   * Used to track visited states in the tabu list
   *
   * Note: This creates a hash based on schedule assignments, not the full state.
   * This is efficient because we only care about the assignment decisions,
   * not the entire state object.
   *
   * The signature format: "classId:day:startTime:room|classId:day:startTime:room|..."
   * Sorted for consistency so same assignments produce same signature
   */
  private getStateSignature(state: TState): string {
    // Get schedule from state (generic approach)
    const schedule = (state as any).schedule;
    if (!schedule || !Array.isArray(schedule)) {
      return Math.random().toString(36); // Fallback for non-timetable states
    }

    // Create a signature based on class assignments (classId -> day+time+room)
    const assignments: string[] = [];
    for (const entry of schedule) {
      if (entry.classId && entry.timeSlot && entry.room) {
        assignments.push(`${entry.classId}:${entry.timeSlot.day}:${entry.timeSlot.startTime}:${entry.room}`);
      }
    }
    
    // Sort for consistency and join
    return assignments.sort().join('|');
  }

  /**
   * Check if a state is in the tabu list (recently visited)
   */
  private isTabu(signature: string, currentIteration: number): boolean {
    if (!this.config.tabuSearchEnabled) {
      return false;
    }

    const addedAt = this.tabuList.get(signature);
    if (addedAt === undefined) {
      return false;
    }

    // Check if still within tabu tenure
    return (currentIteration - addedAt) < this.config.tabuTenure;
  }

  /**
   * Add a state signature to the tabu list
   */
  private addToTabuList(signature: string, iteration: number): void {
    if (!this.config.tabuSearchEnabled) {
      return;
    }

    this.tabuList.set(signature, iteration);

    // Cleanup if list is too large
    if (this.tabuList.size > this.config.maxTabuListSize) {
      this.cleanupTabuList(iteration);
    }
  }

  /**
   * Remove expired entries from tabu list
   */
  private cleanupTabuList(currentIteration: number): void {
    const expiredKeys: string[] = [];
    
    for (const [key, addedAt] of this.tabuList.entries()) {
      if ((currentIteration - addedAt) >= this.config.tabuTenure) {
        expiredKeys.push(key);
      }
    }

    for (const key of expiredKeys) {
      this.tabuList.delete(key);
    }

    // If still too large, remove oldest entries
    if (this.tabuList.size > this.config.maxTabuListSize * 0.8) {
      const entries = [...this.tabuList.entries()].sort((a, b) => a[1] - b[1]);
      const toRemove = entries.slice(0, Math.floor(entries.length * 0.3));
      for (const [key] of toRemove) {
        this.tabuList.delete(key);
      }
    }
  }

  /**
   * Phase 1 acceptance probability (prioritize hard constraints)
   *
   * Logic:
   * - Always accept if hard violations decrease
   * - Standard SA acceptance if hard violations stay the same
   * - Never accept if hard violations increase
   */
  private acceptanceProbabilityPhase1(
    currentHardViolations: number,
    newHardViolations: number,
    currentFitness: number,
    newFitness: number,
    temperature: number
  ): number {
    // Better hard violations: always accept
    if (newHardViolations < currentHardViolations) {
      return 1.0;
    }

    // Same hard violations: standard SA acceptance
    if (newHardViolations === currentHardViolations) {
      if (newFitness < currentFitness) {
        return 1.0;
      }
      // Standard SA acceptance probability
      // i.e :
      // currentFitness = 150, newFitness = 160, temperature = 1000
      // acceptanceProbability = exp((150 - 160) / 1000) = exp(-10 / 1000) = exp(-0.01) ≈ 0.99005
      // so the chance of accepting a slightly worse solution is about 99%
      return Math.exp((currentFitness - newFitness) / temperature);
    }

    // Worse hard violations: never accept in phase 1
    return 0.0;
  }

  /**
   * Phase 2 acceptance probability (strictly enforce hard constraints)
   *
   * Logic:
   * - NEVER accept if hard violations increase (strict enforcement)
   * - Always accept if hard violations decrease
   * - Standard SA acceptance for soft constraint optimization if hard violations stable
   *
   * This ensures once a feasible solution is found, we never violate hard constraints
   * while optimizing soft constraints.
   */
  private acceptanceProbabilityPhase2(
    bestHardViolations: number,
    newHardViolations: number,
    currentFitness: number,
    newFitness: number,
    temperature: number
  ): number {
    // CRITICAL: NEVER accept solutions that worsen hard violations
    if (newHardViolations > bestHardViolations) {
      return 0.0;
    }

    // If hard violations improved: always accept
    if (newHardViolations < bestHardViolations) {
      return 1.0;
    }

    // Same hard violations: standard SA acceptance based on fitness
    if (newFitness < currentFitness) {
      return 1.0;
    }

    return Math.exp((currentFitness - newFitness) / temperature);
  }

  /**
   * Standard acceptance probability
   */
  private acceptanceProbability(
    currentFitness: number,
    newFitness: number,
    temperature: number
  ): number {
    if (newFitness < currentFitness) {
      return 1.0;
    }

    return Math.exp((currentFitness - newFitness) / temperature);
  }

  /**
   * Get all violations for a state
   */
  private getViolations(state: TState): Violation[] {
    const violations: Violation[] = [];

    for (const constraint of this.constraints) {
      const score = constraint.evaluate(state);

      if (score < 1) {
        // Use getViolations() if available for detailed violation list
        if (constraint.getViolations) {
          const descriptions = constraint.getViolations(state);
          for (const description of descriptions) {
            violations.push({
              constraintName: constraint.name,
              constraintType: constraint.type,
              score: score,
              description: description,
            });
          }
        } else {
          // Fallback to describe() for backward compatibility
          const violation: Violation = {
            constraintName: constraint.name,
            constraintType: constraint.type,
            score: score,
          };

          if (constraint.describe) {
            const description = constraint.describe(state);
            if (description !== undefined) {
              violation.description = description;
            }
          }

          violations.push(violation);
        }
      }
    }

    return violations;
  }

  /**
   * Update operator statistics
   */
  private updateOperatorStats(): void {
    for (const operatorName in this.operatorStats) {
      const stats = this.operatorStats[operatorName]!;
      if (stats.attempts > 0) {
        stats.successRate = stats.improvements / stats.attempts;
      }
    }
  }

  /**
   * Log operator statistics
   */
  private logOperatorStats(): void {
    this.log('info', 'Operator Statistics:');

    for (const operatorName in this.operatorStats) {
      const stats = this.operatorStats[operatorName]!;
      this.log('info', `  ${operatorName}: Attempts = ${stats.attempts}, Improvements = ${stats.improvements}, Accepted = ${stats.accepted}, Success Rate = ${(stats.successRate * 100).toFixed(2)}%`);
    }
  }

  /**
   * Merge config with defaults
   */
  private mergeWithDefaults(config: SAConfig<TState>): SAConfig<TState> & {
    reheatingFactor: number;
    maxReheats: number;
    tabuSearchEnabled: boolean;
    tabuTenure: number;
    maxTabuListSize: number;
    enableIntensification: boolean;
    intensificationIterations: number;
    maxIntensificationAttempts: number;
    logging: Required<NonNullable<SAConfig<TState>['logging']>>;
  } {
    return {
      ...config,
      reheatingFactor: config.reheatingFactor ?? 2.0,
      maxReheats: config.maxReheats ?? 3,
      // Tabu Search defaults
      tabuSearchEnabled: config.tabuSearchEnabled ?? false,
      tabuTenure: config.tabuTenure ?? 50,
      maxTabuListSize: config.maxTabuListSize ?? 1000,
      // Intensification defaults
      enableIntensification: config.enableIntensification ?? true,
      intensificationIterations: config.intensificationIterations ?? 2000,
      maxIntensificationAttempts: config.maxIntensificationAttempts ?? 3,
      logging: {
        enabled: config.logging?.enabled ?? true,
        level: config.logging?.level ?? 'info',
        logInterval: config.logging?.logInterval ?? 1000,
        output: config.logging?.output ?? 'console',
        filePath: config.logging?.filePath ?? './sa-optimization.log',
      },
    };
  }

  /**
   * Logging helper
   */
  private log(level: string, message: string, data?: any): void {
    if (!this.config.logging.enabled) return;

    const logLevels = ['debug', 'info', 'warn', 'error', 'none'];
    const currentLevelIndex = logLevels.indexOf(this.config.logging.level);
    const messageLevelIndex = logLevels.indexOf(level);

    if (messageLevelIndex < currentLevelIndex) return;

    const timestamp = new Date().toISOString();
    const logMessage = data
      ? `[${timestamp}] [${level.toUpperCase()}] ${message} ${JSON.stringify(data)}`
      : `[${timestamp}] [${level.toUpperCase()}] ${message}`;

    if (this.config.logging.output === 'console' || this.config.logging.output === 'both') {
      console.log(logMessage);
    }

    // File logging could be implemented here if needed
  }

  /**
   * Get current operator statistics
   */
  getStats(): OperatorStats {
    return this.operatorStats;
  }
}
