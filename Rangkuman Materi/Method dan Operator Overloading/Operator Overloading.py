class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num,"/",self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

f = Fraction(2,4)
f.show()
print(f)

def __add__(self,otherfraction):
    newnum = self.num * otherfraction.den+self.den * otherfraction.num
    newden = self.den * otherfraction.den

    return Fraction(newnum,newden)
    
f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1+f2)
