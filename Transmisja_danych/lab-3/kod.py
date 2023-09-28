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

def widmo(re,im):
    M=[]
    Mprim=[]
    fk=[]
    for k in range(N//2):

        
        M.append(m.sqrt(re[k]**2+im[k]**2))
        Mprim.append(10*m.log(M[k],10))
        fk.append(k*(fs/N))
    return Mprim,fk

tc=1
fn=1000
fs=5000#=2*max(fn,fm)
ts=1/fs
fm=20
N=int(tc*fs) #liczba probek



vector=[]

for k in range(N):
    t=k*ts
    vector.append(m.sin(2*m.pi*fm*t))
    
    
za=[]
zp=[]
zf=[]
k='c'

if k=='a':
    ka=0.5
    kp=0.4
    kf=0.8
if k=='b':
    ka=6
    kp=3
    kf=3
if k=='c':
    ka=21
    kp=10
    kf=10
        

for i in range(N):

    za.append((ka*vector[i]+1)*m.cos(2*m.pi*fn*t))
    zp.append(m.cos(2*m.pi*fn*t+kp*vector[i]))
    zf.append(m.cos(2*m.pi*fn*t+(kf/fm)*vector[i]))
    

#plt.plot(fk,vector)
#plt.show()

#zad2

re,im=dft(za)
re2,im2=dft(zp)
re3,im3=dft(zf)



Mprim,fk=widmo(re,im)
Mprim2,fk2=widmo(re2,im2)
Mprim3,fk3=widmo(re3,im3)


    
plt.plot(fk,Mprim)
plt.xscale('log')
plt.show()
plt.plot(fk2,Mprim2)
plt.xscale('log')
plt.show()
plt.plot(fk3,Mprim3)
plt.xscale('log')
plt.show()



#zad3
fmin=500
fmax=1000
maxv=None
minv=None

for i in range (fmax):
    if (maxv == None):
        maxv = Mprim[i]
    if (minv == None):
        minv = Mprim[i]
    if (Mprim[i] < minv):
        minv = Mprim[i]
    if (Mprim[i] > maxv):
        maxv = Mprim[i]

print(maxv)
print(minv)
print(maxv-minv)