class pegawai:
    def __init__(self):
        self.nama = input("Nama :")
    def show(self):
        raise NotimplementedError("subclass must implemet abstract method")
        
class manager(pegawai):
    def __init__(self, nama, gaji, tunjangan):
        pegawai.__init__(self, nama)
        self.tunjangan = int(input("Tunjangan :"))
        self.gaji = gaji
    def gaji(self):
        print(self.gaji + self.tunjangan)

class programmer(pegawai):
    def __init__(self, nama, gaji, bonus):
        pegawai.__init__(self, nama)
        self.bonus = int(input("Bonus :"))
        self.gaji = gaji
    def gaji(self):
        print(self.gaji + self.bonus)

pgw = pegawai()
mng = manager()
pgm = programmer()

