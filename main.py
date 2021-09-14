from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------------CREATING NEW FLASHCARDS-----------------------------------
data = pandas.read_csv("data_french_words.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)
current_card = {}

def next_word():
    global current_card
    current_card = random.choice(data_dict)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# to change to english meaning of the french word
def flip_card():

    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, file="images_card_back.png")

#------------------------------------UI SETUP----------------------------


window = Tk()
window.title("Flash Card Game")
# window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


window.after(3000, func=flip_card)


# image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images_card_front.png")
card_back_image = PhotoImage(file="images_card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images_wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images_right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_word)
known_button.grid(row=1, column=1)

next_word()


window.mainloop()
