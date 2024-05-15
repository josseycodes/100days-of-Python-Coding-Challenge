import json
import os

# Sample data embedded directly in the script
vocabulary_data = [
    {"word": "apple", "translation": "manzana", "pronunciation": "mænˈzænə"},
    {"word": "book", "translation": "libro", "pronunciation": "ˈliːbroʊ"},
    {"word": "house", "translation": "casa", "pronunciation": "ˈkæsə"}
]

quizzes_data = [
    {
        "question": "What is the translation of 'apple'?",
        "options": ["manzana", "libro", "casa"],
        "answer": "manzana"
    },
    {
        "question": "What is the translation of 'book'?",
        "options": ["manzana", "libro", "casa"],
        "answer": "libro"
    }
]

progress_data = {
    "username": "user",
    "vocab_progress": {},
    "quiz_progress": {}
}

# Utility functions
def load_data(data):
    return data

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def update_progress(progress, key, value):
    progress[key] = value
    save_data('progress.json', progress)

# Load data
vocabulary = load_data(vocabulary_data)
quizzes = load_data(quizzes_data)
progress = load_data(progress_data)

# Main functionality
def show_menu():
    print("Language Learning App")
    print("1. Vocabulary Exercise")
    print("2. Take Quiz")
    print("3. Flashcards")
    print("4. View Progress")
    print("5. Exit")

def vocabulary_exercise():
    for entry in vocabulary:
        word = entry['word']
        translation = entry['translation']
        pronunciation = entry['pronunciation']
        print(f"Word: {word} - Translation: {translation} - Pronunciation: {pronunciation}")
        input("Press Enter to continue...")

def take_quiz():
    score = 0
    for quiz in quizzes:
        question = quiz['question']
        options = quiz['options']
        answer = quiz['answer']
        print(question)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        user_answer = int(input("Your answer: ")) - 1
        if options[user_answer] == answer:
            score += 1
    progress['quiz_progress'] = score
    update_progress(progress, 'quiz_progress', score)
    print(f"Your score: {score}/{len(quizzes)}")

def flashcards():
    for entry in vocabulary:
        word = entry['word']
        translation = entry['translation']
        pronunciation = entry['pronunciation']
        print(f"Word: {word}")
        input("Press Enter to reveal translation...")
        print(f"Translation: {translation} - Pronunciation: {pronunciation}")
        input("Press Enter to continue...")

def view_progress():
    print("Your Progress:")
    print(f"Vocabulary progress: {progress.get('vocab_progress', 'No progress yet')}")
    print(f"Quiz progress: {progress.get('quiz_progress', 'No progress yet')}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            vocabulary_exercise()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            flashcards()
        elif choice == '4':
            view_progress()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
