import numpy as np
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

def game_np32():# sicbo numpy 32-bit
    a = np.random.randint(1,6,size=3, dtype=np.int32) # random
    b = np.sum(a) #hasil random
    
    print ('\t','MULAI :','\b')
    print ('\t','~~~~~~~')
    print('\t','hasilnya adalah = ',a)
    print('\t','total = ','(',b,')')
    
    if b <= 10:
         print ('\t','katagori = ( KECIL )','\n')
         
    elif b >= 11:
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
    game_np32()
    batasBawah ()
    mundur (wjd)
   
   