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
        self.header_frm = ttk.Frame(master=self)#, style="KindLern.TFrame")
        self.header_frm.pack()#grid(row=0)#pack()#.grid(row=0)
        
        ### Container Frame ###
        self.container_frm = ttk.Frame(master=self)#, style="KindLern.TFrame")
        self.container_frm.pack()#grid(row=1)

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
        #self.cancel_lbl.grid(column=0, row=0)
        self.cancel_lbl.pack(side="left", anchor="nw")#side="left", anchor="nw")

        """prompt_img = Image.open(r'View/Images/prompt.png')
        prompt_img = prompt_img.resize((750, 180))
        prompt_ph = ImageTk.PhotoImage(prompt_img)
        self.prompt_lbl = ttk.Label(self.header_frm, image=prompt_ph)
        self.prompt_lbl.img = prompt_ph
        self.prompt_lbl.config(image=self.prompt_lbl.img)
        self.prompt_lbl.pack(side="left", anchor="center")"""

        boy_img = Image.open(r'View/Images/kind_b.png')
        boy_img = boy_img.resize((int(width * 147 / 694), int(height * 174 / 369)))
        boy_ph = ImageTk.PhotoImage(boy_img)
        self.boy_lbl = ttk.Label(self.header_frm, image=boy_ph)
        self.boy_lbl.img = boy_ph
        self.boy_lbl.config(image=self.boy_lbl.img)
        #self.boy_lbl.grid(column=1, row=0)
        self.boy_lbl.pack(side="left", anchor="center")

        logo_img = Image.open(r'View/Images/logo.png')
        logo_img = logo_img.resize((width, height))
        logo_ph = ImageTk.PhotoImage(logo_img)
        self.logo_lbl = ttk.Label(self.header_frm, image=logo_ph)
        self.logo_lbl.img = logo_ph
        self.logo_lbl.config(image=self.logo_lbl.img)
        #self.logo_lbl.grid(column=2, row=0)
        self.logo_lbl.pack(side="left", anchor="center")

        girl_img = Image.open(r'View/Images/kind_g.png')
        girl_img = girl_img.resize((int(width * 138 / 694), int(height * 176 / 369)))
        girl_ph = ImageTk.PhotoImage(girl_img)
        self.girl_lbl = ttk.Label(self.header_frm, image=girl_ph)
        self.girl_lbl.img = girl_ph
        self.girl_lbl.config(image=self.girl_lbl.img)
        #self.girl_lbl.grid(column=3, row=0)
        self.girl_lbl.pack(side="left", anchor="center")

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