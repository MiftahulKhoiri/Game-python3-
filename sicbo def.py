import random
from time import sleep
from datetime import datetime

print ('~~~ selamat datang di permainan roll dadu ~~~')
print ('\t','[••• silahkan bermain •••]','\n')
         
main = int (input(' Berapakali ingin bermain = '))
wjd = int(input (' waktu jeda [ menit : detik ] = '))

def logo ():#logo pertama
    print ('\t',' ---------------------')
    print ('\t','|  {••••BERMAIN••••}  |')
    print ('\t',' ---------------------',)
    print ('\t','  [ PUTARAN DADU KE ]','\n','\t','\t',f" [ {i} ]",'\n')

def game (): # game rool randint.choice
    a = random.randint (1,6)
    b = random.randint (1,6 )
    c = random.randint (1,6 )
    a1 = random.randint (1,6 )
    b1 = random.randint (1,6 )
    c1 = random.randint (1,6 )
    
    hasil =[a,a1]
    hasil1 =[b,b1]
    hasil2 = [c,c1]
    
    ahir = random.choice(hasil)
    ahir1 = random.choice(hasil1)
    ahir2 = random.choice(hasil2)
    
    keluar = ahir,ahir1,ahir2
    total = int(ahir + ahir1 + ahir2)
    
    print ('\t','MULAI :','\b')
    print ('\t','~~~~~~~')
    print('\t','hasilnya adalah = ',keluar)
    print('\t','total = ','(',total,')')
    
    if total <= 10:
         print ('\t','katagori = ( KECIL )','\n')
         
    elif total >= 11:
         print ('\t','katagori = ( BESAR )','\n')
         
def game1 ():#game 1 angka
    a = random.randint(3,18)
    
    keluar = a
    
    print('\t','hasilnya adalah = ',keluar)
    
    if keluar <= 10:
         print ('\t','katagori = ( KECIL )','\n')
         
    elif keluar >= 11:
         print ('\t','katagori = ( BESAR )','\n')
         
def mundur (wjd):# waktu mundur 
    while wjd:
        mins, secs = divmod(wjd, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\t','\t','WAKTU = ','( ',timer,' )', end="\r")
        sleep(1)
        wjd -= 1
        

def waktu (): #info waktu
    e=datetime.now()
    print ('\t',"¤[ tanggal/bulan/tahun  = %s/%s/%s ]¤" % (e.day, e.month, e.year))
    print ('\t',"¤[ jam : menit : detik = %s:%s:%s ]¤" % (e.hour, e.minute, e.second))
    print ('\t')
    
    
def batasAtas ():#batas atas 
    print('\t','{=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=}')
    
def batasBawah ():#batas bawah
    print('\t','{=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=}','\t')
    print('\t')
    print('\t')
    print('\t')
    
for i in range (main):
    batasAtas()
    logo ()
    waktu ()
    game ()
    game1 ()
    batasBawah ()
    mundur (wjd)
   