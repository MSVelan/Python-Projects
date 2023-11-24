# import requests, html
from ui import QuizInterface
from questionModel import Question
from data import questionData
from quizBrain import QuizBrain

questionBank = [Question(i['question'],i['correct_answer']) for i in questionData]
quiz = QuizBrain(questionBank)

quizUI = QuizInterface(quiz)
