from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TileGame(ttk.Frame):

    ### input: options = dict
    ### input: master = ttk.Frame
    ### input: controller = MainController
    def __init__(self, master, controller, options, answer, main_scrn):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.main_scrn = main_scrn
        self.answer = answer
        self.options = options
        self.controller = controller
        self.opt_frm = ttk.Frame(self)
        self.ans_frm = ttk.Frame(self)
        self.opt_frm.grid(row=0)
        self.ans_frm.grid(row=1)
        self.opt_lbl_ls = [None, None, None, None]
        self.load_selections()

    def load_selections(self):

        i = 0
        for txt, img_path in self.options.items():
            img = Image.open(img_path)
            ph = ImageTk.PhotoImage(img)
            self.opt_lbl_ls[i] = ttk.Label(self.opt_frm, text=txt, image=ph)
            self.opt_lbl_ls[i].img = ph
            self.opt_lbl_ls[i].config(image=self.opt_lbl_ls[i].img)
            self.opt_lbl_ls[i].bind("<ButtonPress>", self.selected)
            i += 1

        self.opt_lbl_ls[0].grid(row=0, column=0)
        self.opt_lbl_ls[1].grid(row=0, column=1)
        self.opt_lbl_ls[2].grid(row=0, column=2)
        self.opt_lbl_ls[3].grid(row=0, column=3)

        self.ans_lbl = ttk.Label(self.ans_frm, text=self.answer, font=("Comic Sans MS", 36))
        self.ans_lbl.grid()

    def selected(self, event):
        for x in self.opt_lbl_ls:
            x.destroy()
        img = Image.open(self.options[self.answer])
        ph = ImageTk.PhotoImage(img)
        self.opt_lbl_ls = ttk.Label(self.opt_frm, text=self.answer, image=ph)
        self.opt_lbl_ls.img = ph
        self.opt_lbl_ls.config(image=self.opt_lbl_ls.img)
        self.opt_lbl_ls.bind("<ButtonPress>", self.next_game)
        self.opt_lbl_ls.grid()

    def next_game(self, event):
        game = self.controller.get_game().get_name()
        if game == "M_Animal":
            self.main_scrn.load_match_animal(event)
        elif game == "M_Job":
            self.main_scrn.load_match_job(event)