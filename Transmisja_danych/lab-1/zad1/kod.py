import math as m
import matplotlib.pyplot as plt
Tc=1 #czas trwania sygnału
fs=10000 #częstotliwość
N=int(Tc*fs) #liczba probek

Ts=1/fs

f=2
o=10
osx=[]
osy=[]

#funkcja numer 5
for n in range(0,N):
    t=n*Ts
    osx.append(t)
    x=m.sin(2*m.pi*f*t*m.cos(3*m.pi*t)+t*o)
    osy.append(x)

plt.title('Wykres zad 1 funckja numer 5')
plt.plot(osx,osy)
plt.show()