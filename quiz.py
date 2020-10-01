"""
quiz.py

A multi-choice quiz with randomly-ordered questions, and randomly-ordered
answers for each question.
"""
import random

class QuizQuestion:
    """Class representing each multi-choice question in the quiz"""
    def __init__(self, question, answers, correctAnswerIndex):
        """Constructor. The answers should be a list of potential answers for the
        multi-choice question. The correct answer is indicated as the index (zero
        based) of the correct answer within the list."""
        self.question = question
        self.answers = answers
        # Store the correct answer so it can be found again after shuffling
        correctAnswer = answers[correctAnswerIndex]
        random.shuffle(self.answers)
        self.correctAnswerIndex = self.answers.index(correctAnswer)

    def askQuestion(self):
        """Prints out the question and each potential answer"""
        print("Q.",self.question)
        for i in range(len(self.answers)):
            print(str(i+1) + ") " + self.answers[i])

    def checkAnswer(self, answerNum):
        """Returns a boolean indicating if the answer with that number (1-indexed) is correct""" 
        answerIndex = answerNum - 1
        return answerIndex == self.correctAnswerIndex

    def correctAnswerNum(self):
        """Returns the number (1-indexed) of the correct answer"""
        return self.correctAnswerIndex+1

class Quiz:
    """Class representing the quiz itself"""
    def __init__(self, quizQuestions):
        """Constructor. Parameter quizQuestions is a ist of QuizQuestion objects."""
        self.quizQuestions = quizQuestions
        random.shuffle(self.quizQuestions)
        self.score = 0

    def getFinalScore(self):
        """Returns the score, out of the total, as a string"""
        return str(self.score) + "/" + str(len(self.quizQuestions))

    def getFinalComment(self):
        """Returns a comment based on the score"""
        scorePrecent = self.score / len(self.quizQuestions) * 100
        if scorePrecent >= 90:
            return "Excellent!"
        elif scorePrecent >= 50:
            return "Well done."
        else:
            return "Better luck next time."

    def run(self):
        """Runs the quiz, presenting question, checking answers, and giving the
        final score and comment"""
        print("Here are your questions. Provide the number of the answer you think is correct.")
        for quizQuestion in self.quizQuestions:
            print("-"*20) # A line to separate each quiz question
            quizQuestion.askQuestion()
            userAnswer = int(input("> "))
            isCorrect = quizQuestion.checkAnswer(userAnswer)
            if isCorrect:
                print("Correct!")
                self.score = self.score+1
            else:
                print("Sorry, the correct answer was", quizQuestion.correctAnswerNum())
        print("="*20) # A line to separate the score from the quiz questions
        print("Your score:", self.getFinalScore())
        print(self.getFinalComment())

# Set up a quiz with a few questions
quiz = Quiz([
    QuizQuestion(
        "What is the chemical symbol for Boron?",
        ["Bo", "B", "N", "Bn"],
        1
    ),
    QuizQuestion(
        "When was Issac Newton born?",
        ["1642", "1644", "1666", "1701"],
        0
    ),
    QuizQuestion(
        "What is the meaning of the word 'xebec'?",
        [   "ill-tempered woman",
            "small tropical rainforest bird",
            "engraving design on wood with hot poker",
            "a small three-masted pirate ship"
        ],
        3
    ),
    QuizQuestion(
        "What is the formula to find the surface area of a sphere with radius 'r'?",
        [
            "4 * π * r^2",
            "(4/3) * π * r^2",
            "(4/3) * π * r^3",
            "3 * π * r^2"
        ],
        0
    )
])

# Run the quiz
quiz.run()


        
