class Kategori:
    def __init__(self):
        self.kode=input("Kode :")
        self.deskripsi=input("Deskripsi :")
    def tkode(self):
        print("Kode :",self.kode)
    def tdesk(self):
        print("Deskripsi :",self.deskripsi)
class Barang(Kategori):
    def __init__(self):
        self.nama=input("Nama :")
        self.harga=input("Harga :")
        self.diskon=input("Diskon :")
    def tampilsemua(self):
        raise NotImplementedError('Hanya Subclass yang Boleh mengimplementasikan metode Tampil abstact method')
class Makanan(Barang):
    def __init__(self):
        self.exdate=input("Exdate :")
        Barang.__init__(self)
    def tampilsemua(self):
        print('Nama         :',self.nama,
              '\nHarga        : Rp.',self.harga,
              '\nDiskon       : Rp.',self.diskon,
              '\nExpired Date :',self.exdate,'\n')
class Pakaian(Barang):
    def __init__(self):
        self.ukuran=input("Ukuran :")
        Barang.__init__(self)
    def tampilsemua(self):
        print('Nama         :',self.nama,
              '\nHarga        : Rp.',self.harga,
              '\nDiskon       : Rp.',self.diskon,
              '\nUkuran       :',self.ukuran,'\n')

for i in (Makanan(),Pakaian()):
  i.tampilsemua()
