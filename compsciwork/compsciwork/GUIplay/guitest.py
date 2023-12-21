import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("First GUI Test")
window.geometry("400x250")
window.configure(background = "lightblue")

def Multiply():
    usernum1 = int(num1ent.get())
    usernum2 = int(num2ent.get())
    tk.messagebox.showinfo("Multiplied", f"Your two numbers multiplied together is: {usernum1*usernum2}")


title=tk.Label(window, text="Welcome to my first gui!", fg="black", bg="lightblue", font=("Arial", 15))
text1=tk.Label(window, text="\nEnter 2 numbers to multiply together: ", fg="black", bg="lightblue", font=("Arial", 15))
pad1=tk.Frame(window, width=10, height=30, bg="lightblue")
num1ent=tk.Entry(window, text="Num1", fg="black", bg="white", width=6, font=("Arial", 15))
pad2=tk.Frame(window, width=10, height=30, bg="lightblue")
num2ent=tk.Entry(window, fg="black", bg="white", width=6, font=("Arial", 15))
pad3=tk.Frame(window, width=10, height=30, bg="lightblue")
enterbutton=tk.Button(window, text="Multiply", fg="black", bg="navajo white", command=Multiply)


title.pack()
text1.pack()
pad1.pack(fill=tk.X)
num1ent.pack()
pad2.pack(fill=tk.X)
num2ent.pack()
pad3.pack(fill=tk.X)
enterbutton.pack()
window.mainloop()