from tkinter import *
from tkinter import messagebox
import os, random, string, pyperclip, json

# Generate password

def genpassword():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    letterlist = [random.choice(letters) for i in range(nr_letters)]
    
    numberlist = [random.choice(numbers) for i in range(nr_numbers)]

    symbollist = [random.choice(symbols) for i in range(nr_symbols)]

    passwordlist = letterlist+numberlist+symbollist

    random.shuffle(passwordlist)

    genpass = ''.join(passwordlist)
    
    passwordentry.delete(0,END)
    passwordentry.insert(0,genpass)
    pyperclip.copy(genpass)


# Save password

def save():
    website = websiteentry.get()
    email = emailentry.get()
    password = passwordentry.get()
    new_data = {}
    new_data[website]={
        'email': email,
        'password': password
    }

    if(website=='' or email=='' or password==''):
        messagebox.showinfo(title="Oops",message="Fill all the details to save")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open(os.path.dirname(__file__)+"\passwords.json",'r') as f:
                    data = json.load(f)
                    data.update(new_data)
            except:
                with open(os.path.dirname(__file__)+"\passwords.json",'w') as f:
                    json.dump(new_data,f,indent=4)
            else:
                with open(os.path.dirname(__file__)+"\passwords.json",'w') as f:
                    json.dump(data,f,indent=4)
            finally:
                websiteentry.delete(0,END)
                passwordentry.delete(0,END)
                websiteentry.focus()

# Searching

def search():
    website = websiteentry.get()
    try:
        with open(os.path.dirname(__file__)+"\passwords.json",'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo("Error","No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"{website}",f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo("Error","No details for the website exists.")
            
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(window,width=256,height=256)
canvas.grid(row=0,column=1)
lockimg = PhotoImage(file=os.path.dirname(__file__)+"/lock_img.png")
canvas.create_image(128,128,image=lockimg)

websiteLabel = Label(text="Website:",font=("Courier",12,'normal'))
websiteLabel.grid(row=1,column=0)

emailLabel = Label(text="Email/Username:",font=("Courier",12,'normal'))
emailLabel.grid(row=2,column=0)

passwordLabel = Label(text="Password:",font=("Courier",12,'normal'))
passwordLabel.grid(row=3,column=0)

websiteentry = Entry(width=32)
websiteentry.grid(row=1,column=1,columnspan=1)
websiteentry.focus()

searchbtn = Button(text="Search",highlightthickness=0,padx=0,command=search, width= 17)
searchbtn.grid(row=1,column=2)

emailentry = Entry(width=49)
emailentry.grid(row=2,column=1,columnspan=2)
emailentry.insert(0,"muthiahsvn@gmail.com")

passwordentry = Entry(width=32)
passwordentry.grid(row=3,column=1)

genPasswordBtn = Button(text="Generate Password",highlightthickness=0,padx=0,command=genpassword)
genPasswordBtn.grid(row=3,column=2)

addBtn = Button(text="Add",highlightthickness=0,width=49,command=save)
addBtn.grid(row=4,column=1,columnspan=2)

window.mainloop()
