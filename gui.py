from tkinter import *
import time
import PIL
from PIL import ImageTk, Image
import real_time_video


window = Tk()
window.title("Stagecraft")
window.geometry('600x600')
logo = PhotoImage(file="finalcurt.gif",master=window)
w1 = Label(window, image=logo)
w1.place(relx=0.5, rely=0.5, anchor=CENTER)

def pg1(): 
    lbl= Label(window, text="Difficulty Level",borderwidth = 2,width=18)
    lbl.place(relx=0.35, rely=0.7, anchor=CENTER)
    spin = Spinbox(window, from_=0, to=100,borderwidth = 2)
    a= spin.get() # a is the value of difficulty
    spin.place(relx=0.65,rely=0.7, anchor=CENTER)
    lb2= Label(window, text="Time",borderwidth = 20)
    lb2.place(relx=0.35, rely=0.8, anchor=CENTER)
    spi = Spinbox(window, from_=0, to=100,borderwidth = 2)
    b = spi.get() # b is the value of time 
    spi.place(relx=0.65,rely=0.8, anchor=CENTER)
    a = Button(text="Click to Start",height = 3, width = 20, command=real_time_video.loops,borderwidth = 2)
    a.place(relx=0.5, rely=0.5, anchor=CENTER)
    
def pg2():
    lbl= Label(window, text="Emotion to show",borderwidth = 2)
    lbl.place(relx=0.35, rely=0.7, anchor=CENTER)
    lb3= Label(window, text="Anger",borderwidth = 2,width=22)
    lb3.place(relx=0.65, rely=0.7, anchor=CENTER)
    lb2= Label(window, text="Showing",borderwidth = 2)
    lb2.place(relx=0.35, rely=0.8, anchor=CENTER)
    lb4= Label(window, text="Anger",borderwidth = 2,width=22)
    lb4.place(relx=0.65, rely=0.8, anchor=CENTER)
    a = Button(text="Click to go back",height = 3, width = 20, command=pg1,borderwidth = 2)
    a.place(relx=0.5, rely=0.5, anchor=CENTER)
    
pg1()
window.mainloop()