# Tugas Kelompok / Tugas ke 2
# Zainul Abad - 160411100116
# Alvin Nur Arrofi - 160411100111

import time;
localtime = time.localtime(time.time())

no = int(160411100116);
nama = ("Zainul Abad");
tgllahir = int(1997);

class pegawai:
    def __init__(self):
        self.no = no
        self.nama = nama
        self.tahunlahir = tgllahir
        self.tahunsekarang = localtime

    def tampilno(self):
        print(self.no)

    def tampilnama(self):
        print(self.nama)

    def tampiltgllahir(self):
        print(self.tahunlahir)

    def hitungumur(self):
        print(int(self.tahunsekarang.tm_year)- int(self.tahunlahir))

    

pegawai1 = pegawai()
print ("No : "),pegawai1.tampilno()
print ("")
print ("Nama : "),pegawai1.tampilnama()
print ("")
print ("Umur sekarang : "),pegawai1.hitungumur()
