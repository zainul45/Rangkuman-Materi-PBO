class Kubus:
    def __init__(self,s):
        self.sisi = s

    def tampilkansisi(self):
        print(self.sisi)

    def luas(self):
        print("Luas =" ,self.sisi ** 2)

    def volume(self):
        print("Volume =" ,self.sisi **3)

Kubus1 = Kubus(4)
Kubus1.tampilkansisi()
Kubus1.luas()
Kubus1.volume()



