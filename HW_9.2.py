import random
list_of_colors = ["white", "yellow", "purple", "red"]
class Ghost(object):
    '''ghost class trial'''

    
    def __init__(self):
        self.color=random.choice(list_of_colors)
    
