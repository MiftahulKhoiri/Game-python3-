from random import randint
from time import sleep 

print ('selamat datang di permainan roll dadu tanpa batas ')
print ('\t','[••• silahkan bermain •••]','\n')
         
main = int (input('Masuk kan nilai berapakali ingin bermain = '))
t = int(input ('jeda waktu = '))

def sc (): # rool dic
    a = randint (1,6 )
    b = randint (1,6 )
    c = randint (1,6 )
    hasil =int (a + b +c)
    print('\t','hasilnya adalah =','{',a,',',b,',',c,'}')
    print('\t','total = ',hasil)
    
    if hasil <= 10:
         print ('\t','katagori : ( KECIL )','\n')
         
    elif hasil >= 11:
         print ('\t','katagori : ( BESAR )','\n') 
         
def mundur(t):# waktu mundur 
    while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\t','WAKTU : ','( ',timer,' )', end="\r")
        sleep(1)
        t -= 1

def waktu(): #info waktu
    e=datetime.now()
    print ('\t',"¤[ hari tanggal tahun:  = %s/%s/%s ]¤" % (e.day, e.month, e.year))
    print ('\t',"¤[ waktu sekarang: = %s:%s:%s ]¤" % (e.hour, e.minute, e.second))
    print('\t')


for i in range (main):
    print ('\t','---------------------')
    print ('\t','| {••••BERMAIN••••} |')
    print ('\t','---------------------','\n')
    print ('\t',f"putaran dadu ke = {i}")
    sc()
    mundur(t)
    waktu()
    