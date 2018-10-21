class Makanan:
    def __init__(self):
        self.nama=input("Nama :")
        self.harga=input("Harga :")
        self.diskon=input("Diskon :")
        self.exdate=input("Exdate :")
    def tampilsemua(self):
        print('Nama         :',self.nama,
              '\nHarga        : Rp.',self.harga,
              '\nDiskon       : Rp.',self.diskon,
              '\nExpired Date :',self.exdate,'\n')
class Pakaian:
    def __init__(self):
        self.nama=input("Nama :")
        self.harga=input("Harga :")
        self.diskon=input("Diskon :")
        self.ukuran=input("Ukuran :")
    def tampilsemua(self):
        print('Nama         :',self.nama,
              '\nHarga        : Rp.',self.harga,
              '\nDiskon       : Rp.',self.diskon,
              '\nUkuran       :',self.ukuran,'\n')
for i in (Makanan(),Pakaian()):
  i.tampilsemua()
