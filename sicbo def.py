from random import randint
from time import sleep
from datetime import datetime

print ('selamat datang di permainan roll dadu tanpa batas ')
print ('\t','[••• silahkan bermain •••]','\n')
         
main = int (input(' Berapakali ingin bermain = '))
wjd = int(input (' waktu jeda [ menit : detik ] = '))

def logo ():#logo pertama
    print ('\t',' ---------------------')
    print ('\t','|  {••••BERMAIN••••}  |')
    print ('\t',' ---------------------',)
    print ('\t','  [ PUTARAN DADU KE ]','\n','\t','\t',f" [ {i} ]",'\n')

def game (): # game rool dic
    a = randint (1,6 )
    b = randint (1,6 )
    c = randint (1,6 )
   
    hasil =int (a + b +c)
    
    print('\t','hasilnya adalah =','{',a,',',b,',',c,'}')
    print('\t','total = ','(',hasil,')')
    
    if hasil <= 10:
         print ('\t','katagori = ( KECIL )','\n')
         
    elif hasil >= 11:
         print ('\t','katagori = ( BESAR )','\n')
         
def game1 () :
          d = randint ( 3,18 ) #angka random
          hasil1 = d
          print ('\t','hasil 1 =',d)
          
          if hasil1 <= 10:
           print ('\t','katagori1 = ( KECIL )','\n')
          
          elif hasil1 >= 11:
           print ('\t','katagori1 = ( BESAR )','\n')
         
def mundur (wjd):# waktu mundur 
    while wjd:
        mins, secs = divmod(wjd, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\t','WAKTU = ','( ',timer,' )', end="\r")
        sleep(1)
        wjd -= 1

def waktu (): #info waktu
    e=datetime.now()
    print ('\t',"¤[ tanggal/bulan/tahun  = %s/%s/%s ]¤" % (e.day, e.month, e.year))
    print ('\t',"¤[ jam : menit : detik = %s:%s:%s ]¤" % (e.hour, e.minute, e.second))
    
def batas ():#batas bawah
    print('\t','=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=+×+=','\t')
    print('\t')
    print('\t')
    
for i in range (main):
    logo ()
    game ()
    game1()
    mundur (wjd)
    waktu ()
    batas ()
    