def reverse_string(input_string):
    return input_string[::-1]

def count_occurrences(input_string, character):
    return input_string.count(character)

def is_palindrome(input_string):
    reversed_string = reverse_string(input_string)
    return input_string == reversed_string

def remove_duplicates(input_string):
    return ''.join(set(input_string))

def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

# Main program
user_input = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)

# Count occurrences of a specific character
character = input("Enter a character to count its occurrences: ")
occurrences = count_occurrences(user_input, character)
print("Occurrences of", character + ":", occurrences)

# Check if the string is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Remove duplicates from the string
removed_duplicates = remove_duplicates(user_input)
print("String with duplicates removed:", removed_duplicates)

# Capitalize each word in the string
capitalized_words = capitalize_words(user_input)
print("String with capitalized words:", capitalized_words)

