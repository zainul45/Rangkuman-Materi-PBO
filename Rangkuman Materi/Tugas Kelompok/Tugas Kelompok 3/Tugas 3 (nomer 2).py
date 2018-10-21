class orang:
    def __init__(self, name):
        self.name = name
    def printname(self):
        print("name = " +self.name )
        
class Mahasiswa(orang): #(inheritence = )
    def __init__(self,nama, npm,semester):
        orang.__init__(self,nama)
        self.npm=npm
        self.semester=semester
    def NamaMhs(self):
        orang.printname(self)
        print("Nim:",self.npm)
        print("Semester:",self.semester)

class pegawai(orang):
    def __init__(self,nama, nip):
        orang.__init__(self,nama)
        self.nip=nip
    def tampil(self):
        orang.printname(self)
        print("Nip:",self.nip)
class karyawan(pegawai):
    def __init__(self,nama,nip):
        pegawai.__init__(self,nama,nip)
    def nama_karyawan(self):
        print("karyawan")
        pegawai.tampil(self)
class dosen(pegawai):
    def __init__(self,nama, nip,nidn):
        self.nidn=nidn
        pegawai.__init__(self,nama,nip)
    def nama_dosen(self):
        print("Dosen")
        pegawai.tampil(self)
        print("nidn:",self.nidn)
        
andi = dosen("andi",1243627,262781)
andi.nama_dosen()    
danu = karyawan("danu",1243627)
danu.nama_karyawan()
