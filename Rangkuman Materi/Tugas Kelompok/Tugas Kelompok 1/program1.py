# Tugas Kelompok No 1
# Zainul Abad - 160411100116
# Alvin Nur Arrofi - 160411100111

import time;
nama = input ('Nama Anda : ');
 
waktu = time.localtime()
jam=waktu.tm_hour

if(jam>00 and jam<10):
    print("Selamat pagi",nama);
elif(jam>10 and jam==15):
    print("Selamat Siang",nama);
elif(jam>15 and jam==18):
    print("Selamat Sore",nama);
else:
    print("Selamat Malam",nama);
