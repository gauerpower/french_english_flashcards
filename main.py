import tkinter, pandas, random

word_data = pandas.read_csv('data/french_words.csv')
words_to_learn = word_data.to_dict(orient = 'records')

current_words = {}

def next_card():
    big_ol_canvas.itemconfig(card_instructions, text = '')
    global current_words
    current_words = random.choice(words_to_learn)
    big_ol_canvas.itemconfig(card_title, text = 'French')
    big_ol_canvas.itemconfig(card_word, text = current_words['French'])
    big_ol_canvas.itemconfig(big_ol_card, image = card_front_img)

def flip_card():
    if current_words == {}:
        next_card()
        return
    if big_ol_canvas.itemcget(card_title, 'text') == 'French':
        big_ol_canvas.itemconfig(card_title, text = 'English')
        big_ol_canvas.itemconfig(card_word, text = current_words['English'])
        big_ol_canvas.itemconfig(big_ol_card, image = card_back_img)
    elif big_ol_canvas.itemcget(card_title, 'text') == 'English':
        big_ol_canvas.itemconfig(card_title, text = 'French')
        big_ol_canvas.itemconfig(card_word, text = current_words['French'])
        big_ol_canvas.itemconfig(big_ol_card, image = card_front_img)

window = tkinter.Tk()
window.title('Flashcards')
window.config(padx = 50, pady = 50, bg = "#B1DDC6")

big_ol_canvas = tkinter.Canvas(width = 800, height = 526)
card_front_img = tkinter.PhotoImage(file = 'images/card_front.png')
card_back_img = tkinter.PhotoImage(file = 'images/card_back.png')
big_ol_card = big_ol_canvas.create_image(400, 263, image = card_front_img)
card_title = big_ol_canvas.create_text(400, 150, text = 'French-English Flash Cards', font = ('Courier', 40, 'italic'), fill = '#000')
card_word = big_ol_canvas.create_text(400, 263, text = '', font = ('Courier', 60, 'bold'), fill = '#000')
card_instructions = big_ol_canvas.create_text(400, 396, text = 'Click any button to start', font = ('Courier', 40, 'italic'), fill = '#000')
big_ol_canvas.config(bg = "#B1DDC6", highlightthickness = 0)
big_ol_canvas.grid(row = 1, column = 1, columnspan = 2)

flip_button = tkinter.Button(text = 'Flip Card', font = ('Courier', 25, 'bold'), command = flip_card)
flip_button.grid(row = 2, column = 1)
flip_button.config(width = 10, height = 3)

next_button = tkinter.Button(text = 'Next Card', font = ('Courier', 25, 'bold'), command = next_card)
next_button.grid(row = 2, column = 2)
next_button.config(width = 10, height = 3)

window.mainloop()