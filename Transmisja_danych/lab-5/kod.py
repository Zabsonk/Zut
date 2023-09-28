import math as m
import matplotlib.pyplot as plt
import numpy as np
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

    print('\nSzerokoœæ B3' ':', int(fmax3 - fmin3))
    print('Szerokoœæ B6'  ':', int(fmax6 - fmin6))
    print('Szerokoœæ B12 '  ':', int(fmax12 - fmin12))
def sygnal_bit(sig):
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
    
    
    
text=list(input('podaj tekst:'))


byte=[]
for i in text:
    if 127>=ord(i)>=32:
        byte.append(bin(ord(i)))
    else:
        print('bl¹d')

rem=[s[2:]for s in byte]

str1=''
for el in rem:
    str1+=el
    
print(str1[0:10])




#zad2

tc=1 #czas trwania sygnalu
tb=tc/len(str1)#czas trwania poj bitu
w=2#docelowa czestotliwosc
fn=w*tb**-1#czestotliwosc nosna
a1=1
a2=9
fn1=(w+0)/tb
fn2=(w+4)/tb
fs=10000#=2*max(fn,fm) czestotliwosc probkowania
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
    if b<=N:
        a=b+1
        b=b+c

plt.plot(x,za)
plt.show()
plt.plot(x,zp)
plt.show()
plt.plot(x,zf)
plt.show()


#x(t)

n=len(za)

sin=np.zeros(n)
sin2=np.zeros(n)
sin3=np.zeros(n)
z1=np.zeros(n)
z2=np.zeros(n)

for i in range(n):
    t=i*ts
    sin[i]=a1*m.sin(2*m.pi*fn*t)
    sin2[i]=a1*m.sin(2*m.pi*fn1*t)
    sin3[i]=a1*m.sin(2*m.pi*fn2*t)
    
    za[i]=za[i]*sin[i]
    zp[i]=zp[i]*sin[i]
    z1[i]=zf[i]*sin2[i]
    z2[i]=zf[i]*sin3[i]

plt.plot(x, za, 'red')
plt.title('ASK')
plt.show()

plt.plot(x, zp, 'green')
plt.title('PSK')
plt.show()

plt.plot(x, z1, 'blue')
plt.title('FSK')
plt.show()

plt.plot(x, z2, 'blue')
plt.title('FSK')
plt.show()

#p(t)

a=0
b=n//10
c=b-a

zap=np.zeros(len(x))
zpp=np.zeros(len(x))
zfp=np.zeros(len(x))
zfp2=np.zeros(len(x))
zfp3=np.zeros(len(x))


for i in range(10):
    for j in range(a,b):
        zap[j]=sum(za[a:j])
        zpp[j]=sum(zp[a:j])
        
        zfp2[j]=sum(z1[a:j])
        zfp3[j]=sum(z2[a:j])
        zfp[j]=-zfp2[j]+zfp3[j]
    if b<=n:
        a=b+1
        b=b+c

plt.plot(x, zap)
plt.title('ASK')
plt.show()

plt.plot(x, zpp)
plt.title('PSK')
plt.show()

plt.plot(x, zfp2)
plt.title('FSK1')
plt.show()

plt.plot(x, zfp3)
plt.title('FSK2')
plt.show()

#c(t)

zac = np.zeros(len(x))
zpc = np.zeros(len(x))
zfc = np.zeros(len(x))

a = 0
b = n // 10
c = b - a

h = max(zap) // 3

for i in range(10):
    zap1 = []
    zap0 = []
    zpp1 = []
    zpp0 = []
    zfp1 = []
    zfp0 = []

    for j in range(a, b):
        if zap[j] > h:
            zap1.append(j)
        elif zap[j] < h:
            zap0.append(j)
        
        
        if zpp[j] < 0:
            zpp1.append(j)
        elif zpp[j] > 0:
            zpp0.append(j)
        
        
        if zfp[j] > 0:
            zfp1.append(j)
        elif zfp[j] < 0:
            zfp0.append(j)
    
    
    if len(zap1) > len(zap0):
        zac[a:b + 1] = 1
    elif len(zap1) < len(zap0):
        zac[a:b + 1] = 0

    
    if len(zpp1) > len(zpp0):
        zpc[a:b + 1] = 1
    elif len(zpp1) < len(zpp0):
        zpc[a:b + 1] = 0

  
    if len(zfp1) > len(zfp0):
        zfc[a:b + 1] = 1
    elif len(zfp1) < len(zfp0):
        zfc[a:b + 1] = 0

    if b <= n:
        a = b + 1
        b=b+c


plt.plot(x, zac)
plt.title('ASK')
plt.show()

plt.plot(x, zpc)
plt.title('PSK')
plt.show()

plt.plot(x, zfc)
plt.title('FSK')
plt.show()


print(sygnal_bit(zac))
print(sygnal_bit(zpc))
print(sygnal_bit(zfc))