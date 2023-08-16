In this program, the Question class represents a single quiz question. It has attributes for the question text, a list of choices, and the correct answer. The check_answer() method checks if the user's answer matches the correct answer.

The Quiz class manages a collection of questions and keeps track of the user's score. It has methods to add questions to the quiz and run the quiz. The run_quiz() method iterates through each question, presents it to the user along with the choices, prompts for an answer, checks if the answer is correct, and updates the score accordingly.

To use the program, you can create instances of the Question class with the appropriate question text, choices, and correct answer. Then, create an instance of the Quiz class, add the questions to the quiz, and finally, run the quiz using the run_quiz() method.

You can expand upon this program by adding more questions, implementing a leaderboard to track high scores, or incorporating additional features to enhance the user experience


In the alternative approach in the second python file, the questions are stored as a list of dictionaries. Each dictionary represents a question and contains the question text, choices, and the index of the correct answer.

The ask_question() function takes a question dictionary, displays the question and choices, prompts for the user's answer, checks if it matches the correct answer, and returns 1 for a correct answer or 0 for an incorrect answer.

The run_quiz() function iterates through each question, calls the ask_question() function for each question, updates the score accordingly, and displays the final score at the end.

The overall structure of the program is similar to the previous approach, but the implementation details are slightly different. Feel free to choose the approach that you find most suitable for your needs.


