from tkinter import *
from tkinter import ttk
from View.Frames.TitleScreen import *
from View.Frames.MainScreen import *
from Model.Games.MatchAnimal import MatchAnimal
from Model.Games.MatchJob import MatchJob
from Model.Games.TypeLetter import TypeLetter

class MainController:

    # master: Tk from Main.py
    def __init__(self, master):
        self.main_tk = master
        self.main_frm = None
        self.load_title()
        self.game = None

    def load_title(self):
        self.main_frm = TitleScreen(self.main_tk, self)

    def load_main(self):
        self.main_frm = MainScreen(self.main_tk, self)
    
    def load_match_animal(self):#, *_args):
        self.game = MatchAnimal()

    def load_match_job(self):
        self.game = MatchJob()

    def load_type_letter(self):
        self.game = TypeLetter()

    def get_options(self):
        return(self.game.get_options())
    
    def get_answer(self):
        return(self.game.get_answer())
    
    def get_game(self):
        return(self.game)