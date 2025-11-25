#!/usr/bin/env python3
"""
Verification Script: Check Actual Conflicts in Final Schedule
Purpose: Verify if violations in report match actual schedule conflicts
"""

import json
from collections import defaultdict
from datetime import datetime, timedelta

def time_to_minutes(time_str):
    """Convert HH:MM to minutes from midnight"""
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def check_time_overlap(start1, end1, start2, end2):
    """Check if two time ranges overlap"""
    s1 = time_to_minutes(start1)
    e1 = time_to_minutes(end1)
    s2 = time_to_minutes(start2)
    e2 = time_to_minutes(end2)
    return s1 < e2 and s2 < e1

def verify_schedule(result_file, violation_file):
    """Verify if violations in report match actual schedule"""
    
    print("="*70)
    print("SCHEDULE VERIFICATION ANALYSIS")
    print("="*70)
    print()
    
    # Load schedule
    with open(result_file) as f:
        schedule = json.load(f)
    
    print(f"✅ Loaded {len(schedule)} scheduled classes")
    print()
    
    # Load violations
    with open(violation_file) as f:
        violations_data = json.load(f)
    
    reported_hard = violations_data['summary']['totalHardViolations']
    reported_soft = violations_data['summary']['totalSoftViolations']
    
    print(f"📊 REPORTED VIOLATIONS:")
    print(f"   Hard: {reported_hard}")
    print(f"   Soft: {reported_soft}")
    print()
    
    # Verify each constraint type
    print("="*70)
    print("ACTUAL CONSTRAINT CHECKING")
    print("="*70)
    print()
    
    actual_violations = {
        'HC1_LecturerConflict': [],
        'HC2_RoomConflict': [],
        'HC3_RoomCapacity': [],
        'HC5_ProdiConflict': [],
        'HC6_ResearchDay': [],
        'HC7_MaxDailyPeriods': [],
        'HC8_ClassTypeTime': [],
        'HC9_SaturdayRestriction': [],
    }
    
    # Check HC1: Lecturer Conflict
    print("🔍 Checking HC1: Lecturer Conflict...")
    lecturer_schedule = defaultdict(list)
    for entry in schedule:
        lecturers = entry['Lecturers'].split(', ') if entry['Lecturers'] else []
        for lec in lecturers:
            lecturer_schedule[lec].append(entry)
    
    for lec, classes in lecturer_schedule.items():
        for i, class1 in enumerate(classes):
            for class2 in classes[i+1:]:
                if class1['Day'] == class2['Day']:
                    if check_time_overlap(
                        class1['Start Time'], class1['End Time'],
                        class2['Start Time'], class2['End Time']
                    ):
                        actual_violations['HC1_LecturerConflict'].append({
                            'lecturer': lec,
                            'class1': class1['Class ID'],
                            'class2': class2['Class ID'],
                            'day': class1['Day'],
                            'time1': f"{class1['Start Time']}-{class1['End Time']}",
                            'time2': f"{class2['Start Time']}-{class2['End Time']}"
                        })
    
    print(f"   Found: {len(actual_violations['HC1_LecturerConflict'])} actual conflicts")
    if actual_violations['HC1_LecturerConflict']:
        print(f"   Examples:")
        for v in actual_violations['HC1_LecturerConflict'][:3]:
            print(f"   - {v['lecturer']}: {v['class1']} vs {v['class2']} on {v['day']}")
    print()
    
    # Check HC2: Room Conflict
    print("🔍 Checking HC2: Room Conflict...")
    room_schedule = defaultdict(list)
    for entry in schedule:
        room_schedule[entry['Room']].append(entry)
    
    for room, classes in room_schedule.items():
        for i, class1 in enumerate(classes):
            for class2 in classes[i+1:]:
                if class1['Day'] == class2['Day']:
                    if check_time_overlap(
                        class1['Start Time'], class1['End Time'],
                        class2['Start Time'], class2['End Time']
                    ):
                        actual_violations['HC2_RoomConflict'].append({
                            'room': room,
                            'class1': class1['Class ID'],
                            'class2': class2['Class ID'],
                            'day': class1['Day'],
                            'time1': f"{class1['Start Time']}-{class1['End Time']}",
                            'time2': f"{class2['Start Time']}-{class2['End Time']}"
                        })
    
    print(f"   Found: {len(actual_violations['HC2_RoomConflict'])} actual conflicts")
    if actual_violations['HC2_RoomConflict']:
        print(f"   Examples:")
        for v in actual_violations['HC2_RoomConflict'][:3]:
            print(f"   - {v['room']}: {v['class1']} vs {v['class2']} on {v['day']}")
    print()
    
    # Check HC5: Prodi Conflict
    print("🔍 Checking HC5: Prodi Conflict...")
    prodi_schedule = defaultdict(list)
    for entry in schedule:
        prodi_schedule[entry['Program']].append(entry)
    
    for prodi, classes in prodi_schedule.items():
        for i, class1 in enumerate(classes):
            for class2 in classes[i+1:]:
                if class1['Day'] == class2['Day']:
                    if check_time_overlap(
                        class1['Start Time'], class1['End Time'],
                        class2['Start Time'], class2['End Time']
                    ):
                        actual_violations['HC5_ProdiConflict'].append({
                            'prodi': prodi,
                            'class1': class1['Class ID'],
                            'class2': class2['Class ID'],
                            'day': class1['Day'],
                            'time1': f"{class1['Start Time']}-{class1['End Time']}",
                            'time2': f"{class2['Start Time']}-{class2['End Time']}"
                        })
    
    print(f"   Found: {len(actual_violations['HC5_ProdiConflict'])} actual conflicts")
    if actual_violations['HC5_ProdiConflict']:
        print(f"   Examples:")
        for v in actual_violations['HC5_ProdiConflict'][:3]:
            print(f"   - {v['prodi']}: {v['class1']} vs {v['class2']} on {v['day']}")
    print()
    
    # Check HC9: Saturday Restriction
    print("🔍 Checking HC9: Saturday Restriction...")
    for entry in schedule:
        if entry['Day'] == 'Saturday':
            prodi = entry['Program'].lower()
            if 'magister manajemen' not in prodi:
                actual_violations['HC9_SaturdayRestriction'].append({
                    'class': entry['Class ID'],
                    'prodi': entry['Program'],
                    'day': entry['Day']
                })
    
    print(f"   Found: {len(actual_violations['HC9_SaturdayRestriction'])} violations")
    if actual_violations['HC9_SaturdayRestriction']:
        print(f"   Examples:")
        for v in actual_violations['HC9_SaturdayRestriction'][:3]:
            print(f"   - {v['class']} ({v['prodi']}) on Saturday")
    print()
    
    # Summary
    print("="*70)
    print("COMPARISON: REPORTED vs ACTUAL")
    print("="*70)
    print()
    
    # Get reported violations by type
    reported_by_type = violations_data['summary']['violationsByType']
    
    comparison = [
        ('HC1: Lecturer Conflict', 
         reported_by_type.get('HC1: Lecturer Conflict', 0),
         len(actual_violations['HC1_LecturerConflict'])),
        ('HC2: Room Conflict',
         reported_by_type.get('HC2: Room Conflict', 0),
         len(actual_violations['HC2_RoomConflict'])),
        ('HC5: Prodi Conflict',
         reported_by_type.get('HC5: Prodi Conflict', 0),
         len(actual_violations['HC5_ProdiConflict'])),
        ('HC9: Saturday Restriction',
         reported_by_type.get('HC9: Saturday Restriction', 0),
         len(actual_violations['HC9_SaturdayRestriction'])),
    ]
    
    print(f"{'Constraint':<30} {'Reported':<15} {'Actual':<15} {'Match?'}")
    print("-"*70)
    
    total_reported = 0
    total_actual = 0
    
    for name, reported, actual in comparison:
        match = '✅ YES' if reported == actual else '❌ NO'
        print(f"{name:<30} {reported:<15} {actual:<15} {match}")
        total_reported += reported
        total_actual += actual
    
    print("-"*70)
    print(f"{'SUBTOTAL':<30} {total_reported:<15} {total_actual:<15}")
    print()
    
    # Conclusion
    print("="*70)
    print("CONCLUSION")
    print("="*70)
    print()
    
    if total_reported > total_actual:
        diff = total_reported - total_actual
        print(f"⚠️  DISCREPANCY DETECTED!")
        print(f"   Reported violations: {total_reported}")
        print(f"   Actual violations: {total_actual}")
        print(f"   Difference: {diff} violations")
        print()
        print("💡 Possible explanations:")
        print("   1. Violation report shows TEMPORAL violations (during SA process)")
        print("   2. Final schedule was optimized after violations were recorded")
        print("   3. Violations in report include intermediate iterations")
        print()
        print("🎯 GOOD NEWS: Final schedule is better than reported!")
        
    elif total_actual > total_reported:
        diff = total_actual - total_reported
        print(f"⚠️  MORE VIOLATIONS THAN REPORTED!")
        print(f"   Reported violations: {total_reported}")
        print(f"   Actual violations: {total_actual}")
        print(f"   Difference: {diff} violations")
        print()
        print("💡 This suggests a bug in violation tracking")
        
    else:
        print(f"✅ PERFECT MATCH!")
        print(f"   Reported violations: {total_reported}")
        print(f"   Actual violations: {total_actual}")
        print()
        print("🎯 Violation report accurately reflects final schedule")
    
    print()
    print("="*70)
    
    # Save detailed analysis
    analysis = {
        'scheduled_classes': len(schedule),
        'reported_violations': {
            'hard': reported_hard,
            'soft': reported_soft,
            'total': reported_hard + reported_soft
        },
        'actual_violations': {
            'HC1_LecturerConflict': len(actual_violations['HC1_LecturerConflict']),
            'HC2_RoomConflict': len(actual_violations['HC2_RoomConflict']),
            'HC5_ProdiConflict': len(actual_violations['HC5_ProdiConflict']),
            'HC9_SaturdayRestriction': len(actual_violations['HC9_SaturdayRestriction']),
        },
        'detailed_violations': actual_violations
    }
    
    with open('schedule_verification_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print("💾 Detailed analysis saved to: schedule_verification_analysis.json")
    print()

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python verify_schedule.py <result_file.json> <violation_file.json>")
        print()
        print("Example:")
        print("  python verify_schedule.py timetable_result_v3.json violation_report_v3.json")
        sys.exit(1)
    
    result_file = sys.argv[1]
    violation_file = sys.argv[2]
    
    try:
        verify_schedule(result_file, violation_file)
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON - {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()