MAX_DIFF = 3
MIN_DIFF = 1

# Read input values
with open('Day_2/input.py', 'r') as file:
    reports = [[int(value) for value in line.split()] for line in file]

# Tests a report to see if it is safe or unsafe
def test_report(report):

    # Check the first two values to determine if increasing or decreasing
    increasing = report[0] - report[1] < 0

    # Precompute differences (to reduce redundant calulations)
    differences = [report[i- 1] - report[i] for i in range(1, len(report))]

    for diff in differences:
        
        # If it is not increasing/decreasing consistently, exit as this report is not safe
        if (diff < 0) != increasing:
            return False
        
        # Check that difference is only changing by accepted boundaries
        if abs(diff) > MAX_DIFF or abs(diff) < MIN_DIFF:
            return False
        
    return True     # if we encounter no issues, the report is marked as safe
    
safe_reports = 0

# Check each report individually
for report in reports:

    # If the report is safe increment counter and continue to the next report
    if test_report(report):
        safe_reports += 1
        print(f"Report is safe: {report}")
        continue
    
    # Remove a value at a time to see if this makes the report safe (dampener)
    is_safe = False
    for i in range(len(report)):
        if test_report(report[:i] + report[i + 1:]):
            is_safe = True
            break
            
    # Increment counter if safe
    if is_safe:
        safe_reports += 1
        print(f"Report is safe: {report}")
    else:
        print(f"Report is unsafe: {report}")
        

print(f"Number of safe reports: {safe_reports}")