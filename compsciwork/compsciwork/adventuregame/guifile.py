import tkinter as tk
from tkinter import messagebox
from tkinter import *
import player as p
import enemy as e
import rooms as r

window = tk.Tk()
window.title("Adventure")
window.geometry("1400x700")


bgimg= tk.PhotoImage(file="forestbg.ppm")

bg = Label(window, i=bgimg)
title = tk.Label(window, text="Welcome to Adventure™!", fg="#b82323", bg="#21195c", font=("Old English Text MT", 90))
text1 = tk.Label(window, text="Hit the start button to begin your Adventure™!", fg="#b82323", bg="#21195c", font=("Old English Text MT", 45))
enterbutton = tk.Button(window, text="Start", fg="#b82323", bg="#21195c", font=("Old English Text MT", 90), command=e.newEnemies(7))



bg.pack(fill=tk.X)
title.pack()
text1.pack()
enterbutton.pack()
window.mainloop()