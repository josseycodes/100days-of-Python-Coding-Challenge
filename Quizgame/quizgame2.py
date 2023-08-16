questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "Berlin", "London", "Rome"],
        "answer": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is the largest ocean in the world?",
        "choices": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": 0
    }
]

score = 0

def ask_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == question["answer"]:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def run_quiz():
    global score
    for question in questions:
        score += ask_question(question)
        print()
    
    print("Quiz completed!")
    print(f"Your score: {score}/{len(questions)}")

# Run the quiz
run_quiz()

