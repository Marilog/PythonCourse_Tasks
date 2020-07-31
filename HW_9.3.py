class Human:
    def __init__(self, name):
        self.name = name
class Man(Human):
    def __init__(self, name):
        self.name = name
class Woman(Human):
    def __init__(self, name):
        self.name = name
   

def God():
    Adam = Man("Adam")
    Eve = Woman("Eva")
    return[Adam, Eve]
        
paradise = God()