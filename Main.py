from tkinter import *
from tkinter import ttk
from Controller.MainController import *
#from Model.Games.MatchAnimal import MatchAnimal

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
    my_game = MatchAnimal()
    print(my_game.get_options())
    root = Main()
    root.mainloop()