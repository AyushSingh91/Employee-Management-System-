from customtkinter import *
from PIL import Image
# from tkinter import callback
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='admin' and passwordEntry.get()=='12345':
        messagebox.showinfo('Success','Login successfully')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong credentials')

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('cover.png'), size=(630,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employ Managment System',font=('Goudy old style',20,'bold'),text_color='dark blue')
headinglabel.place(x=650,y=100)

usernameEntry= CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=670,y=150)

passwordEntry= CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.place(x=670,y=200)

loginbutton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginbutton.place(x=690,y=250)

root.mainloop()
