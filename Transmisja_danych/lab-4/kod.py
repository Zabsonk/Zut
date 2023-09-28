import math as m
import matplotlib.pyplot as plt
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
def widmo(re,im):
    M=[]
    Mprim=[]
    fk=[]
    for k in range(len(x)//2):

        
        M.append(m.sqrt(re[k]**2+im[k]**2))
        Mprim.append(10*m.log(M[k],10))
        fk.append(k*(fs/N))
    
    

    return Mprim,fk
        
def szerokosc_pasma(Mprim,fk) :
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

text=list(input('podaj tekst:'))


byte=[]
for i in text:
    if 127>=ord(i)>=32:
        byte.append(bin(ord(i)))
    else:
        print('bląd')

rem=[s[2:]for s in byte]
print(rem)
str1=''
for el in rem:
    str1+=el
    
print(str1)
#zad2

tc=1 #czas trwania sygnalu
tb=1/10#czas trwania poj bitu
w=2#docelowa czestotliwosc
fn=w*tb**-1#czestotliwosc nosna
a1=1
a2=8
fn1=(w+1)/tb
fn2=(w+2)/tb
fs=4000#=2*max(fn,fm) czestotliwosc probkowania
ts=1/fs #okres peobkowania
N=int(tc*fs)

x=[]
za=[]
zp=[]
zf=[]
a=0
b=N//len(str1)
c=b-a
for l in range(10):
    for i in range(a,b):
        t=i*ts
        x.append(t)
        if str1[l]=='0':
            za.append(a1*m.sin(2*m.pi*fn*t))
            zp.append(m.sin(2*m.pi*fn*t))
            zf.append(m.sin(2*m.pi*fn1*t))
        if str1[l]=='1':
            za.append(a2*m.sin(2*m.pi*fn*t))
            zp.append(m.sin(2*m.pi*fn*t+m.pi))
            zf.append(m.sin(2*m.pi*fn2*t))
    if b<N:
        a=b+1
        b=b+c
print(za)
plt.plot(x,za)
plt.show()
plt.plot(x,zp)
plt.show()
plt.plot(x,zf)
plt.show()

re,im=dft(za)
re2,im2=dft(zp)
re3,im3=dft(zf)


Mprim,fk=widmo(re,im)
Mprim2,fk2=widmo(re2,im2)
Mprim3,fk3=widmo(re3,im3)


plt.plot(fk,Mprim)

plt.show()
plt.plot(fk2,Mprim2)

plt.show()
plt.plot(fk3,Mprim3)
plt.show()

szerokosc_pasma(fk,Mprim)
szerokosc_pasma(fk2,Mprim2)
szerokosc_pasma(fk3,Mprim3)