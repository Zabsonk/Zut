import math as m
import matplotlib.pyplot as plt
Tc=1.0 #czas trwania sygna³u
fs=10000 #czêstotliwoœæ
N=int(Tc*fs) #liczba probek

Ts=1/fs

f=4000
o=10
osx=[]
osy=[]
#tabela 3 przyklad 6


for n in range(0,N):
    t=n*Ts
    osx.append(t)
   
def funkcja(t):
    if(1.8>t>=0):
        x=(-t/2)*m.sin((20*t**3)-(18*t**2))
    elif(3>t>=1.8):
        x=m.cos(5*m.pi*t)*m.sin(12*m.pi*t**2)
    elif(4.5>t>=3):
        x=((t-3)/3)*m.sin((12-t)*m.pi*t**2)
    return x

#zad4 
for n in range(0,len(osx)):
    osy.append(funkcja(osx[n]))

plt.title('Wykres zad 3 funckja numer 6')
plt.plot(osx,osy)
plt.show()