import html
class QuizBrain:
    def __init__(self,qnList):
        self.questionNumber = 0
        self.questionList = qnList
        self.score = 0

    def nextQn(self):
        self.currentQn = self.questionList[self.questionNumber]
        self.questionNumber += 1
        return "Q.{}: {} (True/False)?: ".format(self.questionNumber,html.unescape(self.currentQn.text))
        # userAns = input("Q.{}: {} (True/False)?: ".format(self.questionNumber,html.unescape(currentQn.text)))
        # self.checkans(currentQn,userAns)

        
    def stillHasQuestion(self):
        return self.questionNumber<len(self.questionList)
    
    def checkans(self,ans):
        if ans.lower()==self.currentQn.answer.lower():
            self.score+=1
            return True
        else:
            return False