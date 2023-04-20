from . import Game
from os import listdir 
from os.path import isfile, join, basename, dirname
from random import choices, choice
import platform 

class MatchAnimal:

    def __init__(self):

        self.resource_path = dirname(__file__)
        self.options = {}
        self.name = "Match the Job"

        path_mkr = self.add_path(self.resource_path)
        img_ls = self.load_options(self.resource_path)
        img_ls = choices(img_ls, k=4)
        
        for x in img_ls:
            self.options[basename(x).split(".")[0].title()] = path_mkr(x)
        
        self.answer = choice(list(self.options.keys()))