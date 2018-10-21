class persegi:
    def __init__(self, jumlah_persegi = 4, bentuk_persegi = "persegi" ):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi

    def deskripsi(self):
        print("Persegi Bebas")

    def display(self):
        print(self.jumlah_persegi, self.bentuk_persegi)

class persegipanjang(persegi):
    def __init__(self, jumlah_persegi = 4, bentuk_persegi = "persegi panjang" ):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi

    def deskripsi(self):
        print("Persegi Panjang dan ada 2 pasang yang mempunyai panjang sisi yang sama.")

class bujursangkar(persegi):
    def __init__(self, jumlah_persegi = 4, bentuk_persegi = "bujur sangkar"):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi

    def deskripsi(self):
        print("keempatnya sama panjang")


persegi3 = persegi("")
persegi1 = persegipanjang("")
persegi2 = bujursangkar("")

persegi3.deskripsi()
persegi1.deskripsi()
persegi2.deskripsi()

persegi3.display()
persegi1.display()
persegi2.display()
