class mahasiswa():
    __nim=0
    def __init__(self):
        self.__nim="116"
        self.nama="Zainul Abad"    

    def datamahasiswa(self):
        print ("NIM : %s " % self.__nim)
        print ("Nama : %s " % self.nama)
        print ("\n")

    def setnim(self,nim):
        self.__nim=nim
    
    def __datamahasiswa(self):
        print("Nim : %s" % self.__nim)
        print("Nama : %s" % self.nama)
        

        
a = mahasiswa()
a.setnim("112")
a.datamahasiswa()
a._mahasiswa__datamahasiswa()

        
