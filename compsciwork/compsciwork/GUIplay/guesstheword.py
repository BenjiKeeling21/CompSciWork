import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

window = tk.Tk()
window.title("Guess The Word")
window.geometry("400x300")
window.configure(background = "lightblue")

global guessnum
guessnum = 0

def importWords():
    wordlist = []
    wordfile = open("words.csv","r")
    for row in wordfile:
        wordlist.append(row)
    wordfile.close()
    for i, s in enumerate(wordlist):
        wordlist[i] = s.rstrip(s[-1])
    return(wordlist)

answer = random.choice(importWords())

def CheckWord():
    global guessnum
    word = wordEnt.get()
    guessnum = guessnum+1
    if word.lower() == answer:
        print("correct")
        tk.messagebox.showinfo("Congratulations!", f"You win!\nThe word was {answer}")
    else:
        if guessnum == 1:
            tk.messagebox.showinfo("Incorrect!", f"Hint:\nThe first letter is: {answer[0]}")
            wordEnt.delete(0, tk.END)
        elif guessnum == 3:
            tk.messagebox.showinfo("Incorrect!", f"Hint:\nThe last letter is: {answer[len(answer)-1]}")
            wordEnt.delete(0, tk.END)
        elif guessnum == 5:
            tk.messagebox.showinfo("Incorrect!", f"You Lose :( ")
            tk.messagebox.showinfo("Answer", f"You lost!\nThe word was {answer}")
            window.destroy()
        else:
            tk.messagebox.showinfo("Incorrect!", f"Try again!")
            wordEnt.delete(0, tk.END)

answer = random.choice(importWords())
hint = ""

for i in answer:
   hint = hint+"_ "

print(answer)
print(hint)

title=tk.Label(window, text="Welcome to guess my word!", fg="black", bg="lightblue", font=("Arial", 15))
text1=tk.Label(window, text="\nEnter your guess: ", fg="black", bg="lightblue", font=("Arial", 15))
pad1=tk.Frame(window, width=10, height=30, bg="lightblue")
wordEnt=tk.Entry(window, fg="black", bg="white", width=len(answer), font=("Arial", 15))
pad2=tk.Frame(window, width=10, height=30, bg="lightblue")
wordHint=tk.Label(window, fg="black", text=f"\n{hint}", bg="lightblue", font=("Arial", 15))
pad3=tk.Frame(window, width=10, height=30, bg="lightblue")
enterbutton=tk.Button(window, text="Check", fg="black", bg="navajo white", command=CheckWord)


title.pack()
text1.pack()
pad1.pack(fill=tk.X)
wordEnt.pack()
pad2.pack(fill=tk.X)
wordHint.pack()
pad3.pack(fill=tk.X)
enterbutton.pack()
window.mainloop()