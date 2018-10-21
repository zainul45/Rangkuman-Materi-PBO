class orang:
  def __init__(self,nama):
    self.nama=nama
  def nama(Self):
    return Self.nama
class mahasiswa(orang):
  def __init__(self,nama,npm,semester):
    orang.__init__(self,nama)
    self.npm=npm
    self.semester=semester
  def namamahasiswa(self):
     print ("Nama : %s " % self.nama)
     print ("Npm :%s" % self.npm)
     print ("Semester :%s" % self.semester)
class pegawai(orang):
  def __init__(self,nama,nip):
    orang.__init__(self,nama)
    self.nip=nip
  def namapegawai(Self):
    print ("Nama : %s " % Self.nama)
    print ("nip:%s" % Self.nip)
class karyawan(pegawai):
  def __init__(self,nama,nip):
    pegawai.__init__(self,nama,nip)
  def namakaryawan(self):
    print ("Nama karyawan  : %s " % self.nama)
    print ("nip:%s" % self.nip)
class dosen(pegawai):
  def __init__(self,nama,nip,nidn):
    pegawai.__init__(self,nama,nip)
    self.nidn=nidn
  def namadosen(self):
    print ("Nama Dosen : %s " % self.nama)
    print ("nip:%s" % self.nip)
    print ("nidn:%s" % self.nidn)
    

y = dosen("Drs. Slamet Sutjipto M.T.	","19580501 198703 1001","0001055805")
z = karyawan("Briana Simorangkir", "19610211 199201 2001")


y.namadosen()
z.namakaryawan()

    
    
