jarijari = float(input("Masukkan Jari-jari :"))

class lingkaran:
    def __init__(self):
        self.jarijari = jarijari

    def menampilakan(self):
        print("\nJari-jari :", self.jarijari)

    def luaspermukaan(self):
        print("Luas Permukaan :",22/7*self.jarijari**2)

    def keliling(self):
        print("Keliling Lingkaran",2*22/7*self.jarijari)

class tabung(lingkaran):
    def __init__(self):
        self.tinggitabung = float(input("Tinggi Tabung :"))


    def menampilkan(self):
        print("\nTinggi Tabung :", self.tinggitabung)

    def luaspermukaantbg(self):
        print("Luas Permukaan Tabung :",(2*22/7*(jarijari))*((jarijari)+self.tinggitabung))
        
        

lingkaran1=lingkaran()
tabung1=tabung()
lingkaran1.menampilakan()
lingkaran1.luaspermukaan()
lingkaran1.keliling()
tabung1.menampilkan()
tabung1.luaspermukaantbg()
