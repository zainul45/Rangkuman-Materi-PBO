class pecahan:
    def __init__(self):
        self.pembilang = pembilang = int(input("Pembilang :"))
        self.penyebut = penyebut = int(input("Penyebut :"))

    def bilanganpecahan(self):
        print("Bilangan Pecahan :", self.pembilang ,"/",self.penyebut)

    def sederhana(self):
        stop=True
        while stop:
            if(self.pembilang/2==int(self.pembilang/2) and self.penyebut/2==int(self.penyebut/2)):
                self.pembilang=self.pembilang/2
                self.penyebut=self.penyebut/2
            elif(self.pembilang/3==int(self.pembilang/3) and self.penyebut/3==int(self.penyebut/3)):
                self.pembilang=self.pembilang/3
                self.penyebut=self.penyebut/3
            elif(self.pembilang/5==int(self.pembilang/5) and self.penyebut/5==int(self.penyebut/5)):
                self.pembilang=self.pembilang/5
                self.penyebut=self.penyebut/5
            elif(self.pembilang/7==int(self.pembilang/7) and self.penyebut/7==int(self.penyebut/7)):
                self.pembilang=self.pembilang/7
                self.penyebut=self.penyebut/7
            elif(self.pembilang/11==int(self.pembilang/11) and self.penyebut/11==int(self.penyebut/11)):
                self.pembilang=self.pembilang/11
                self.penyebut=self.penyebut/11
            else:
                stop=False
                
        print("Pecahan Paling Sederhana :",int(self.pembilang),"/",int(self.penyebut))


pecahan1 = pecahan()
pecahan1.bilanganpecahan()
pecahan1.sederhana()
