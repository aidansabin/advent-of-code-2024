import re

# Regex pattern to match 'mul(x,y)' format (includes capture groups to separate values)
mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

total = 0   # variable to track total sum of multiplying all matching methods

# Read the file and process it line by line
with open('Day_3/input.txt', 'r') as file:
    for line in file:
        
        # Process each match one by one, extracting values from the capture groups
        for x, y in mul_pattern.findall(line):
            
            # Multiply values and add to total 
            total += int(x) * int(y)

print(total)
