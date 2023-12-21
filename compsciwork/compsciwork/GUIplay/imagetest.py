from tkinter import *
import tkinter as tk
window = tk.Tk()

bgimg= tk.PhotoImage(file="../adventuregame/forestbg.ppm")

bg = Label(window, i=bgimg)
title = tk.Label(window, text="Welcome to Adventure™!", fg="#b82323", bg="#21195c", font=("Old English Text MT", 90))
text1 = tk.Label(window, text="Hit the start button to begin your Adventure™!", fg="#b82323", bg="#21195c", font=("Old English Text MT", 45))
enterbutton = tk.Button(window, text="Start", fg="#b82323", bg="#21195c", font=("Old English Text MT", 90), command=e.newEnemies(7))



bg.pack()
window.mainloop()