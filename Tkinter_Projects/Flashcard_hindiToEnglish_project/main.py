from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#9bdeac"
ele = {}
datalist = {}
# Reading from csv

def knew():
    datalist.remove(ele)
    dfTowrite = pandas.DataFrame(datalist)
    dfTowrite.to_csv('.\data\words_to_learn.csv',index=False)
    next_card()

def next_card():
    global ele,timer,datalist
    window.after_cancel(timer)
    try:
        df = pandas.read_csv('.\data\words_to_learn.csv')
    except FileNotFoundError:
        df = pandas.read_csv('.\data\commonWords.csv')
    datalist = df.to_dict(orient="records")
    ele = random.choice(datalist)
    hword = ele['Hindi']
    canvas.itemconfig(image,image=frontCardImg)
    canvas.itemconfig(title,fill="black",text="Hindi")
    canvas.itemconfig(word,fill="black",text=hword)
    timer = window.after(5000,func=translation)
    
def translation():
    eword = ele['English']
    canvas.itemconfig(image,image=backCardImg)
    canvas.itemconfig(title,fill="white",text="English")
    canvas.itemconfig(word,fill="white",text=eword)
    

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer = window.after(5000,func=translation)

canvas = Canvas(width=866,height=610,bg=BACKGROUND_COLOR,highlightthickness=0)
frontCardImg = PhotoImage(file="./images/flashCard_front2.png")
backCardImg = PhotoImage(file="./images/flashCard_back.png")

image = canvas.create_image(433,305,image=frontCardImg)
canvas.grid(row=0,column=0,columnspan=2)

title = canvas.create_text(433,180,text="Title",font=('Arial',22,'italic'))
word = canvas.create_text(433,280,text="word",font=("Arial",35,'bold'))
rightImg = PhotoImage(file="./images/right.png")

tickbtn = Button(image=rightImg,highlightthickness=0,command=knew)
tickbtn.grid(row=1,column=1)

wrongImg = PhotoImage(file="./images/wrong.png")
wrongbtn = Button(image=wrongImg,highlightthickness=0,command=next_card)
wrongbtn.grid(row=1,column=0)

next_card()

window.mainloop()