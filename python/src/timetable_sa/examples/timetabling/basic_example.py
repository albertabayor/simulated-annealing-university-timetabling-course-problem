"""
Basic example of using timetable-sa for university course scheduling.

This example demonstrates:
1. Loading data from Excel
2. Creating initial state
3. Defining constraints
4. Running optimization
5. Displaying results
"""

from timetable_sa import SimulatedAnnealing, SAConfig
from timetable_sa.core.interfaces.config import LoggingConfig
from timetable_sa.examples.timetabling import (
    load_sample_data,
    create_initial_state,
    generate_default_time_slots,
    NoRoomConflict,
    NoLecturerConflict,
    NoProdiConflict,
    Compactness,
    ChangeTimeSlot,
    ChangeRoom,
    SwapClasses,
)
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


def main():
    """Run a basic timetabling optimization example."""
    print("=" * 60)
    print("Timetable SA - Basic Example")
    print("=" * 60)
    
    # Load sample data
    print("\n1. Loading sample data...")
    rooms, lecturers, classes = load_sample_data()
    print(f"   Loaded {len(rooms)} rooms, {len(lecturers)} lecturers, {len(classes)} classes")
    
    # Generate time slots
    print("\n2. Generating time slots...")
    time_slots = generate_default_time_slots()
    print(f"   Generated {len(time_slots)} time slots")
    
    # Create initial state
    print("\n3. Creating initial random state...")
    state = create_initial_state(classes, rooms, lecturers, time_slots, random_seed=42)
    print(f"   Created state with {len(state.schedule)} scheduled classes")
    
    # Define constraints
    print("\n4. Defining constraints...")
    constraints = [
        NoRoomConflict(),
        NoLecturerConflict(),
        NoProdiConflict(),
        Compactness(weight=5.0),
    ]
    print(f"   Added {len(constraints)} constraints")
    
    # Define move generators
    print("\n5. Defining move generators...")
    moves = [
        ChangeTimeSlot(),
        ChangeRoom(),
        SwapClasses(),
    ]
    print(f"   Added {len(moves)} move generators")
    
    # Configure SA
    print("\n6. Configuring Simulated Annealing...")
    logging_config = LoggingConfig()
    logging_config.enabled = True
    logging_config.level = "info"
    logging_config.log_interval = 500
    logging_config.output = "console"
    logging_config.file_path = "timetable.log"
    
    config = SAConfig(
        initial_temperature=1000.0,
        min_temperature=0.1,
        cooling_rate=0.995,
        max_iterations=5000,
        hard_constraint_weight=10000.0,
        clone_state=clone_state,
        enable_intensification=True,
        intensification_iterations=1000,
        max_intensification_attempts=3,
        logging=logging_config,
    )
    print(f"   Temperature: {config.initial_temperature}")
    print(f"   Max iterations: {config.max_iterations}")
    print(f"   Cooling rate: {config.cooling_rate}")
    
    # Run optimization
    print("\n7. Running optimization...")
    print("-" * 60)
    
    sa = SimulatedAnnealing(state, constraints, moves, config)
    solution = sa.solve()
    
    print("-" * 60)
    
    # Display results
    print("\n8. Optimization Results:")
    print(f"   Final fitness: {solution['fitness']:.4f}")
    print(f"   Hard violations: {solution['hard_violations']}")
    print(f"   Soft violations: {solution['soft_violations']}")
    print(f"   Total iterations: {solution['iterations']}")
    print(f"   Reheats: {solution['reheats']}")
    print(f"   Final temperature: {solution['final_temperature']:.4f}")
    
    # Show constraint violations
    if solution['violations']:
        print("\n   Constraint violations:")
        for v in solution['violations'][:5]:  # Show first 5
            print(f"   - {v['constraint_name']}: {v['description']}")
        if len(solution['violations']) > 5:
            print(f"   ... and {len(solution['violations']) - 5} more")
    else:
        print("\n   No constraint violations!")
    
    # Show operator statistics
    print("\n9. Operator Statistics:")
    for name, stats in solution['operator_stats'].items():
        print(f"   {name}: {stats['attempts']} attempts, "
              f"{stats['improvements']} improvements, "
              f"{stats['success_rate']*100:.1f}% success rate")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
