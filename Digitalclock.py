import tkinter as tk
import time

def clock():
    current=time.strftime("%H:%M:%S")
    label1["text"]=current
    root.after(1000,clock)

def date():
    current1=time.strftime("%A, %B %d, %Y")
    label2["text"]=current1
    root.after(1000,clock)
   

root=tk.Tk()
root.title("Digital Clock")
label1=tk.Label(root,font="article 28",bg="black",fg="red")
label1.grid(row=0,column=0)
clock()
label2=tk.Label(root,font="article 28",bg="black",fg="red")
label2.grid(row=1,column=0)
date()
root.mainloop()
f = open("Digital clock.txt", "r")
print(f.readable())
import os
os.mkdir("C:\Digital clock")
