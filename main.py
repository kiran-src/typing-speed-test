from random import choice
from tkinter import *
import textwrap

sentences_file = open("sentences.txt", 'r')
sentences = sentences_file.read().splitlines()
sentences_file.close()
timer = None
start=True

# Creating a new window and configurations
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=300)
window.config(padx=10, pady=10, bg="#f7f5dd")  # Add padding to the edges of window

paragraph = Label(text="Start the test to view the sentence to type", font=("Arial", 12))
paragraph.pack()


def timer_count(m, s):
    global timer
    if s == 60:
        s = 0
        m += 1
    timer_tag.config(text=f"{m}:{s}")
    timer = window.after(1000, timer_count, m, s+1)


timer_tag = Label(text="0:00", font=("Arial", 13, "bold"))
timer_tag.pack()

typing_box = Text(height=8, width=80, font=("Arial", 12))
typing_box.focus()
typed = typing_box.get("1.0", END)
typing_box.pack()


def start_timer():
    global start
    if start:
        paragraph.config(text=textwrap.fill(choice(sentences), width=80))
        start_button.config(text="Stop")
        timer_count(0, 0)
        start = False
    else:
        start_button.config(text="Start")
        window.after_cancel(timer)
        timer_tag.config(text=f"Congrats!\nYour time is {timer_tag.cget('text')}")
        start = True


start_button = Button(text="Start", command=start_timer)
start_button.pack()

window.mainloop()