### install the lib for mac os - pip install -U PyObjC
import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
root = Tk()
root.geometry("300x300")
inp = Entry(root)
inp.pack()


def sound1():
    a = gTTS(text=inp.get(), lang="en")
    a.save('output.mp3')
    #x = ("output.mp3")
    playsound('./output.mp3')
    #os.system("afplay" + x)


button = Button(root, text="click for sound", command=sound1)
button.pack()
root.mainloop()
