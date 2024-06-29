import numpy as np
from datetime import datetime
import time

# masukan nilai 


def logo ():#logo pertama
    print ('\t',' ---------------------')
    print ('\t','|  {•••• PREDIKSI ••••}  |')
    print ('\t',' ---------------------',)
    
def batasAtas ():#batas atas 
    print('\t','{=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=}')
    
def batasBawah ():#batas bawah
    print('\t','{=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=}','\t')
    print('\t')
    print('\t')
    print('\t')
    
def waktu (): #info waktu sekarang 
    e=datetime.now()
    print ('\t',"¤[ tanggal/bulan/tahun  = %s/%s/%s ]¤" % (e.day, e.month, e.year))
    print ('\t',"¤[ jam : menit : detik = %s:%s:%s ]¤" % (e.hour, e.minute, e.second))
    print ('\t')
    
def mundur (waktujeda):#hitungan waktu mundur 
    while waktujeda:
        mins, secs = divmod(waktujeda, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\t','\t','WAKTU = ','( ',timer,' )', end="\r")
        time.sleep(1)
        waktujeda -= 1
    
def game_np32():# sicbo numpy 32-bit
   for i in range (main) :
        a = np.random.randint(1,6,size=3, dtype=np.int32) # random
        b = np.sum(a) #hasil random
        logo ()
        batasAtas()
        print ('\t','  [ PREDIKSI DADU KE ]','\n','\t','\t',f" [ {i} ]",'\n') 
        waktu()
        print ('\t','MULAI :','\b')
        print ('\t','~~~~~~~')
        print('\t','hasilnya adalah = ',a)
        print('\t','total = ','(',b,')')
    
        if b <= 10:
         print ('\t','katagori = ( KECIL )','\n')
         
        elif b >= 11:
         print ('\t','katagori = ( BESAR )','\n')
         
        batasBawah()
        mundur(waktujeda)
        print ('\n')
        
# memulai program 
print ('~~ selamat datang di prediksi roll dadu sicbo ~~')
print ('\n')
main = int (input(' berapa kali prediksi : '))
waktujeda = int (input(' jeda waktu : '))
print ('\t','[••• mulai prediksi •••]','\n')

while True:
       bermain = input (' [sudah siap]  \n (y).mulai / (n).stop \n (y/n) : ')
       if bermain == 'y' :
         game_np32()
       if bermain == 'n' :
         print ('prediksi selesai  \n [TERIMAKASIH] ')
         break
         
   
             