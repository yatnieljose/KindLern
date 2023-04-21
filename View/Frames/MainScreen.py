from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from View.Frames.TileGame import TileGame
from View.Frames.MenuFrm import MenuFrm

class MainScreen(ttk.Frame):

    def __init__(self, master, controller):

        ttk.Frame.__init__(self, master)
        self.grid()

        ### Header Frame ###
        self.header_frm = ttk.Frame(self)
        self.header_frm.grid(row=0)#pack()#.grid(row=0)
        ### Container Frame ###
        self.container_frm = ttk.Frame(self)
        self.container_frm.grid(row=1)

        self.controller = controller
        self.current_frm = MenuFrm(self.container_frm, self)

        cancel_img = Image.open(r'View/Images/cancel_icon.png')
        cancel_ph = ImageTk.PhotoImage(cancel_img)
        self.cancel_lbl = ttk.Label(self.header_frm, image=cancel_ph)
        self.cancel_lbl.img = cancel_ph
        self.cancel_lbl.config(image=self.cancel_lbl.img)
        self.cancel_lbl.grid(column=0, row=0)

        boy_img = Image.open(r'View/Images/kind_b.png')
        boy_ph = ImageTk.PhotoImage(boy_img)
        self.boy_lbl = ttk.Label(self.header_frm, image=boy_ph)
        self.boy_lbl.img = boy_ph
        self.boy_lbl.config(image=self.boy_lbl.img)
        self.boy_lbl.grid(column=1, row=0)

        logo_img = Image.open(r'View/Images/logo.png')
        logo_ph = ImageTk.PhotoImage(logo_img)
        self.logo_lbl = ttk.Label(self.header_frm, image=logo_ph)
        self.logo_lbl.img = logo_ph
        self.logo_lbl.config(image=self.logo_lbl.img)
        self.logo_lbl.grid(column=2, row=0)

        girl_img = Image.open(r'View/Images/kind_g.png')
        girl_ph = ImageTk.PhotoImage(girl_img)
        self.girl_lbl = ttk.Label(self.header_frm, image=girl_ph)
        self.girl_lbl.img = girl_ph
        self.girl_lbl.config(image=self.girl_lbl.img)
        self.girl_lbl.grid(column=3, row=0)

        self.cancel_lbl.bind('<ButtonPress>', self.exit)

        ### current Frame ###
        #self.current_frm.pack()
        #self.current_frm = 

        """animal_mtc_img = Image.open(r'Model/Games/GameImg/Game/animal_match.png')
        animal_match_ph = ImageTk.PhotoImage(animal_mtc_img)
        self.animal_match_lbl = ttk.Label(self.current_frm, text="Match the Animal", image=animal_mtc_img)
        self.animal_match_lbl.grid(column=0, row=0)
        self.animal_match_lbl.bind('<ButtonPress>', self.load_animal_mtc)"""

        

    def exit(self, event):
        #print(type(MenuFrm))
        if type(self.current_frm).__name__ is "MenuFrm":
            self.destroy()
            self.controller.load_title()
        else:
            self.current_frm.destroy()
            self.current_frm = MenuFrm(self.container_frm, self)

    def load_match_animal(self, event):
        self.controller.load_match_animal()
        self.current_frm.destroy()
        opt_ls = self.controller.get_options()
        ans = self.controller.get_answer()
        self.current_frm = TileGame(self.container_frm, self.controller, opt_ls, ans, self)

    def load_match_job(self, event):
        self.load_match_job()
        self.current_frm.destroy()
        opt_ls = self.controller.get_options()
        ans = self.controller.get_answer()
        self.current_frm(self.container_frm, self.controller, opt_ls, ans, self)