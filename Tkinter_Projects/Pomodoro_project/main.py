from tkinter import *
import playsound,os
import math
# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def play():
    playsound.playsound(os.path.dirname(__file__)+'\\bell.wav')
# Timer Reset

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer",fg=GREEN)
    check_marks.config(text="")
    minutes.set(0)
    seconds.set(0)
    reps = 0
# Timer Mechanism

def start_timer():  
    global reps
    reps += 1
    
    if(reps%8==0):
        label.config(text="Break",fg=RED)
        countdown(int(LONG_BREAK_MIN*60))
    elif(reps%2==0):
        label.config(text="Break",fg=PINK)
        countdown(int(SHORT_BREAK_MIN*60))
    else:
        label.config(text="Work",fg=GREEN)
        countdown(int(WORK_MIN*60))

def pause_timer():
    window.after_cancel(timer)

def resume_timer():
    global minutes,seconds,reps
    if(minutes.get()==0 and seconds.get()==0):
        start_timer()
    else:
        countdown(minutes.get()*60+seconds.get())
# Countdown Mechanism

def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    minutes.set(count_min)
    seconds.set(count_sec)
    if(count_sec<10):
        count_sec = '0' + str(count_sec)
    if(count_min<10):
        count_min = '0' + str(count_min)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,countdown,count-1)
    else:
        workdone = math.ceil(reps/2)
        check_marks.config(text="✅"*workdone)
        play()
        pause_timer()
# UI Setup

window = Tk()
window.title("My Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)

minutes = IntVar()
seconds = IntVar()
minutes.set(0)
seconds.set(0)


canvas = Canvas(width=190, height=178, bg=YELLOW, highlightthickness=0, insertbackground= YELLOW, selectbackground=YELLOW)
tomatoImg = PhotoImage(file="./Tkinter_Projects/Pomodoro_project/tomato7_new.png")
canvas.create_image(95,89,image=tomatoImg)

timer_text = canvas.create_text(95,89,text=f"0{minutes.get()}:0{seconds.get()}",fill="white",font=(FONT_NAME,30,'bold'))
canvas.grid(row=1,column=1)

label = Label(text="Timer",font=(FONT_NAME,30,'normal'),fg=GREEN, bg= YELLOW)
label.grid(row=0,column=1)

startbtn = Button(text="Start",highlightthickness=0,command=start_timer)
startbtn.grid(row=2,column=0)

resetbtn = Button(text="Reset",highlightthickness=0, command=reset_timer)
resetbtn.grid(row=2,column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,18,'normal'),pady=30)
check_marks.grid(row=4,column=1)

gridframe = Frame(window,highlightthickness=0,bg=YELLOW)

pausebtn = Button(gridframe,text="Pause",highlightthickness=0, command=pause_timer)
pausebtn.pack(padx=10,side=LEFT)
# pausebtn.grid(row=0,column=0)

resumebtn = Button(gridframe,text="Resume",highlightthickness=0, command=resume_timer)
resumebtn.pack(padx=10,side=LEFT)
# resumebtn.grid(row=0,column=1)

gridframe.grid(row=3,column=1)
window.mainloop()