# Read the file
with open('Day_1/input.py', 'r') as file:
    lines = file.readlines()

# Store the values
first_values = []
second_values = []

# Extract values from each line
for line in lines:
    first, second = map(int, line.split())
    first_values.append(first)
    second_values.append(second)

# Sort into ascending order
first_values.sort()
second_values.sort()

# Calculate result from differences at each index of sorted array
result = 0
for i in range(0, len(first_values)):
    first = first_values[i]
    second = second_values[i]
    result += abs(first - second)

print(result)