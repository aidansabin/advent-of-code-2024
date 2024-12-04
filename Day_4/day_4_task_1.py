# Read input into array and remove endline characters
with open('Day_4/input.py', 'r') as file:
    word_search = [line.replace('\n', '') for line in file]

word = 'XMAS'   # word to search for

# Directions to check in
directions = [
    (0, 1),     # right
    (0, -1),    # left
    (1, 0),     # down
    (-1, 0),    # up
    (1, 1),     # down-right
    (-1, -1),   # up-left
    (1, -1),    # down-left
    (-1, 1)     # up-right
]

# Finds the number of instances of 'XMAS' words that can be found, from the provided index which is an 'X'
def find_words_from_start_char(row, col):
    matches = 0

    # Check each direction to see if it finds the word in this direction
    for dx, dy in directions:
        matches += 1 if check_direction(row, col, dx, dy) else 0
        
    return matches

# Checks if a word is found in a given direction, starting at a given position
def check_direction(row, col, dx, dy):
    
    # Only search as long as the word is
    for i in range(len(word)):

        # Return False if it is not within bounds of word search
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        
        # Return False if it does not match expected character at this point of the word
        if word_search[row][col] != word[i]:
            return False

        # Iterate to next position
        col += dx
        row += dy
        

    # If we pass the checks we have found a word
    return True

# Get dimensions of the word search
rows, cols = len(word_search), len(word_search[0])

matches = 0

# Iterate through the word search
for row in range(rows):
    for col in range(cols):
        
        # Only check from 'X' values
        if word_search[row][col] == 'X':
            
            matches += find_words_from_start_char(row, col)

print(matches)