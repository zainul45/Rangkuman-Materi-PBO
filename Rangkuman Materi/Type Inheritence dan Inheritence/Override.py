class fish:
    def __init__(self, first_name, last_name="fish", skeleton="bone", eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print("The Fish is swimming.")
    def swim_backwards(self):
        print("The fish can swim backwards.")

class shark(fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

hiu = shark("Hiu Besar")
hiu.swim_backwards()
