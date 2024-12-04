# Read input into array and remove endline characters
with open('Day_4/input.py', 'r') as file:
    word_search = [line.replace('\n', '') for line in file]

word = 'MAS'   # word to search for

def validate_word_in_direction_from_position(row, col, dx, dy):
    constructed_word = ""

    while len(constructed_word) < len(word):
        
        # Return False if it is not within bounds of word search
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        
        constructed_word += word_search[row][col]
        row += dy
        col += dx

    if constructed_word != word and constructed_word[::-1] != word:
        return False
    
    return True

# Finds whether the 'A' is the centre of the MAS cross
def find_words_from_centre_char(row, col):
    
    # Test the word that goes diagonally down through our 'A' is valid
    row_start = row - 1
    col_start = col - 1
    dx = 1
    dy = 1
    downward_word_is_valid = validate_word_in_direction_from_position(row_start, col_start, dx, dy)

    # Exit if it is not valid (prevent unnecessary processing of upward word)
    if not downward_word_is_valid:
        return False
    
    # Test the word that goes diagonally up through our 'A' is valid
    row_start = row + 1
    col_start = col - 1
    dx = 1
    dy = -1
    upward_word_is_valid = validate_word_in_direction_from_position(row_start, col_start, dx, dy)

    # If this is not valid, we did not find a valid MAS cross
    if not upward_word_is_valid:
        return False
    
    # Both direction are valid, we found a match!
    return True

# Get dimensions of the word search
rows, cols = len(word_search), len(word_search[0])

matches = 0

# Iterate through the word search
for row in range(rows):
    for col in range(cols):
        
        # When we find an 'A' we will check if it forms the center of the X
        if word_search[row][col] == 'A':
            
            # Increment for every match we find
            matches += find_words_from_centre_char(row, col)

print(matches)