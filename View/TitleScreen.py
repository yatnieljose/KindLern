from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TitleScreen(ttk.Frame):

    def __init__(self, master, controller):
        self.controller = controller
        ttk.Frame.__init__(self, master)
        self.grid()
        
        img = Image.open(r"View\Images\title_img.png")
        title_img = ImageTk.PhotoImage(img)
        self.title_lbl = ttk.Label(self, image=title_img)
        self.title_lbl.img = title_img
        self.title_lbl.config(image=self.title_lbl.img)
        self.title_lbl.grid()

        self.title_lbl.bind('<ButtonPress>', self.mouse_press)

    def mouse_press(self, event):
        """global prev
        print('alive\n')
        prev = event"""
        self.destroy()
        self.controller.load_menu()
        