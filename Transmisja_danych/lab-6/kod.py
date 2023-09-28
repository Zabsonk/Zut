import math as m
import matplotlib.pyplot as plt
import numpy as np
import random

def negacja(liczba,index):
    if liczba[index]==0:
        liczba[index]=1
    elif liczba[index]==1:
        liczba[index]=0
    return liczba
def dft(x):
    N=len(x)
    ximvector=[]
    xrevector=[]
    for k in range(0,N):
        xim=0
        xre=0
        for n in range(0,N):
            xre+=x[n]*m.cos((-2*m.pi*n*k)/N)
            xim+=x[n]*m.sin((-2*m.pi*n*k)/N)
        xrevector.append(xre)    
        ximvector.append(xim)    
    return xrevector,ximvector
def widmo(re,im,x):
    M=[]
    Mprim=[]
    fk=[]
    for k in range(len(x)//2):

        
        M.append(m.sqrt(re[k]**2+im[k]**2))
        Mprim.append(10*m.log(M[k],10))
        fk.append(k*(fs/N))
    
    

    return Mprim,fk
        
def szerokosc_pasma(Mprim,fk,x) :
    szer=max(Mprim)
    d3=szer-3
    d6=szer-6
    d12=szer-12
    fmin3,fmin6,fmin12=0,0,0
    fmax3,fmax6,fmax12=0,0,0
    
    for k in range(len(x)//2):
        if Mprim[k-1]<=d3<=Mprim[k]:
            fmin3=fk[k]
            break
    for k in range(len(x) // 2):
        if Mprim[k - 1] <= d6 <= Mprim[k]:
            fmin6 = fk[k]
            break
    for k in range(len(x) // 2):
        if Mprim[k - 1] <= d12 <= Mprim[k]:
            fmin12 = fk[k]
            break

    for k in reversed(range(len(x) // 2)):
        if Mprim[k] >= d3 >= Mprim[k - 1]:
            fmax3 = fk[k]
            break
    for k in reversed(range(len(x) // 2)):
        if Mprim[k] >= d6 >= Mprim[k - 1]:
            fmax6 = fk[k]
            break
    for k in reversed(range(len(x) // 2)):
        if Mprim[k] >= d12 >= Mprim[k - 1]:
            fmax12 = fk[k]
            break

    print('\nSzerokość B3' ':', int(fmax3 - fmin3))
    print('Szerokość B6'  ':', int(fmax6 - fmin6))
    print('Szerokość B12 '  ':', int(fmax12 - fmin12))
def sygnal_bit(sig,n):
    text=[]
    a=0
    b=n//10
    c=b-a
    
    for i in range(10):
        jedynki=0
        zera=0
        for j in range(a,b):
            if sig[j]==1:
                jedynki+=1
            elif sig[j]==0:
                zera+=1
        if jedynki>zera:
            text.append('1')
        elif zera>jedynki:
            text.append('0')  
        if b<=n:
            a=b+1
            b=b+c   
    return text
def asci_bit(x):
    byte=[]
    for i in x:
        if 127>=ord(i)>=32:
            byte.append(bin(ord(i)))
        else:
            print('bląd')

    rem=[s[2:]for s in byte]

    str1=''
    for el in rem:
        str1+=el
    return str1

def num_to_bit(num):  
    bin_num = format(num, '04b')
    return bin_num

def koder(bit,n):
    k=len(bit)
    m=n-k
    
    
    jednostkowa=np.identity(k)
    bity=np.zeros([n,m])
    for i in range(n):
        for j in range(m):
            bity[i,j]=num_to_bit(i+1)[j]
            
            
    bity=np.delete(bity,0, axis=0)
    bity=np.delete(bity,0, axis=0)
    bity=np.delete(bity,1, axis=0)
    bity=np.delete(bity,4, axis=0)
    
    parzyste=np.zeros([k,m])
    parzyste[:,0]=bity[:,3]
    parzyste[:,1]=bity[:,2]
    parzyste[:,2]=bity[:,1]
    parzyste[:,3]=bity[:,0]
    
    generująca=np.hstack((parzyste,jednostkowa))
    c=np.dot(bit,generująca)%2
    c=c.astype('int').tolist()
    return c,parzyste
def dekoder(kod,n,k,P):

    jednostkowa = np.identity(n - k)
    H = np.hstack((jednostkowa, np.transpose(P)))
    s = np.dot(kod, np.transpose(H)) % 2 
    s = s.astype('int').tolist()

    S = int(s[0] * 2 ** 0 + s[1] * 2 ** 1 + s[2] * 2 ** 2 + s[3] * 2 ** 3) 
    if S == 0:
        print('nie ma bledow')
    else:
        print('blad na bicie: x' + str(S))
        if S == 4:
            kod[2] ^= 1
        elif S == 8:
            kod[3] ^= 1
        elif S == 3:
            kod[4] ^= 1
        elif S == 5:
            kod[5] ^= 1
        elif S == 6:
            kod[6] ^= 1
        elif S == 7:
            kod[7] ^= 1
        else:
            kod[S - 1] ^= 1

    kod = kod[4:]
    print('wyjscie: ' + str(kod))


bit=[1,1,0,1]

print('Wejscie:',bit)
kod=[]
print(kod)


x3=int(bit[0])
x5=int(bit[1])
x6=int(bit[2])
x7=int(bit[3])

x1=((x3+x5)%2+x7)%2
x2=((x3+x6)%2+x7)%2
x4=((x5+x6)%2+x7)%2


kod.insert(0,((x3+x5)%2+x7)%2)
kod.insert(1,((x3+x6)%2+x7)%2)
kod.insert(2,x3)
kod.insert(3,((x5+x6)%2+x7)%2)
kod.insert(4,x5)
kod.insert(5,x6)
kod.insert(6,x7)

print('kod na wejsciu',kod)


#detekcja z błędem
x1=((x3+x5)%2+x7)%2
x2=((x3+x6)%2+x7)%2
x4=((x5+x6)%2+x7)%2


x1n=(kod[0]+x1)%2
x2n=(kod[1]+x2)%2
x4n=(kod[3]+x4)%2

los=random.randint(1, 7)-1

print('indeks do zanegowania:',los)

negacja(kod, los)


x1p=((kod[2]+kod[4])%2+kod[6])%2
x2p=((kod[2]+kod[5])%2+kod[6])%2
x4p=((kod[4]+kod[5])%2+kod[6])%2

x1n=(kod[0]+x1p)%2
x2n=(kod[1]+x2p)%2
x4n=(kod[3]+x4p)%2

print('kod po zanegowaniu', kod)

S=x1n*2**0+x2n*2**1+x4n*2**2
print('indeks z S:',S-1)


#dekodowanie
negacja(kod, los)


    
print('poprawienie kodu',kod)

#tablica do dekodowania
wyjscie=[]*4
w0=kod[2]
w1=kod[4]
w2=kod[5]
w3=kod[6]

wyjscie.append(w0)
wyjscie.append(w1)
wyjscie.append(w2)
wyjscie.append(w3)

print('wyjscie:',wyjscie)

bit2=[1,1,0,1,0,0,1,1,0,1,0]
print('przed kodowaniem :',bit2)
kod,P=koder(bit2,15)
dekoder(kod, 15,11, P)