from . import Game
from os import listdir 
from os.path import isfile, join, basename, dirname
from random import choices, choice

class MatchAnimal:

    def __init__(self):

        img_ls = self.load_options()
        img_ls = choices(img_ls, k=4)
        self.options = {}
        for x in img_ls:
            self.options[basename(x).split(".")[0].title()] = x
        
        self.answer = choice(list(self.options.keys()))

    ### Returns options from image directory ###
    def load_options(self):
        abs_path = dirname(__file__)
        print (listdir(abs_path + "\GameImg\Animals"))
        return(listdir(abs_path + "\GameImg\Animals"))
    
    def get_options(self):
        return(self.options)
    
    def get_answer(self):
        return(self.answer)