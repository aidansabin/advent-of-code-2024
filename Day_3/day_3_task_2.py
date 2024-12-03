import re

# Regex patterns
mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r'don\'t\(\)')

total = 0       # variable to track total sum of multiplying all matching methods
enabled = True  # variable to track if mul operations are enabled (default is enabled)

# Read the file and process it line by line
with open('Day_3/input.txt', 'r') as file:
    
    for line in file:
        
        # Split line into segments between the 'dont_pattern'
        segments = dont_pattern.split(line)

        # Split these segments again on the 'do_pattern'
        segments = [do_pattern.split(segment) for segment in segments]

        first_segment = True
        # Each segment (except the first) is after a don't() call
        for segment in segments:

            # Set enabled to false as it is after a don't() call
            if not first_segment:
                enabled = False

            first_subsegment = True
            # Each subsegment (except the first) is after a do() call
            for subsegment in segment:
                
                if not first_subsegment:
                    enabled = True
                
                if enabled:
                    for x, y in mul_pattern.findall(subsegment):
                        total += int(x) * int(y)

                first_subsegment = False

            first_segment = False

# 59097164
print(total)