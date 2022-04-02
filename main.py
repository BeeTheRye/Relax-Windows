#take a momment to breath
#goal of this program is to interupt the user at their workstation every few others to remind them to breath.
#it will be a small non-invasive window that should have some text and a gif/video of some sort associated with it.
#Hopefully having the text fade in over something a nice mountain view or ocean view

from email.mime import image
from tkinter import *
from random import choice
import webbrowser
import random


window = Tk()
window.geometry("1105x700")
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

def relaxurl():
    global realrandom
    window.quit()
    print (webbrowser.open((random.choice(relaxingurloptions))))
    
def relaxbutton2():
    window.quit()
    print("test2")
    
def relaxbutton3():
    window.quit()
    print("test3")
     
relaxoptions = [relaxurl, relaxbutton2, relaxbutton3]

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
              ).grid(column=3)

MainPhoto = Label(window,
              text="Welcome to Relaxation",
              image=photo2).grid(row=2, column=3)

RelaxButton = Button(window,
                     font=('Arial',40,'bold'),
                     fg = 'green',
                     bg='black',
                     relief=RAISED,
                     bd=10,
                     padx=10,
                     pady=10,
                     text = 'Relax',
                     #command = realrandom.choice(relaxoptions),
                     command = relaxurl
                     ).grid(row=4, column=2)

QuitButton = Button(window,
                   text = 'Quit',
                   font=('Arial',40,'bold'),
                   fg = 'green',
                   bg='black',
                   relief=RAISED,
                   bd=10,
                   padx=10,
                   pady=10,
                   command = window.destroy).grid(row=4, column=4)
                   
window.mainloop()

    