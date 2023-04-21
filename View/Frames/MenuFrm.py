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
        self.job_match_lbl.config(image=self.job_match_lbl.img, text="Match the Job", compound="center", font=("Comic Sans MS", 20))
        self.job_match_lbl.grid(column=1, row=0)
        self.job_match_lbl.bind("<ButtonPress>", main_scrn.load_match_job)

        az_type_img = Image.open(r"Model/Games/GameImg/Game/type_letter.png")
        az_type_ph = ImageTk.PhotoImage(az_type_img)
        self.az_type_lbl = ttk.Label(self, image=az_type_ph)
        self.az_type_lbl.img = az_type_ph
        self.az_type_lbl.config(image=self.az_type_lbl.img, text="Type the Letter", compound="center", font=("Comic Sans MS", 20))
        self.az_type_lbl.grid(column=2, row=0)
        self.az_type_lbl.bind("<ButtonPress>", main_scrn.load_type_letter)

    """def close(self):

        self.destroy()"""