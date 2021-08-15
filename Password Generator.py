from tkinter import *
from tkinter import messagebox
from myfunction import password_generator as pass_gen

def clear_item():
    passlenght_box.delete(0, END)
    password_list.delete(0,END)

def pass_generator(): 
    request_input = None
    if type(request_input) != int:
        try:
            request_input = int(passlenght_box.get())
            if request_input < 12:
                messagebox.showinfo(message="The password will be weak. Please write a number equal or bigger than 12", title="Warning!")
                clear_item()
            else:
                password = []
                password_generated = pass_gen.main(request_input)
                #print(password_generated)
                messagebox.showinfo(message="Your password was added to clipboard", title="Task done")
                password.append(password_generated)
                for i in password:
                    password_list.insert("end",i)
                    
        except ValueError:
            messagebox.showinfo(message="You wrote an invalid character. Try again", title="ValueError")
            clear_item()
    


window = Tk()
window.title("Password Generator")
window.geometry("290x270")
window.wm_iconbitmap("coffe_ghost.ico")
window.configure(background="gray")

logo = PhotoImage(file = "4.gif")
logoimage = Label(image=logo)
logoimage.place(x=140, y=60, width=130, height=130)

button1 = Button(text = "Generate", command = pass_generator)
button1.place(x=20, y=15, width=100, height=40)
button1["bg"] = "purple"
button1["fg"] = "orange"

passlenght_box = Entry(text="")
passlenght_box.place(x=140, y=20, width=130, height=25)
passlenght_box["justify"]="left"
passlenght_box.focus()

button2 = Button(text = "Clear", command = clear_item)
button2.place(x=20, y=80, width=100, height=40)
button2["bg"] = "purple"
button2["fg"] = "orange"


button3 = Button(text = "Exit", command = window.destroy)
button3.place(x=20, y=145, width=100, height=40)
button3["bg"] = "purple"
button3["fg"] = "orange"


password_list = Listbox()
password_list.place(x=20, y=210, width=250, height=40)

window.mainloop()