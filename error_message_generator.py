import tkinter as tk
from tkinter import messagebox
import random
import pyautogui as pp
import time

canvas = tk.Canvas(width=500, height=500)
canvas.pack()

canvas.winfo_toplevel().title("error message generator")

entry = tk.Entry()
canvas.create_window(250, 250, window=entry)

titles = [
    "onionsonline.com",
    "python error",
    "memes",
    "die",
    "p!warn @charliecowboyee",
    "title",
    "javascript error",
    "useless software",
    "coming up with titels is hard",
    "message from the SCP Foundation",
    "message from Supreme Leader Jimi",
    "message from Big Chungus",
    "message from Noam",
    "error",
]

messages = [
    "i made this in about 78 lines of code",
    "desktop goose is coming for you",
    "404 error error_message_generator.py does not exist",
    "i don't understand why you would want to use this",
    "why did i make this?",
    "matan does not exist, any evidence that proves matan exists is to be destroyed and replaced with evidence that proves he dosen't exist",
    "all hail big chungus",
    "stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software stupid software",
    "this is a utility that makes you see random errors for no reason",
    "if you accidentally made this send too many errors that just force quit the software (or task manager)",
    "message",
    "by order of the Administrator and the 05 Council using this software is grounds for termination",
    "it was kind of fun to make tho",
    "why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? why? ",
    "hELp@#%^%^&%#!@##$%^$^&$^& fdg 4#@%%^# $FGW E RFGT%ERT@!#$@T RGDs",
    "error",
    "if you have anymore title or message suggestions plz dm me on discord",
]


def errorz():
    value = entry.get()
    cvalue = int(value)
    count = 0

    while count < cvalue:
        messagebox.showerror(random.choice(titles), random.choice(messages))
        count = count + 1

def errorsound():
    count = 0
    while count < 100:
        if count < 100:
            messagebox.showerror("sound", "its time for error noises!!!!")
            pp.press('enter')
            time.sleep(1)
        count = count + 1

def quitty():
    count = 0
    while count < 20:
        if count < 20:
            messagebox.showerror("why?", "why do you leave? i am lonely...")
            pp.press('enter')
            time.sleep(1)
        count = count + 1
    quit()

def mousetp():
    count = 0
    mos = mouseentry.get()
    mosi = int(mos)
    while count < mosi:
        if count < mosi:
            pp.moveTo(random.randrange(0, 1920), random.randrange(0, 1080))
            time.sleep(0.25)
        count += 1

mouseentry = tk.Entry()
canvas.create_window(250, 370, window=mouseentry)


button = tk.Button(text="get some errors (why would you want this???)", bg='pink', fg='black', activebackground="blue", activeforeground="white", command=errorz)
canvas.create_window(250, 290, window=button)

button1 = tk.Button(text="time for error noises", bg='pink', fg='black', activebackground="blue", activeforeground="white", command=errorsound)
canvas.create_window(250, 330, window=button1)

quittybutton = tk.Button(text="quit the software", bg='#630101', fg='white', activebackground="blue", activeforeground="white", command=quitty)
canvas.create_window(445, 490, window=quittybutton)

mousetpbutt = tk.Button(text="teleport your mouse!", bg='pink', fg='black', activebackground="blue", activeforeground="white", command=mousetp)
canvas.create_window(250, 410, window=mousetpbutt)

canvas.mainloop()