from tkinter import *
from Controller.MainController import *

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="white")
        self.geometry("800x480")
        self.main_controller = MainController(self)
        WIDTH, HEIGHT = self.winfo_screenwidth, self.winfo_screenheight

if __name__ == "__main__":
    root = Main()
    root.mainloop()