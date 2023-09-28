import numpy as np
import math as m
import time 
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

def funkcja_x(t,f):
    return m.sin(2*m.pi*f*t*m.cos(3*m.pi*t)+t*o)


Tc=1
f=1000
o=10
fs=100
Ts=1/fs
N=int(Tc*fs) #liczba probek



vector=[]
for i in range(N):
    t=i*Ts
    vector.append(m.sin(2*f*t))
    


#print('wektor',vector)

#start=time.time()
#print(dft(vector))
stop=time.time()

czas1=stop-start

re,im=dft(vector)

#start2=time.time()
#print(np.fft.fft(vector))
#stop2=time.time()

#czas2=stop2-start2

print("DFT:")
print(czas1)

print("\nFFT:\n")
#print(czas2)  

M=[]
Mprim=[]
fk=[]
for k in range(N//2):
    
    M.append(m.sqrt(re[k]**2+im[k]**2))
    Mprim.append(10*m.log(M[k],10))
    fk.append(k*(fs/len(vector)))
    


plt.plot(fk,Mprim)

plt.show()

tc=1
fs=10000
N=int(tc*fs)
ts=1/fs
f=2
o=10


x3=[]
y3=[]

for n in range(N):
    x3.append(n/fs)
    
for n in range(N):
    y3.append(funkcja_x(x3[n],f))
dft(y3)
print("koniec")
