from random import choice
from tkinter import *
import textwrap

sentences_file = open("text.txt", 'r')
sentences = sentences_file.read().splitlines()
sentences_file.close()
timer = None
start=True
to_type = ''

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
    timer_tag.config(text=f"{m}".zfill(1) + ":" + f"{s}".zfill(2))
    timer = window.after(1000, timer_count, m, s+1)


timer_tag = Label(text="0:00", font=("Arial", 13, "bold"))
timer_tag.pack()

typing_box = Text(height=8, width=80, font=("Arial", 12))
typing_box.focus()
typing_box.pack()


def wpm(timer):
    splt = timer.split(':')
    print(float(len(to_type.split(' '))))
    print(60.0*float(splt[0]) + float(splt[1]))
    return ((60.0*float(len(to_type.split(' '))))/(60.0*float(splt[0]) + float(splt[1])))


def start_timer():
    global start, to_type
    if start:
        to_type = choice(sentences)
        paragraph.config(text=textwrap.fill(to_type, width=80))
        start_button.config(text="Stop")
        timer_count(0, 0)
        start = False
    else:
        start_button.config(text="Start")
        window.after_cancel(timer)
        if typing_box.get("1.0", END)[:-1] == to_type:
            timer_tag.config(text=f"Congrats!\nYour time is {timer_tag.cget('text')}\n Your WPM is {wpm(timer_tag.cget('text'))}")
        else:
            timer_tag.config(text=f"You failed!\nYour time is {timer_tag.cget('text')}")
        start = True


start_button = Button(text="Start", command=start_timer)
start_button.pack()

window.mainloop()