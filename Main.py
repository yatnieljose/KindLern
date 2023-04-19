from tkinter import *
from tkinter import ttk
from Controller.MainController import *
from Model.Games import *
import importlib
import pkgutil
import os

#def Main(master):#(Tk):

#    MainController(master)
class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main_controller = MainController(self)
        width, height = self.winfo_screenwidth, self.winfo_screenheight
        #self.geometry('%dx%d+0+0' % (width, height))
        #### fullscreen
        #self.attributes('-fullscreen', True)
        #self.geometry('800x480')
        #self.propagate(False)

if __name__ == "__main__":
    #root = Tk()
    #Main(root)
    pkg_dir = os.path.dirname(__file__)
    for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
        importlib.import_module('.' + name, __package__)

    all_my_base_classes = {cls.__name__: cls for cls in base._MyBase.__subclasses__()}
    root = Main()
    root.mainloop()