"""Full optimization with real UISI data."""

import sys
sys.path.insert(0, '/home/emmanuelabayor/projects/timetable-sa/python/src')

import random
import copy
import json
import time as time_python

from timetable_sa import SimulatedAnnealing, SAConfig
from timetable_sa.examples.timetabling import (
    generate_default_time_slots,
    NoRoomConflict,
    NoLecturerConflict,
    NoProdiConflict,
    RoomCapacity,
    MaxDailyPeriods,
    FridayTimeRestriction,
    NoFridayPrayConflict,
    PrayerTimeStart,
    ClassTypeTime,
    SaturdayRestriction,
    Compactness,
    OverflowPenalty,
    PreferredRoom,
    PreferredTime,
    TransitTime,
    ResearchDay,
    PrayerTimeOverlap,
    EveningClassPriority,
    ChangeTimeSlot,
    ChangeRoom,
    SwapClasses,
    ChangeTimeSlotAndRoom,
    FixRoomConflict,
    FixLecturerConflict,
    FixRoomCapacity,
    FixMaxDailyPeriods,
    FixFridayPrayerConflict,
    FixClassTypeTime,
    SwapFridayWithNonFriday,
)
from timetable_sa.examples.timetabling.domain_types.domain import (
    Room, Lecturer, TimeSlot, ClassRequirement
)
from timetable_sa.examples.timetabling.domain_types.state import (
    ScheduleEntry, TimetableState
)
from timetable_sa.examples.timetabling.utils.time import (
    time_to_minutes,
    calculate_end_time,
    is_valid_friday_start_time,
    is_starting_during_prayer_time,
)
from timetable_sa.examples.timetabling.utils.class_helper import has_class_overlap
from timetable_sa.examples.timetabling.data.excel_loader import load_uisi_data
import json


def create_greedy_initial_state_v2(
    classes: list[ClassRequirement],
    rooms: list[Room],
    lecturers: list[Lecturer],
    time_slots: list[TimeSlot],
    random_seed: int | None = None
) -> TimetableState:
    """Create initial state using greedy assignment (matches TypeScript approach exactly).

    This version exactly matches the TypeScript initial-solution.ts.
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate pagi and sore slots like TypeScript's initializeTimeSlots
    from timetable_sa.examples.timetabling.utils.time import time_to_minutes
    
    def generate_ts_slots(start_time: str, end_time: str, slot_duration: int = 50) -> list[TimeSlot]:
        slots = []
        end_min = time_to_minutes(end_time)
        
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            hour = time_to_minutes(start_time) // 60
            minute = time_to_minutes(start_time) % 60
            period = 1
            
            while True:
                current_min = hour * 60 + minute
                if current_min >= end_min:
                    break
                
                slot_start = f"{hour:02d}:{minute:02d}"
                
                end_min_calc = minute + slot_duration
                end_hour = hour + end_min_calc // 60
                end_minute = end_min_calc % 60
                
                end_time_calc = end_hour * 60 + end_minute
                if end_time_calc > end_min:
                    break
                
                slot_end = f"{end_hour:02d}:{end_minute:02d}"
                
                if hour == 19 and minute == 20:
                    slots.append(TimeSlot(
                        day=day,
                        start_time=slot_start,
                        end_time=slot_end,
                        period=period
                    ))
                    break
                
                slots.append(TimeSlot(
                    day=day,
                    start_time=slot_start,
                    end_time=slot_end,
                    period=period
                ))
                
                minute = end_minute
                
                hour_adjusted = False
                if minute == 50 and hour == 15:
                    minute -= 20
                elif hour == 18 and minute == 50:
                    minute -= 20
                    hour_adjusted = True
                
                if minute >= 60:
                    hour += minute // 60
                    minute = minute % 60
                elif not hour_adjusted:
                    hour = end_hour
                
                period += 1
        
        return slots
    
    # Generate pagi and sore slots exactly like TypeScript
    TIME_SLOTS_PAGI = generate_ts_slots("07:30", "15:30", 50)
    TIME_SLOTS_SORE = generate_ts_slots("15:30", "21:00", 50)
    
    # Filter evening slots (start >= 18:00) like TypeScript
    EVENING_START_MINUTES = time_to_minutes("18:00")
    TIME_SLOTS_EVENING = [s for s in TIME_SLOTS_SORE if time_to_minutes(s.start_time) >= EVENING_START_MINUTES]
    
    schedule: list[ScheduleEntry] = []
    skipped = []
    success_count = 0
    
    # Shuffle classes for random placement order (matching TypeScript)
    shuffled_classes = list(classes)
    random.shuffle(shuffled_classes)
    
    def has_class_overlap(kelas1: str, kelas2: str) -> bool:
        """Check if two classes have overlapping class codes (matches TypeScript)."""
        classes1 = [c.strip().upper() for c in kelas1.split(',')]
        classes2 = [c.strip().upper() for c in kelas2.split(',')]
        for c1 in classes1:
            for c2 in classes2:
                if c1 == c2:
                    return True
        return False
    
    def has_time_overlap(start1: str, end1: str, start2: str, end2: str) -> bool:
        """Check if two time ranges overlap."""
        s1 = time_to_minutes(start1)
        e1 = time_to_minutes(end1)
        s2 = time_to_minutes(start2)
        e2 = time_to_minutes(end2)
        return s1 < e2 and s2 < e1
    
    def has_conflict(new_entry: ScheduleEntry, existing_schedule: list[ScheduleEntry]) -> bool:
        """Check if new entry conflicts with any existing entry (matches TypeScript)."""
        for existing in existing_schedule:
            if new_entry.time_slot.day != existing.time_slot.day:
                continue
            
            # Calculate actual end times based on SKS (matching TypeScript)
            end1, _ = calculate_end_time(new_entry.time_slot.start_time, new_entry.sks, new_entry.time_slot.day)
            end2, _ = calculate_end_time(existing.time_slot.start_time, existing.sks, existing.time_slot.day)
            
            if not has_time_overlap(new_entry.time_slot.start_time, end1,
                                    existing.time_slot.start_time, end2):
                continue
            
            # 1. Room conflict
            if new_entry.room == existing.room:
                return True
            
            # 2. Lecturer conflict
            for lect in new_entry.lecturers:
                if lect in existing.lecturers:
                    return True
            
            # 3. Prodi/Class conflict
            if new_entry.prodi == existing.prodi and has_class_overlap(new_entry.kelas, existing.kelas):
                return True
        
        return False
    
    for class_req in shuffled_classes:
        lecturers_list = class_req.get_lecturers()
        
        if not lecturers_list:
            skipped.append(f"{class_req.kode_matakuliah}: No lecturers")
            continue
        
        # Get class properties (matching TypeScript)
        participants = class_req.peserta
        needs_lab = class_req.needs_lab()
        class_type = class_req.class_type.lower()
        prodi = class_req.prodi
        sks = class_req.sks
        
        # Filter time slots exactly like TypeScript
        # Use TIME_SLOTS_PAGI for pagi, TIME_SLOTS_SORE for sore
        slots = TIME_SLOTS_SORE if class_type == 'sore' else TIME_SLOTS_PAGI
        
        # Filter Saturday for non-Magister Manajemen (matching TypeScript)
        is_mm = 'magister manajemen' in prodi.lower()
        if not is_mm:
            slots = [s for s in slots if s.day != 'Saturday']
        
        if not slots:
            skipped.append(f"{class_req.kode_matakuliah}: No valid slots")
            continue
        
        placed = False
        
        for slot in slots:
            # Find suitable rooms (matching TypeScript logic)
            suitable_rooms = []
            for r in rooms:
                # Check capacity
                if r.capacity < participants:
                    continue
                # Check lab requirement
                if needs_lab and 'lab' not in r.type.lower():
                    continue
                suitable_rooms.append(r)
            
            if not suitable_rooms:
                continue
            
            random.shuffle(suitable_rooms)
            
            # Try each suitable room until find one without conflict
            for room in suitable_rooms:
                end_time, prayer_time = calculate_end_time(slot.start_time, sks, slot.day)
                
                entry = ScheduleEntry(
                    class_id=class_req.kode_matakuliah,
                    class_name=class_req.mata_kuliah,
                    kelas=class_req.kelas,
                    prodi=prodi,
                    lecturers=lecturers_list,
                    room=room.code,
                    time_slot=TimeSlot(
                        day=slot.day,
                        start_time=slot.start_time,
                        end_time=end_time,
                        period=slot.period
                    ),
                    sks=sks,
                    needs_lab=needs_lab,
                    participants=participants,
                    class_type=class_type,
                )
                
                if not has_conflict(entry, schedule):
                    schedule.append(entry)
                    placed = True
                    success_count += 1
                    break
            
            if placed:
                break
        
        if not placed:
            skipped.append(f"{class_req.kode_matakuliah}: No available slot")
    
    print(f"   Placed: {success_count}/{len(classes)}")
    if skipped:
        for s in skipped[:10]:
            print(f"   Skipped: {s}")
        if len(skipped) > 10:
            print(f"   ... and {len(skipped) - 10} more")
    
    # Verify no conflicts
    conflict_count = 0
    for entry in schedule:
        if has_conflict(entry, [e for e in schedule if e.class_id != entry.class_id]):
            conflict_count += 1
    
    if conflict_count > 0:
        print(f"   WARNING: {conflict_count} entries have conflicts!")
    else:
        print(f"   No conflicts in initial state")
    
    # Save result for analysis
    import json
    result = [{
        'class_id': e.class_id,
        'class_name': e.class_name,
        'kelas': e.kelas,
        'prodi': e.prodi,
        'lecturers': e.lecturers,
        'room': e.room,
        'day': e.time_slot.day,
        'start_time': e.time_slot.start_time,
        'end_time': e.time_slot.end_time,
        'period': e.time_slot.period,
        'sks': e.sks,
        'class_type': e.class_type,
    } for e in schedule]
    
    with open('initial-solution.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=time_slots,
        rooms=rooms,
        lecturers=lecturers,
    )


def main():
    print("=" * 60)
    print("University Course Timetabling - Full Optimization")
    print("=" * 60)
    
    # Load real data
    print("\n1. Loading UISI data from Excel...")
    result = load_uisi_data()
    rooms, lecturers, classes = result[0], result[1], result[2]
    print(f"   Loaded {len(rooms)} rooms, {len(lecturers)} lecturers, {len(classes)} classes")
    
    # Generate time slots - matching TypeScript's timeslot-generator.ts
    print("\n2. Generating time slots...")
    
    # TypeScript PAGI: 07:30-15:30, SORE: 15:30-21:00, slotDuration=50
    # Only SORE slots with start >= 18:00 are included in combined TIME_SLOTS
    from timetable_sa.examples.timetabling.utils.time import time_to_minutes
    
    def generate_ts_slots(start_time: str, end_time: str, slot_duration: int = 50) -> list[TimeSlot]:
        """Generate slots matching TypeScript's generateTimeSlots exactly."""
        slots = []
        start_min = time_to_minutes(start_time)
        end_min = time_to_minutes(end_time)
        
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            hour = time_to_minutes(start_time) // 60
            minute = time_to_minutes(start_time) % 60
            period = 1
            
            while True:
                current_min = hour * 60 + minute
                if current_min >= end_min:
                    break
                
                slot_start = f"{hour:02d}:{minute:02d}"
                
                # Calculate end time
                end_min_calc = minute + slot_duration
                end_hour = hour + end_min_calc // 60
                end_minute = end_min_calc % 60
                
                end_time_calc = end_hour * 60 + end_minute
                if end_time_calc > end_min:
                    break
                
                slot_end = f"{end_hour:02d}:{end_minute:02d}"
                
                # Special handling for prayer time breaks (matches TypeScript - break AFTER creating slot)
                if hour == 19 and minute == 20:
                    slots.append(TimeSlot(
                        day=day,
                        start_time=slot_start,
                        end_time=slot_end,
                        period=period
                    ))
                    break
                
                slots.append(TimeSlot(
                    day=day,
                    start_time=slot_start,
                    end_time=slot_end,
                    period=period
                ))
                
                # Move to next slot
                minute = end_minute
                
                # Prayer time adjustments (matches TypeScript exactly)
                # Track if we manually adjust hour to skip else branch
                hour_adjusted = False
                if minute == 50 and hour == 15:
                    minute -= 20
                elif hour == 18 and minute == 50:
                    minute -= 20
                    # NOTE: TypeScript does NOT increment hour here!
                    # The else branch below will handle the hour update
                    hour_adjusted = True
                
                if minute >= 60:
                    hour += minute // 60
                    minute = minute % 60
                elif not hour_adjusted:
                    hour = end_hour
                
                period += 1
        
        return slots
    
    # Generate pagi and sore slots like TypeScript
    pagi_slots = generate_ts_slots("07:30", "15:30", 50)  # 54 slots (9/day x 6)
    sore_slots = generate_ts_slots("15:30", "21:00", 50)  # 42 slots (7/day x 6)
    
    # Only include sore slots with start >= 18:00 (matches TypeScript initializeTimeSlots)
    evening_slots = [s for s in sore_slots if time_to_minutes(s.start_time) >= time_to_minutes("18:00")]
    
    time_slots = pagi_slots + evening_slots  # 54 + 18 = 72 slots
    
    print(f"   Generated {len(time_slots)} time slots (PAGI: {len(pagi_slots)}, EVENING: {len(evening_slots)})")
    
    # Create initial state with greedy algorithm
    print("\n3. Creating initial state using greedy assignment...")
    state = create_greedy_initial_state_v2(classes, rooms, lecturers, time_slots)
    print(f"   Created schedule with {len(state.schedule)} entries")
    
    # Define all hard constraints
    print("\n4. Defining constraints...")

    hard_constraints = [
        NoRoomConflict(),
        NoLecturerConflict(),
        NoProdiConflict(),
        RoomCapacity(),
        MaxDailyPeriods(),
        FridayTimeRestriction(),
        NoFridayPrayConflict(),
        PrayerTimeStart(),
        ClassTypeTime(),
        SaturdayRestriction(),
    ]
    print(f"   Added {len(hard_constraints)} hard constraints")
    
    soft_constraints = [
        Compactness(),
        OverflowPenalty(),
        PreferredRoom(),
        PreferredTime(),
        TransitTime(),
        ResearchDay(),
        PrayerTimeOverlap(),
        EveningClassPriority(),
    ]
    print(f"   Added {len(soft_constraints)} soft constraints")
    
    all_constraints = hard_constraints + soft_constraints
    
    # Define all move generators
    print("\n5. Defining move generators...")
    move_generators = [
        ChangeTimeSlot(),
        ChangeRoom(),
        SwapClasses(),
        ChangeTimeSlotAndRoom(),
        FixRoomConflict(),
        FixLecturerConflict(),
        FixRoomCapacity(),
        FixMaxDailyPeriods(),
        FixFridayPrayerConflict(),
        FixClassTypeTime(),
        SwapFridayWithNonFriday(),
    ]
    print(f"   Added {len(move_generators)} move generators")
    
    # Configure SA - matching TypeScript parameters
    print("\n6. Configuring Simulated Annealing...")
    from timetable_sa.core.interfaces.config import LoggingConfig
    config = SAConfig(
        tabu_search_enabled=True,
        tabu_tenure=500,
        initial_temperature=100000.0,
        min_temperature=0.0000001,
        cooling_rate=0.9995,
        max_iterations=100000,
        clone_state=lambda s: TimetableState(
            schedule=copy.deepcopy(s.schedule),
            available_time_slots=s.available_time_slots,
            rooms=s.rooms,
            lecturers=s.lecturers,
        ),
        reheating_threshold=2000,
        reheating_factor=2.0,
        max_reheats=3,
        logging=LoggingConfig(
            enabled=True,
            level="info",  # Reduce logging to info for faster execution
            log_interval=1000,
            output="console",
        ),
    )
    print(f"   Temperature: {config.initial_temperature} -> {config.min_temperature}")
    print(f"   Max iterations: {config.max_iterations}")
    print(f"   Cooling rate: {config.cooling_rate}")
    
    # Run optimization
    print("\n7. Running optimization...")
    start_time = time_python.time()

    sa = SimulatedAnnealing(state, all_constraints, move_generators, config)
    result = sa.solve()

    elapsed_time = time_python.time() - start_time
    
    # Print results - using correct result keys
    print("\n" + "=" * 60)
    print("OPTIMIZATION RESULTS")
    print("=" * 60)
    print(f"\nFinal fitness: {result['fitness']:.4f}")
    print(f"Hard violations: {result['hard_violations']}")
    print(f"Soft violations: {result['soft_violations']}")
    print(f"Total iterations: {result['iterations']}")
    print(f"Reheats: {result.get('reheats', 0)}")
    print(f"Final temperature: {result.get('final_temperature', 'N/A'):.2f}")
    print(f"Execution time: {elapsed_time:.2f} seconds")
    
    print("\n--- Operator Statistics ---")
    if 'operator_stats' in result:
        for name, stats in result['operator_stats'].items():
            print(f"  {name}: {stats}")
    
    print("\n--- Constraint Summary ---")
    for constraint in all_constraints:
        violations = constraint.get_violations(result['state'])
        if violations:
            print(f"  {constraint.name}: {len(violations)} violations")
            # Show details for hard constraint violations
            if constraint.type == "hard" and len(violations) > 0:
                for v in violations[:5]:  # Show first 5
                    print(f"    - {v}")
                if len(violations) > 5:
                    print(f"    ... and {len(violations) - 5} more")
    
    print("\n" + "=" * 60)
    print("Optimization completed successfully!")
    print("=" * 60)

    # Save final result to JSON file (matching TypeScript format)
    print("\nSaving final result to timetable-result.json...")
    final_state = result['state']

    # Calculate prayer time additions for entries that need it
    schedule_result = []
    for entry in final_state.schedule:
        end_time, prayer_time_added = calculate_end_time(
            entry.time_slot.start_time, entry.sks, entry.time_slot.day
        )

        # Check if this is an overflow to lab (room has 'lab' but class doesn't need it)
        is_overflow = False
        if not entry.needs_lab and 'lab' in entry.room.lower():
            is_overflow = True

        schedule_result.append({
            "classId": entry.class_id,
            "className": entry.class_name,
            "class": entry.kelas,
            "prodi": entry.prodi,
            "lecturers": entry.lecturers,
            "room": entry.room,
            "timeSlot": {
                "period": entry.time_slot.period,
                "day": entry.time_slot.day,
                "startTime": entry.time_slot.start_time,
                "endTime": entry.time_slot.end_time,
            },
            "sks": entry.sks,
            "needsLab": entry.needs_lab,
            "participants": entry.participants,
            "classType": entry.class_type,
            "prayerTimeAdded": prayer_time_added,
            "isOverflowToLab": is_overflow,
        })

    final_result = {
        "fitness": result['fitness'],
        "hardViolations": result['hard_violations'],
        "softViolations": result['soft_violations'],
        "iterations": result['iterations'],
        "schedule": schedule_result,
    }

    with open('timetable-result.json', 'w') as f:
        json.dump(final_result, f, indent=2, ensure_ascii=False)
    print("   Result saved successfully!")

    return result


if __name__ == "__main__":
    main()
