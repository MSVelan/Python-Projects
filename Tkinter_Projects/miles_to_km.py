import tkinter

def convert():
    thirdLabel['text'] = f'{(float(input.get())*1.609).__round__(2)}'

STYLE = ("Arial",12,'normal')
window = tkinter.Tk()
window.minsize(width=250,height=200)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

input = tkinter.Entry(width=10)
input.grid(row=0,column=1)

firstLabel = tkinter.Label(text="Miles",font=STYLE)
firstLabel.grid(row=0,column=2)
firstLabel.config(padx=10,pady=10)

secondLabel = tkinter.Label(text="is equal to",font=STYLE)
secondLabel.grid(row=1,column=0)
secondLabel.config(padx=10,pady=10)

thirdLabel = tkinter.Label(text='0',font=STYLE)
thirdLabel.grid(row=1,column=1)
thirdLabel.config(padx=10,pady=10)

fourthLabel = tkinter.Label(text="Km",font=('Arial',12,'normal'))
fourthLabel.grid(row=1,column=2)
fourthLabel.config(padx=10,pady=10)

btn = tkinter.Button(text="Calculate",command=convert)
btn.grid(row=2,column=1)
btn.config(padx=10,pady=10)

window.mainloop()