from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class MainScreen(ttk.Frame):

    def __init__(self, master, controller):
        self.controller = controller

        ttk.Frame.__init__(self, master)
        self.grid()

        self.header_frm = ttk.Frame(self)
        self.header_frm.grid(row=0)

        cancel_img = Image.open(r'View\Images\cancel_icon.png')
        cancel_ph = ImageTk.PhotoImage(cancel_img)
        self.cancel_lbl = ttk.Label(self.header_frm, image=cancel_ph)
        self.cancel_lbl.img = cancel_ph
        self.cancel_lbl.config(image=self.cancel_lbl.img)
        self.cancel_lbl.grid(column=0, row=0)

        boy_img = Image.open(r'View\Images\kind_b.png')
        boy_ph = ImageTk.PhotoImage(boy_img)
        self.boy_lbl = ttk.Label(self.header_frm, image=boy_ph)
        self.boy_lbl.img = boy_ph
        self.boy_lbl.config(image=self.boy_lbl.img)
        self.boy_lbl.grid(column=1, row=0)

        logo_img = Image.open(r'View\Images\logo.png')
        logo_ph = ImageTk.PhotoImage(logo_img)
        self.logo_lbl = ttk.Label(self.header_frm, image=logo_ph)
        self.logo_lbl.img = logo_ph
        self.logo_lbl.config(image=self.logo_lbl.img)
        self.logo_lbl.grid(column=2, row=0)

        girl_img = Image.open(r'View\Images\kind_g.png')
        girl_ph = ImageTk.PhotoImage(girl_img)
        self.girl_lbl = ttk.Label(self.header_frm, image=girl_ph)
        self.girl_lbl.img = girl_ph
        self.girl_lbl.config(image=self.girl_lbl.img)
        self.girl_lbl.grid(column=3, row=0)

        self.cancel_lbl.bind('<ButtonPress>', self.exit_main)

    def exit_main(self, event):
        self.destroy()
        self.controller.load_title()