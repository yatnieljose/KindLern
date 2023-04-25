from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from View.Frames.TileGame import TileGame
from View.Frames.KeyGame import KeyGame
from View.Frames.MenuFrm import MenuFrm

class MainScreen(ttk.Frame):

    def __init__(self, master, controller):

        ttk.Frame.__init__(self, master)
        self.pack(side="top", anchor="center")

        style = ttk.Style()
        style.configure("KindLern.TFrame", background="white")

        ### Header Frame ###
        self.header_frm = ttk.Frame(master=self)
        self.header_frm.pack()
        
        ### Container Frame ###
        self.container_frm = ttk.Frame(master=self)
        self.container_frm.pack()
        self.controller = controller
        self.current_frm = MenuFrm(self.container_frm, self)

        width = 800 // 3
        height = 480 // 3

        cancel_img = Image.open(r'View/Images/cancel_icon.png')
        cancel_img = cancel_img.resize((int(width * 54 / 694), int(height * 54 / 369)))
        cancel_ph = ImageTk.PhotoImage(cancel_img)
        self.cancel_lbl = ttk.Label(self.header_frm, image=cancel_ph)
        self.cancel_lbl.img = cancel_ph
        self.cancel_lbl.config(image=self.cancel_lbl.img)
        self.cancel_lbl.pack(side="left", anchor="nw")

        boy_img = Image.open(r'View/Images/kind_b.png')
        boy_img = boy_img.resize((int(width * 147 / 694), int(height * 174 / 369)))
        boy_ph = ImageTk.PhotoImage(boy_img)
        self.boy_lbl = ttk.Label(self.header_frm, image=boy_ph)
        self.boy_lbl.img = boy_ph
        self.boy_lbl.config(image=self.boy_lbl.img)
        self.boy_lbl.pack(side="left", anchor="center")

        logo_img = Image.open(r'View/Images/logo.png')
        logo_img = logo_img.resize((width, height))
        logo_ph = ImageTk.PhotoImage(logo_img)
        self.logo_lbl = ttk.Label(self.header_frm, image=logo_ph)
        self.logo_lbl.img = logo_ph
        self.logo_lbl.config(image=self.logo_lbl.img)
        self.logo_lbl.pack(side="left", anchor="center")

        girl_img = Image.open(r'View/Images/kind_g.png')
        girl_img = girl_img.resize((int(width * 138 / 694), int(height * 176 / 369)))
        girl_ph = ImageTk.PhotoImage(girl_img)
        self.girl_lbl = ttk.Label(self.header_frm, image=girl_ph)
        self.girl_lbl.img = girl_ph
        self.girl_lbl.config(image=self.girl_lbl.img)
        self.girl_lbl.pack(side="left", anchor="center")

        self.cancel_lbl.bind('<ButtonPress>', self.exit)

    def exit(self, event):
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
        self.controller.load_match_job()
        self.current_frm.destroy()
        opt_ls = self.controller.get_options()
        ans = self.controller.get_answer()
        self.current_frm = TileGame(self.container_frm, self.controller, opt_ls, ans, self)

    def load_type_letter(self, event):
        self.controller.load_type_letter()
        self.current_frm.destroy()
        opt_ls = self.controller.get_options()
        ans = self.controller.get_answer()
        self.current_frm = KeyGame(self.container_frm, self.controller, opt_ls, ans, self)