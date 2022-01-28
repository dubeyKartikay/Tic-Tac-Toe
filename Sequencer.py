from tkinter import *
from tkinter import messagebox
from Main import main

def close_window (): 
    win.destroy()

def start():
    who_won=main()
    if who_won == "":
         messagebox.showinfo("Information","It's a Tie:")
    elif who_won == "X" or who_won == "O" :
        messagebox.showinfo("Information","Player "+who_won+" won!")
    else:
        messagebox.showinfo("Information","Game Forfeited")
    button1["text"]="Play Again"
    button1.place(x=90,y=50,width=70,height=50)
win=Tk()
win.geometry("250x200")

heading = Label(win,text="Tic-Tac-Toe Game",font = "Times 20")
heading.place(x=20,y=0)
button1 = Button(win,text="Start",command = start)
button2=Button(win,text="Quit",command = close_window)
button2.place(x=90,y=130,width=70,height=50)
button1.place(x=90,y=50,width=70,height=50)

win.mainloop()
