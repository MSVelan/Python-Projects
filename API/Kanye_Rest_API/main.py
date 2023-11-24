from tkinter import *
import os.path as r, requests

def displayquote():
    data = requests.get(url="https://api.kanye.rest/")
    data.raise_for_status()
    quote = data.json()["quote"]
    canvas.itemconfig(toChange,text=quote)


window = Tk()
window.title("Kanye quotes using API")
window.config(padx=50,pady=50)

canvas = Canvas(width=600,height=402)
kanyeFaceImg = PhotoImage(file=r.dirname(__file__)+"/images/kanyeImg2.png")
frameImg = PhotoImage(file=r.dirname(__file__)+"/images/Frame1.png")
canvas.create_image(300,201,image=frameImg)
canvas.grid(row=0,column=0)
toChange = canvas.create_text(300,181,text="Hello this is a very long text just for checking purpose",font=("Arial",18,"bold"),width=450,fill="white")

clickbtn = Button(image=kanyeFaceImg,highlightthickness=0,command=displayquote)
clickbtn.grid(row=1,column=0)

displayquote()
window.mainloop()