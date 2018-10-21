class pegawai:
    __nama=""
    __alamat=""
    __gaji=0

    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat

    def __hitunggaji(self):
        upah_lembur=20000
        gaji_pokok=2000000
        jum_lembur=int(input("Total Jam Lembur :"))
        self.__gaji=(upah_lembur * jum_lembur) + gaji_pokok

    def tampil(self):
        print ("\n-- Menghitung dan Menampilkan Detail Gaji Pegawai ---")
        print ("Nama : ",self.__nama)
        print ("Alamat : ",self.__alamat)

        self.__hitunggaji()
        print ("Total Gaji : ",self.__gaji)

pgw=pegawai("Zainul Abad","Ploso Nganjuk")
pgw.tampil()

pgw2=pegawai("Iqbal Okthapian","Lamongan")
pgw2.tampil()
        
    
