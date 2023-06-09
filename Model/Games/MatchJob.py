#from . import Game
from os import listdir 
from os.path import isfile, join, basename, dirname
from random import choices, choice, sample
import platform 

class MatchJob:

    def __init__(self):

        self.resource_path = dirname(__file__)
        self.options = {}
        self.name = "M_Job"

        path_mkr = self.add_path(self.resource_path)
        img_ls = self.load_options(self.resource_path)
        img_ls = sample(img_ls, k=4)
        
        for x in img_ls:
            self.options[basename(x).split(".")[0].title()] = path_mkr(x)
        
        self.answer = choice(list(self.options.keys()))

    ### Returns options from image directory ###
    def load_options(self, abs_path):
        if "Windows" in platform.platform():
            return(listdir(abs_path + "\GameImg\Jobs"))
        else:
            return(listdir(abs_path + "/GameImg/Jobs"))
    
    def get_options(self):
        return(self.options)
    
    def get_answer(self):
        return(self.answer)

    def get_img_path(self):
        return(self.resource_path)

    def add_path(self, path):
        if "Windows" in platform.platform():
            return lambda f : path + "\\GameImg\\Jobs\\" + f 
        else:
            return lambda f : path + "/GameImg/Jobs/" + f

    def get_name(self):
        return(self.name)