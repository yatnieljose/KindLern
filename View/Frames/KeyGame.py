from tkinter import *
from tkinter import ttk

class KeyGame(ttk.Frame):

    def __init__(self, master, controller, options, answer):
        ttk.Frame.__init__(self, master)
        self.bind("<Key>", self.key_stroke)
        #print(ttk.Treeview.parent())
        self.grid()
        self.answer = answer
        self.options = options
        self.controller = controller
        self.letter_lbl = ttk.Label(self, text=self.options[self.answer], font=("Comic Sans MS", 140))
        #self.letter_lbl.bind("<KeyRelease>", self.key_stroke)
        self.letter_lbl.grid()

    def key_stroke(self, event):
        print(event.keysym + ":" + event.char)