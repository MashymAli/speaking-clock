from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from time import strftime
import pyttsx3

root=tk.Tk()
root.geometry("550x350")
root.configure(bg="black")
root.title("Speaking clock")

def time():    #printing time
    current_time = strftime('%I:%M:%S %p')  #change %I to %H for 24 hr format and %p is for AM and PM
    time_label.config(text = current_time)
    time_label.after(1000, time)

def speak_time():   #speaking time
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # index 1 = female voice ,  index 0 = male voice
    engine.setProperty("rate", 200)   #set the speed of voice 
    SpeakTime = strftime('%I:%M %p')  #gives system time in hour and minute format 12 hr format
    engine.say(SpeakTime)  #actually saying the time
    engine.runAndWait()


time_label=Label(root,anchor="center",font="Stencil 65 bold",bg="black",fg="cyan")
time_label.pack(pady=10)
time()        #calling time function 

speak = Image.open("sound.png")                  #speak time button  
resize_image = speak.resize((110, 110))
speak = ImageTk.PhotoImage(resize_image)
speak_button=Button(root, image=speak,borderwidth=0,bg="black",command=speak_time,bd=0,anchor="center")
speak_button.pack(pady=60)

root.mainloop()