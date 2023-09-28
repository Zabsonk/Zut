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
def funkcja_y(t,f):
    return (t**3-1)+m.cos(4*t**2*m.pi)*t


def funkcja_z(t,f):
    
    x=m.sin(2*m.pi*f*t*m.cos(3*m.pi*t)+t*o)
    
    fy=funkcja_y(t, f)
    return (x)/(m.fabs(fy*m.cos(5*t)-x*fy)+t)


def funkcja_v(t,f):
    x=m.sin(2*m.pi*f*t*m.cos(3*m.pi*t)+t*o)
    fy=funkcja_y(t, f)
    return (x*662)/(m.fabs(x-fy)+0.5)
def funkcja_u(t,f):
    if(1.8>t>=0):
       x=(-t/2)*m.sin((20*t**3)-(18*t**2))
    elif(3>t>=1.8):
       x=m.cos(5*m.pi*t)*m.sin(12*m.pi*t**2)
    elif(4.5>t>=3):
       x=((t-3)/3)*m.sin((12-t)*m.pi*t**2)
    return x
def funkcja_b1(t):
    b1=0
    for h in range(1,2):
        b1=b1+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b1
def funkcja_b2(t):
    b2=0
    for h in range(1,5):
        b2=b2+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b2

def funkcja_b3(t):
    b3=0
    for h in range(1,25):
        b3=b3+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b3



tc=1
fs=10000
N=int(tc*fs)
ts=1/fs
f=2
o=10
N=int(tc*fs) #liczba probek



vector=[]
for i in range(N):
    t=i*ts
    vector.append(funkcja_b3(t))
    
start1=time.time()
np.fft.fft(vector)
stop1=time.time()

czas=stop1-start1
print(czas)

M=[]
Mprim=[]
fk=[]
#for k in range(N//2):

    
 #   M.append(m.sqrt(re[k]**2+im[k]**2))
 #   Mprim.append(10*m.log(M[k],10))
 #   fk.append(k*(fs/len(vector)))
    
    
#plt.plot(fk,Mprim)
#plt.xscale('log')
#plt.show()
    
