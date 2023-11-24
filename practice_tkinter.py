import tkinter

def onbtnclick():
    myLabel["text"] = input.get()

window = tkinter.Tk()
window.title("Practice tkinter program")
window.minsize(width=500,height=300)

# Label
myLabel = tkinter.Label(text="I am a text",font=("Verdana",14,'normal'))
myLabel.grid(row=0,column=0)

myLabel['text']="New text"
myLabel.config(text="This is the final text and font being used",font=("Arial",14,'bold'))

# Creating button


button = tkinter.Button(text="CLICK ME",command=onbtnclick)
button.grid(row = 1,column= 1)

newbtn = tkinter.Button(text="New button")
newbtn.grid(row=0,column=2)

# Entry

input = tkinter.Entry(width= 10)
input.grid(row=2,column=3)

window.mainloop()