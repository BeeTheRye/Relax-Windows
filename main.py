#This is a GUI program I've created to give relaxing options to a user
from email.mime import image
from tkinter import *
from random import choice
from turtle import update
import webbrowser
import random
import time
from anyio import current_time
window = Tk()
window.geometry("695x900")
window.title("Ready to chill?")
window.config(background="#027eab")
window.resizable(False,False)
photo =  PhotoImage(file='C:\\Users\\brian\\Desktop\\code\\Python\\RelaxWindows\\legologo.png')
photo2 = PhotoImage(file='C:\\Users\\brian\\Desktop\\code\\Python\\RelaxWindows\\LOGO.png')
relaxingurloptions = [
    'https://www.youtube.com/watch?v=2IqAr_Uyg8M',
    'https://www.youtube.com/watch?v=CdMUOsf2QNc',
    'https://www.youtube.com/watch?v=MugU4Rzg3rk',
    'https://www.youtube.com/watch?v=ArkLSz-It0s&t=192s',
    'https://www.youtube.com/watch?v=_nbyBJESxTM&t=409s',
    'https://www.youtube.com/watch?v=FR3i0qKzRvg',
    'https://www.youtube.com/watch?v=5qap5aO4i9A',    
]

def clockstart():
   clocktime = time.strftime("%H:%M:%S")
   timer2.config(text=clocktime)
   
   
def clockupdate():
   clocktime = time.strftime("%H:%M:%S")
   timer.config(text=clocktime)
   timer.after(1000, clockupdate)
    

def relaxurl():
    global realrandom
    print (webbrowser.open((random.choice(relaxingurloptions))))
    
def relaxbutton2():
    global timer
    global timer2
    window2 = Toplevel(window)
    window2.geometry('695x900')
    window2.resizable(False,False)
    window2.title('Snack Break!')
    
    timer = Label(window2,
                  text="",
                  font=("Comic Sans", 50),
                  bg="green",)
    
    message = Label(window2,
                    text = "see you in 15! \n Below is the time you went on break \n and above is the current time",
                    font =("comic sans", 25),
                    )
    timer2 = Label(window2,
                  text="",
                  font=("Comic Sans", 50),
                  bg="green",)
   
    timer.pack(pady=20)
    message.pack(pady=20) 
    timer2.pack(pady=20)
    clockupdate()
    clockstart()
      
relaxoptions = [relaxurl, relaxbutton2]   
label = Label(window,
              text="Welcome to Relaxation",
              font=('Arial',40,'bold'),
              fg = 'green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=50,
              pady=20,
              compound='bottom'
              ).grid(row= 0,sticky='e')

RelaxButton = Button(window,
                     font=('Arial',20,'bold'),
                     fg = 'green',
                     bg='black',
                     relief=RAISED,
                     bd=10,
                     padx=10,
                     pady=10,
                     text = 'Relaxing Videos',
                     command = relaxurl
                     ).grid(row=6)
             

RelaxButton2 = Button(window,
                     font=('Arial',20,'bold'),
                     fg = 'green',
                     bg='black',
                     relief=RAISED,
                     bd=10,
                     padx=10,
                     pady=10,
                     text = 'Snack',
                     command =relaxbutton2,
                     ).grid(row=7)


QuitButton = Button(window,
                   text = 'Quit',
                   font=('Arial',20,'bold'),
                   fg = 'green',
                   bg='black',
                   relief=RAISED,
                   bd=10,
                   padx=10,
                   pady=10,
                   command = window.destroy).grid(row=9)
                   
window.mainloop()

    