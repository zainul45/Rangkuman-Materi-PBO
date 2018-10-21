class mahasiswa:
    def __init__(self):
        self.nama = input("Nama :")
        self.npm = input("NPM :")

class matakuliah:
    def __init__(self):
        self.kode = input("Kode :")
        self.namamatkul = input("Nama Mata Kuliah :")

class pengambilanmatkul(mahasiswa,matakuliah):
    def __init__(self):
        mahasiswa.__init__(self)
        matakuliah.__init__(self)
        self.tambahannilai = float(input("Tambahan Nilai :"))

    def main(self):
        print(self.nama, self.npm, self.namamatkul, self.tambahannilai)

pm = pengambilanmatkul()
pm.main()
