import math as m
import matplotlib.pyplot as plt
Tc=1 #czas trwania sygna³u
fs=10000 #czêstotliwoœæ
N=int(Tc*fs) #liczba probek

Ts=1/fs

f=2
o=10
osx=[]
osy=[]
osz=[]
osv=[]
#tabela numer 1 wzor  5
#tabela numer 2 wzor 3
for n in range(0,N):
    t=n*Ts
    osx.append(t)
    x=m.sin(2*m.pi*f*t*m.cos(3*m.pi*t)+t*o)

    fy=(t**3-1)+m.cos(4*t**2*m.pi)*t
    osy.append(fy)

    fz=(x)/(m.fabs(fy*m.cos(5*t)-x*fy)+t)
    osz.append(fz)

    fv=(x*662)/(m.fabs(x-fy)+0.5)
    osv.append(fv)


plt.title('Zad2 wykres y(t)')
plt.plot(osx,osy)
plt.show()

plt.title('Zad2 wykres z(t)')
plt.plot(osx,osv)
plt.show()

plt.title('Zad2 wykres v(t)')
plt.plot(osx,osy)
plt.show()