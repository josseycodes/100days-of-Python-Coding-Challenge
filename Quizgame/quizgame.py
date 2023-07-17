class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run_quiz(self):
        for question in self.questions:
            print(question.text)
            for i, choice in enumerate(question.choices):
                print(f"{i + 1}. {choice}")
            user_answer = int(input("Enter your answer (1-4): "))
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()

        print("Quiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")


# Create questions
question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 1)
question2 = Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2)
question3 = Question("What is the largest ocean in the world?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], 1)

# Create quiz
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)

# Run the quiz
quiz.run_quiz()

