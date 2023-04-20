from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TileGame(ttk.Frame):

    ### input: options = dict
    ### input: master = ttk.Frame
    ### input: controller = MainController
    def __init__(self, master, controller, options):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.opt_lbl_ls = []

        i = 0
        for text, img_path in options.items():
            img = Image.open(img_path)
            ph = ImageTk.PhotoImage(img)
            self.opt_lbl_ls[i] = ttk.Label(self, text=text, image=img).pack()
            i += 1
        """
        self.game_name = game_name

        ttk.Frame.__init__(self, master, padding=10)
        self.grid()

        img = Image.open(pic_path)
        tile_img = ImageTk.PhotoImage(img)
        self.tile_lbl = ttk.Label(self, image=tile_img)
        self.tile_lbl.img = tile_img
        self.tile_lbl.config(image=self.tile_lbl.img)
        self.tile_lbl.grid()

        name_frm = ttk.Frame(master=self)
        name_frm.grid()

        ttk.Label(name_frm, text=self.game_name, font="Comic Sans MS", foreground='#ffe599ff').grid()

        self.tile_lbl.bind('<ButtonPress>', self.mouse_press)
        """
    def mouse_press(self):
        self.destroy()
        print("it works")