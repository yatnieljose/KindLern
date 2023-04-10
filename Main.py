from tkinter import *
from tkinter import ttk
from Controller.MainController import *

#def Main(master):#(Tk):

#    MainController(master)
class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main_controller = MainController(self)

if __name__ == "__main__":
    #root = Tk()
    #Main(root)
    root = Main()
    root.mainloop()