#Digital clock
""" 
from time import strftime
Tkinter library
"""

from time import strftime
from tkinter import Label, Tk

#Label: it will simply specify the container box for text,image etc
window=Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="black")
window.resizable(False,False)

clock_label=Label(window, bg="black", fg="white", font= ("Times",30, 'bold'), relief='flat')
clock_label.place(x=20,y=20)

def updatinglabel():
    current_time=strftime("%H: %M: %S")
    clock_label.configure(text=current_time)
    clock_label.after(80,updatinglabel)

updatinglabel()
window.mainloop() 