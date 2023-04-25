from tkinter import *
from tkinter import ttk

class KeyGame(ttk.Frame):

    def __init__(self, master, controller, options, answer, main_scrn):
        ttk.Frame.__init__(self, master)
        self.bind("<Key>", self.key_stroke)
        self.focus_set()
        self.grid()
        self.main_scrn = main_scrn
        self.answer = answer
        self.options = options
        self.controller = controller
        self.letter_lbl = ttk.Label(self, text=self.options[self.answer], font=("Comic Sans MS", 140))
        self.letter_lbl.grid()

    def key_stroke(self, event):
        ### If key stroke correct, load new game
        if (self.controller.get_game().check_answer(event.char)):
            self.main_scrn.load_type_letter(event)
        ### Else, do not change
        else:
            pass