from random import choice
from tkinter import *

sentences_file = open("sentences.txt", 'r')
sentences = sentences_file.read().splitlines()
sentences_file.close()

# Creating a new window and configurations
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10, bg="#f7f5dd")  # Add padding to the edges of window

paragraph = Label(text="Start the test to view the sentence to type", font=("Arial", 12, "bold"))
paragraph.pack()

timer_tag = Label(text="0:00", font=("Arial", 10))
timer_tag.pack()

typing_box = Text(height=5, width=30)
typing_box.focus()
typed = typing_box.get("1.0", END)
typing_box.pack()


def start_timer():
    paragraph.config(text=choice(sentences))


start_button = Button(text="Start", command=start_timer)
start_button.pack()

window.mainloop()