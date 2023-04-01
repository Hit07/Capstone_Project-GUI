from random import choice
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -------------------------------FUNCTIONS----------------------------------------------------------------
try:
    data = pd.read_csv("data/unknown.csv")

except FileNotFoundError:
    display_words = pd.read_csv("data/Kannada_words.csv")
    dict_words = display_words.to_dict(orient="records")
else:
    dict_words = data.to_dict(orient="records")
finally:
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dict_words)
    canvas.itemconfig(title, text="Kannada", fill="black")
    canvas.itemconfig(word, text=current_card["Kannada"], fill="black")
    canvas.itemconfig(old_image, image=front_image)
    flip_timer = window.after(2000, flip)


def flip():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(old_image, image=back_image)


def known():
    dict_words.remove(current_card)
    # print(len(dict_words))
    next_card()
    data = pd.DataFrame(dict_words)
    data.to_csv("data/unknown.csv",index=False)


# ----------------------------------- UI SETUP----------------------------------------------------------

flip_timer = window.after(2000, flip)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
old_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="/Users/hitesh/Project03/flash-card-project-start/images/wrong.png")
wrong_mark = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_mark.grid(row=1, column=0)

right_image = PhotoImage(file="/Users/hitesh/Project03/flash-card-project-start/images/right.png")
right_mark = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=known)
right_mark.grid(row=1, column=1)

next_card()
window.mainloop()

