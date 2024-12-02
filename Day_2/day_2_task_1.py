MAX_DIFF = 3
MIN_DIFF = 1

with open('Day_2/input.py', 'r') as file:
    reports = [[int(value) for value in line.split()] for line in file]

safe_reports = 0

# Check each report individually
for report in reports:
    
    print(report)

    is_safe = True  # report is marked as safe until proven otherwise
    
    # Check the first two values to determine if increasing or decreasing
    increasing = report[0] - report[1] < 0

    # Iterate through all values in report
    for i in range(1, len(report)):
        
        diff = report[i - 1] - report[i]    # get difference for comparison

        # If it is not increasing/decreasing consistently, exit as this report is not safe
        if (diff < 0) != increasing:
            is_safe = False
            print("Report was not consistently increasing or decreasing")
            break
        
        # Check that difference is only changing by accepted boundaries
        if abs(diff) > MAX_DIFF or abs(diff) < MIN_DIFF:
            print(f"Report had adjacent values that did not change by between {MIN_DIFF} and {MAX_DIFF}")
            is_safe = False
            break
        
    # If we checked all values without finding a reason to mark it unsafe, increment safe reports counter
    if is_safe:
        safe_reports += 1

print(f"Number of safe reports: {safe_reports}")