#Tugas Praktikum 2
#Zainul Abad
#160411100116

import calendar;
import time;
localtime = time.localtime(time.time())


class orang:
    def __init__(self):
        self.nama = input("Nama : " )
        self.tmplahir = input("Tempat Lahir : ")
        self.thlahir = int(input("Tahun lahir : "))
        self.alamat = input("Alamat : ")
        self.hobi = input("Hobi : ")
        self.citacita = input("Cita-Cita : ")
        self.tahunsekarang = localtime

    def perkenalan(self):
        print("Hello, Saya",self.nama)

    def umursekarang(self):
        print("Umur Sekarang ",int(self.tahunsekarang.tm_year)- int(self.thlahir),"tahun")

    def prediksi(self):
        self.pu=input("Masukan Tahun Untuk Prediksi :")
        print("Pada Tahun",self.pu,"Saya Berumur :", int(self.pu)-int(self.thlahir),"Tahun")
        
class Mahasiswa(orang): #(inheritence = )
    def __init__(self):
        self.jenjangpendidikan = input("Jenjang Pendidikan : ")
        self.jurusan = input("Jurusan : ")
        self.university = input("University : ")
        self.thlulus = input("Tahun Lulus : ")
        self.ipk = float(input("IPK : "))
        
    def tampil(self):
        print ("Jenjang pendidikan :", self.jenjangpendidikan,"Jurusan :", self.jurusan,"Universitas :", self.university,"Tahun Lulus :", self.thlulus,"IPK :", self.ipk)

O = orang()
M = Mahasiswa()
O.perkenalan()
O.umursekarang()
O.prediksi()
M.tampil()
