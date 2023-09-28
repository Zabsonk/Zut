import math as m
import matplotlib.pyplot as plt
Tc=1.0 #czas trwania sygna³u
fs=22050 #czêstotliwoœæ
N=int(Tc*fs) #liczba probek

Ts=1/fs

f=11025
osx=[]
osy=[]
osy2=[]
osy3=[]
def fun1(t):
    b1=0
    for h in range(1,2):
        b1=b1+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b1
def fun2(t):
    b2=0
    for h in range(1,5):
        b2=b2+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b2

def fun3(t):
    b3=0
    for h in range(1,25):
        b3=b3+((m.sin(m.sin(m.pi*h/7*t)*m.pi*t*h))/((2*h**2)+1))
    return b3
#tabela 4 punkt numer 2
for n in range(0,N):
    t=n*Ts
    osx.append(t)
    
for n in range(0,len(osx)):
    osy.append(fun1(osx[n]))
    osy2.append(fun2(osx[n]))
    osy3.append(fun3(osx[n]))


plt.title("zad4 wykres b1(t)")
plt.plot(osx,osy)
plt.show()

plt.title("zad4 wykres b2(t)")
plt.plot(osx,osy2)
plt.show()

plt.title("zad4 wykres b3(t)")
plt.plot(osx,osy3)
plt.show()