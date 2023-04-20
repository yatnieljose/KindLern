from tkinter import *
from tkinter import ttk
from View.Frames.TitleScreen import *
from View.Frames.MainScreen import *
from Model.Games.GameModules.MatchAnimal import MatchAnimal
from Model.Games.GameModules.MatchJob import MatchJob

class MainController:

    # master: Tk from Main.py
    def __init__(self, master):
        self.main_tk = master
        self.current_frm = None
        self.load_title()
        self.game = None
        #self.current_frm = self.load_title()
        #self.current_frm.grid()
        #self.current_frm.grid()
        #self.load_title()

    def load_title(self):
        #self.title_scrn = TitleScreen(self.main_tk)
        #self.title_scrn.grid()
        self.current_frm = TitleScreen(self.main_tk, self)

    def load_main(self):
        self.current_frm = MainScreen(self.main_tk, self)
    
    def load_match_animal(self):
        self.game = MatchAnimal()

    def get_options(self):
        self.game.get_options()