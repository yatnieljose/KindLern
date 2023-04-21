from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class MenuFrm(ttk.Frame):

    def __init__(self, master, main_scrn):

        ttk.Frame.__init__(self, master)
        self.pack()
        animal_mtc_img = Image.open(r'Model/Games/GameImg/Game/animal_match.png')
        animal_mtc_ph = ImageTk.PhotoImage(animal_mtc_img)
        self.animal_match_lbl = ttk.Label(self, image=animal_mtc_ph)
        self.animal_match_lbl.img = animal_mtc_ph
        self.animal_match_lbl.config(image=self.animal_match_lbl.img, text="Match the Animal", compound="center", font=("Comic Sans MS", 20))
        self.animal_match_lbl.grid(column=0, row=0)#pack()#grid(column=0, row=0)
        self.animal_match_lbl.bind('<ButtonPress>', main_scrn.load_match_animal)

        job_mtc_img = Image.open(r"Model/Games/GameImg/Game/job_match.png")
        job_mtc_ph = ImageTk.PhotoImage(job_mtc_img)
        self.job_match_lbl = ttk.Label(self, image=job_mtc_ph)
        self.job_match_lbl.img = job_mtc_ph
        self.job_match_lbl.config(image=self.job_match_lbl.img, text="Match the Job")
        self.job_match_lbl.grid(column=1, row=0)
        self.job_match_lbl.bind("<ButtonPress>", main_scrn.load_match_job)

    def close(self):

        self.destroy()