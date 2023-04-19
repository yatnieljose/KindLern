from tkinter import *
from tkinter import ttk

class Tile(ttk.Frame):

    def __init__(self, master, game_name, pic_path):
        ttk.Frame.__init__(self, master)
        