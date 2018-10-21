class pegawai:
    def __init__(self):
        self.nama = input("Nama :")
        self.idpegawai = int(input("ID Pegawai :"))

class toko:
    def __init__(self):
        self.namatoko = input("Nama Toko :")
        self.lokasi = input("Lokasi :")

class penempatan(pegawai,toko):
    def __init__(self):
        pegawai.__init__(self)
        toko.__init__(self)

    def menampilkan(self):
        print("\nNama Pegawai :",self.nama)
        print("Lokasi :", self.lokasi)
        print("Nama Toko :",self.namatoko)

penempatan1 = penempatan()
penempatan1.menampilkan()
