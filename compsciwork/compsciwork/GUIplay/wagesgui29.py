import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Wage Calculator")
#window.geometry("400x250")
window.configure(background = "lightblue")

def WagesCalc():
    while True:
        try:
            TeddyNum = int(TeddyNumEnt.get())
            HoursNum = int(HoursNumEnt.get())
            break
        except ValueError:
            tk.messagebox.showerror("Error Message", "You must enter a number!")
            TeddyNumEnt.delete(0, tk.END)
            HoursNumEnt.delete(0, tk.END)
            break
    
    TeddyWage = TeddyNum*2
    HoursWage = HoursNum*5
    if TeddyWage >= HoursWage:
        tk.messagebox.showinfo("Wages", f"The wages for this employee are: £{TeddyWage}")
    else:
        tk.messagebox.showinfo("Wages", f"The wages for this employee are: £{HoursWage}")
    TeddyNumEnt.delete(0, tk.END)
    HoursNumEnt.delete(0, tk.END)


title=tk.Label(window, text="Welcome to the Teddy Factory Wage Calculator", fg="black", bg="lightblue", font=("Arial", 15))
textTed=tk.Label(window, text="\nEnter the number of Teddy Bears™ you have made this shift: ", fg="black", bg="lightblue", font=("Arial", 15))
pad1=tk.Frame(window, width=10, height=30, bg="lightblue")
TeddyNumEnt=tk.Entry(window, fg="black", bg="white", width=10, font=("Arial", 15))
pad2=tk.Frame(window, width=10, height=30, bg="lightblue")
textHour=tk.Label(window, text="\nEnter the number of Hours you have worked this shift: ", fg="black", bg="lightblue", font=("Arial", 15))
pad3=tk.Frame(window, width=10, height=30, bg="lightblue")
HoursNumEnt=tk.Entry(window, fg="black", bg="white", width=10, font=("Arial", 15))
pad4=tk.Frame(window, width=10, height=30, bg="lightblue")
enterbutton=tk.Button(window, text="Enter", fg="black", bg="navajo white", height=1, width=20, font=("Arial", 20), command=WagesCalc)
pad5=tk.Frame(window, width=10, height=30, bg="lightblue")

title.pack()
textTed.pack()
pad1.pack(fill=tk.X)
TeddyNumEnt.pack()
pad2.pack(fill=tk.X)
textHour.pack()
pad3.pack(fill=tk.X)
HoursNumEnt.pack()
pad4.pack(fill=tk.X)
enterbutton.pack()
pad5.pack(fill=tk.X)
window.mainloop()