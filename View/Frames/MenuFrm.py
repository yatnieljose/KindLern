from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class MenuFrm(ttk.Frame):

    def __init__(self, master, controller):

        ttk.Frame.__init__(self, master)
        self.pack()
        animal_mtc_img = Image.open(r'Model/Games/GameImg/Game/animal_match.png')
        animal_match_ph = ImageTk.PhotoImage(animal_mtc_img)
        self.animal_match_lbl = ttk.Label(self.container_frm, text="Match the Animal", image=animal_mtc_img)
        self.animal_match_lbl.grid(column=0, row=0)
        self.animal_match_lbl.bind('<ButtonPress>', self.load_animal_mtc)