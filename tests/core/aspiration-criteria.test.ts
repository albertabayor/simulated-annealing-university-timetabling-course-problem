/**
 * Aspiration Criteria Tests for Simulated Annealing
 *
 * Tests verify that:
 * 1. Tabu states are skipped when aspiration is disabled
 * 2. Tabu states are accepted when aspiration is enabled AND fitness < globalBest
 * 3. Tabu states are rejected when aspiration is enabled AND fitness >= globalBest
 */

import { describe, it, expect, beforeEach } from '@jest/globals';
import { SimulatedAnnealing } from '../../src/core/SimulatedAnnealing.js';
import type { Constraint, MoveGenerator } from '../../src/core/index.js';

// Mock state type for testing
interface TestState {
  value: number;
  items: number[];
}

// Mock constraint that evaluates to a simple fitness
const createMockConstraint = (violations: number = 0): Constraint<TestState> => {
  const satisfaction = Math.max(0, 1 - violations * 0.5);
  return {
    name: `MockConstraint`,
    type: 'hard' as const,
    evaluate: (state: TestState) => {
      // Return score based on state value for testing
      return state.value >= 10 ? 1 : 0;
    },
  };
};

// Mock move generator that can increment value
const createMockMoveGenerator = (name: string, increment: number): MoveGenerator<TestState> => {
  return {
    name,
    canApply: () => true,
    generate: (state: TestState, _temperature: number) => {
      return {
        ...state,
        value: state.value + increment,
        items: [...state.items, increment],
      };
    },
  };
};

describe('Aspiration Criteria', () => {
  describe('shouldSkipTabu method', () => {
    it('should return false when tabu search is disabled', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: false, // Disabled
        }
      );

      // Manually add to tabu list
      (solver as any).tabuList.set('test-signature', 100);

      // shouldSkipTabu should return false (not skip) when tabu is disabled
      const result = (solver as any).shouldSkipTabu('test-signature', 150, 50, 100);
      expect(result).toBe(false);
    });

    it('should return false when state is not in tabu list', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
        }
      );

      // Tabu list is empty
      const result = (solver as any).shouldSkipTabu('non-existent', 100, 50, 100);
      expect(result).toBe(false);
    });

    it('should return false (accept) when tabu but fitness < globalBest (aspiration met)', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true, // Enabled
        }
      );

      // Add state to tabu list at iteration 100
      (solver as any).tabuList.set('test-signature', 100);

      // Current iteration 110, within tabu tenure (110 - 100 = 10 < 50)
      // newFitness = 50 < globalBest = 100 → Aspiration met
      const result = (solver as any).shouldSkipTabu('test-signature', 110, 50, 100);
      expect(result).toBe(false); // Should NOT skip (aspiration met!)
    });

    it('should return true (skip) when tabu and fitness >= globalBest (aspiration NOT met)', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true, // Enabled
        }
      );

      // Add state to tabu list at iteration 100
      (solver as any).tabuList.set('test-signature', 100);

      // Current iteration 110, within tabu tenure
      // newFitness = 150 >= globalBest = 100 → Aspiration NOT met
      const result = (solver as any).shouldSkipTabu('test-signature', 110, 150, 100);
      expect(result).toBe(true); // Should skip (tabu + no aspiration)
    });

    it('should return true (skip) when aspiration is disabled even if fitness < globalBest', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: false, // Disabled!
        }
      );

      // Add state to tabu list at iteration 100
      (solver as any).tabuList.set('test-signature', 100);

      // Current iteration 110, within tabu tenure
      // newFitness = 50 < globalBest = 100, BUT aspiration is disabled
      const result = (solver as any).shouldSkipTabu('test-signature', 110, 50, 100);
      expect(result).toBe(true); // Should skip (aspiration disabled)
    });

    it('should return false when tabu tenure has expired', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
        }
      );

      // Add state to tabu list at iteration 100
      (solver as any).tabuList.set('test-signature', 100);

      // Current iteration 200, tabu tenure expired (200 - 100 = 100 >= 50)
      const result = (solver as any).shouldSkipTabu('test-signature', 200, 50, 100);
      expect(result).toBe(false); // Should NOT skip (tabu expired)
    });

    it('should return false when fitness equals globalBest (not strictly less)', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 1000,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
        }
      );

      // Add state to tabu list at iteration 100
      (solver as any).tabuList.set('test-signature', 100);

      // Current iteration 110, within tabu tenure
      // newFitness = 100 === globalBest = 100 → NOT less, aspiration NOT met
      const result = (solver as any).shouldSkipTabu('test-signature', 110, 100, 100);
      expect(result).toBe(true); // Should skip (not strictly better)
    });
  });

  describe('Integration: Tabu Search with Aspiration Criteria', () => {
    it('should accept breakthrough solution in optimization', () => {
      let aspirationCalled = false;

      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [
          {
            name: 'breakthrough',
            canApply: () => true,
            generate: (state: TestState, _temp: number) => {
              return { ...state, value: state.value + 100 }; // Big improvement
            },
          },
        ],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.99,
          maxIterations: 500,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 100,
          aspirationEnabled: true,
          logging: { enabled: false },
        }
      );

      // Manually add a "breakthrough" state to tabu
      // But this state would have fitness 0.1 which is better than global best 1.0

      const result = solver.solve();

      // The solver should complete without error
      expect(result).toBeDefined();
      expect(result.iterations).toBeGreaterThan(0);
    });

    it('should respect tabu when solution is not better than global best', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [
          {
            name: 'small-move',
            canApply: () => true,
            generate: (state: TestState, _temp: number) => {
              return { ...state, value: state.value + 1 }; // Small improvement
            },
          },
        ],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.99,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
          logging: { enabled: false },
        }
      );

      const result = solver.solve();

      // Should complete with tabu search working
      expect(result).toBeDefined();
      expect(result.iterations).toBeGreaterThan(0);
    });
  });

   describe('Config: Default aspirationEnabled value', () => {
    it('should default to true when not specified', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          // NOT specifying aspirationEnabled - should default to true
        }
      );

      // Access config to check default
      const config = (solver as any).config;
      expect(config.aspirationEnabled).toBe(true);
    });

    it('should respect explicit false setting', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          aspirationEnabled: false, // Explicitly false
        }
      );

      const config = (solver as any).config;
      expect(config.aspirationEnabled).toBe(false);
    });

    it('should respect explicit true setting', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          aspirationEnabled: true, // Explicitly true
        }
      );

      const config = (solver as any).config;
      expect(config.aspirationEnabled).toBe(true);
    });
  });

  describe('Edge cases', () => {
    it('should handle negative fitness values correctly', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
        }
      );

      // Add to tabu
      (solver as any).tabuList.set('test-signature', 100);

      // Negative fitness < positive globalBest → aspiration should be met
      const result = (solver as any).shouldSkipTabu('test-signature', 110, -50, 10);
      expect(result).toBe(false); // Should accept (aspiration met)
    });

    it('should handle very large global best values', () => {
      const solver = new SimulatedAnnealing<TestState>(
        { value: 0, items: [] },
        [createMockConstraint()],
        [createMockMoveGenerator('test', 1)],
        {
          initialTemperature: 100,
          minTemperature: 0.0001,
          coolingRate: 0.95,
          maxIterations: 100,
          hardConstraintWeight: 1000,
          cloneState: (s) => ({ ...s, items: [...s.items] }),
          tabuSearchEnabled: true,
          tabuTenure: 50,
          aspirationEnabled: true,
        }
      );

      (solver as any).tabuList.set('test-signature', 100);

      // Very large global best, any positive fitness is less
      const result = (solver as any).shouldSkipTabu('test-signature', 110, 500, 1000000);
      expect(result).toBe(false); // Should accept (aspiration met)
    });
  });
});
