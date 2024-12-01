# Read the file
with open('Day_1/input.py', 'r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

# Store the values and sort them into ascending order
first_values = sorted(pair[0] for pair in pairs)
second_values = sorted(pair[1] for pair in pairs)

similarity = 0
f_idx = 0   # pointer for first array
s_idx = 0   # pointer for second array

# Continue until reached the end of either list (no more matches possible)
while f_idx < len(first_values) and s_idx < len(second_values):
    
    # We have found a match
    if first_values[f_idx] == second_values[s_idx]:
        
        value = first_values[f_idx]     # store value of match

        # Iterate through first array to find number of occurences of this value in first array
        f_count = 0
        while f_idx < len(first_values) and first_values[f_idx] == value:
            f_count += 1
            f_idx += 1

        # Iterate through second array to find number of matches in second array
        s_count = 0
        while s_idx < len(second_values) and second_values[s_idx] == value:
            s_count += 1
            s_idx += 1

        # Update similarity score
        similarity += (value * s_count) * f_count

    # Our value in first array is less than value in second array so we need to 'catch up' to it by getting the next value in our first array
    elif first_values[f_idx] < second_values[s_idx]:
        f_idx += 1

    # Our value in second array is less than value in first array so we need to 'catch up' to it by getting the next value in our second array
    elif first_values[f_idx] > second_values[s_idx]:
        s_idx += 1

print(similarity)