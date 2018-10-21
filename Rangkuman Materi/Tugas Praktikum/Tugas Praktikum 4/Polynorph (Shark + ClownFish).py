class Shark():
    def swim(self):
        print('yes')
    def swim_backwards(self):
        print('no')
    def skeleton(self):
        print('cartilage')

class ClownFish():
    def swim(self):
        print('yes')
    def swim_backwards(self):
        print('yes')
    def skeleton(self):
        print('bone')

a = Shark()
a.skeleton()

b = ClownFish()
b.skeleton()
