import string
from collections import Counter

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        # Read the file content
        content = file.read()

        # Remove punctuation and convert to lowercase
        content = content.translate(str.maketrans('', '', string.punctuation)).lower()

        # Calculate word count
        words = content.split()
        word_count = len(words)

        # Calculate character count
        character_count = len(content)

        # Calculate most common words
        word_frequency = Counter(words)
        most_common_words = word_frequency.most_common(5)  # Change the number to display more or fewer common words

        # Display the results
        print(f"Word Count: {word_count}")
        print(f"Character Count: {character_count}")
        print("Most Common Words:")
        for word, count in most_common_words:
            print(f"{word}: {count}")

# Provide the file path
file_path = 'example.txt'  # Replace 'example.txt' with the path to your text file
analyze_file(file_path)

