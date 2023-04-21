import string 
from random import choice

class TypeLetter:

    def __init__(self):

        low_case = list(string.ascii_lowercase)
        up_case = list(string.ascii_uppercase)
        self.options = {}

        for x in range(len(up_case)):
            self.options[low_case[x]] = up_case[x] + low_case[x]

        self.answer = choice(list(self.options.keys()))

    def get_options(self):
        return(self.options)
    
    def get_answer(self):
        return(self.answer)