from tkinter import *
from quizBrain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quizbrain: QuizBrain):
        self.userAns = 'None'
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.scoreLabel = Label(text=f"Score: {self.quiz.score}",font=("Arial",12,'normal'),fg="white",bg=THEME_COLOR)
        self.scoreLabel.grid(row=0,column=1)

        self.canvas = Canvas(width=400,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.text = self.canvas.create_text(200,100,text="Question",font=("Arial",14,'italic'),fill=THEME_COLOR,width=380)
        
        tickImg = PhotoImage(file="./API/Quiz_OpenTriviaDB_API/Images/right.png")
        self.tickbtn = Button(image=tickImg,highlightthickness=0,bd=0,command=self.truePressed)
        self.tickbtn.grid(row=2,column=1)

        wrongImg = PhotoImage(file="./API/Quiz_OpenTriviaDB_API/Images/wrong.png")
        self.wrongbtn = Button(image=wrongImg,highlightthickness=0,bd=0,command=self.falsePressed)
        self.wrongbtn.grid(row=2,column=0)

        self.getNextQn()
        self.window.mainloop()
    
    def truePressed(self):
        isCrt = self.quiz.checkans("True")
        self.giveFeedback(isCrt)

    def falsePressed(self):
        isCrt = self.quiz.checkans("False")
        self.giveFeedback(isCrt)

    def getNextQn(self):
        self.canvas.config(bg="white")
        self.scoreLabel.config(text=f"Score: {self.quiz.score}")
        if(self.quiz.stillHasQuestion()):
            nxtQn = self.quiz.nextQn()
            self.canvas.itemconfig(self.text,text=nxtQn)
        else:
            self.canvas.itemconfig(self.text,text="You have reached the end of the quiz.")
            self.tickbtn.config(state="disabled")
            self.wrongbtn.config(state="disabled")
            self.tickbtn.grid_forget()
            self.wrongbtn.grid_forget()
    
    def giveFeedback(self,isCrt):
        if(isCrt):
            self.canvas.config(bg="green")
            self.window.after(1000,self.getNextQn)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.getNextQn)
    