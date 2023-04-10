from tkinter import *
from tkinter import ttk
from View.TitleScreen import *

class MainController:

    # master: Tk from Main.py
    def __init__(self, master):
        self.main_tk = master
        self.current_frm = self.load_title()
        self.current_frm.grid()
        #self.current_frm.grid()
        #self.load_title()

    def load_title(self):
        #self.title_scrn = TitleScreen(self.main_tk)
        #self.title_scrn.grid()
        return(TitleScreen(self.main_tk))