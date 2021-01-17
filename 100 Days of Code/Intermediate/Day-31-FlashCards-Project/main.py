from tkinter import *
from tkinter import messagebox

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ORIGINAL_CSV_FILE = "./data/french_words.csv"
CSV_FILE_TO_LEARN = "./data/words_to_learn.csv"
SOURCE_LANG = "French"
TARGET_LANG = "English"
FRONT_IMG = "./images/card_front.png"
BACK_IMG = "./images/card_back.png"
CORRECT_IMG = "./images/right.png"
INCORRECT_IMG = "./images/wrong.png"
flip_timer = 0
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv(CSV_FILE_TO_LEARN)
except:
    messagebox.showinfo(title="Congratz!", message="No more cards to learn! Importing original deck")
    original_data = pandas.read_csv(ORIGINAL_CSV_FILE)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def is_known():
    global to_learn
    try:
        to_learn.remove(current_card)
    except ValueError:
        messagebox.showinfo(title="Congratz!", message="No more cards to learn! Importing original deck")
        original_data = pandas.read_csv(ORIGINAL_CSV_FILE)
        to_learn = original_data.to_dict(orient="records")
    else:
        data = pandas.DataFrame(to_learn)
        data.to_csv(CSV_FILE_TO_LEARN, index=False)
        next_card()


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=SOURCE_LANG, fill="black")
    canvas.itemconfig(card_word, text=current_card[SOURCE_LANG], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = screen.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text=TARGET_LANG, fill="white")
    canvas.itemconfig(card_word, text=current_card[TARGET_LANG], fill="white")
    canvas.itemconfig(card_background, image=card_back)


screen = Tk()
screen.title("PyFlascard")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, func=flip_card)
card_front = PhotoImage(file=FRONT_IMG)
card_back = PhotoImage(file=BACK_IMG)
canvas = Canvas(height=526, width=800)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file=INCORRECT_IMG)
fail_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
fail_button.grid(row=1, column=1)

correct_image = PhotoImage(file=CORRECT_IMG)
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=0)

next_card()
screen.mainloop()
