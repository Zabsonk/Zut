import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

def modulacja_zf(zakodowany):
    zf=[]
    a=0
    b=N//len(zakodowany)
    c=b-a
    for l in range(B):
        for i in range(a,b):
            t=i*ts
            
            if zakodowany[l]==1:
                zf.append(m.sin(2*m.pi*fn2*t))
                
            if zakodowany[l]==0:
                zf.append(m.sin(2*m.pi*fn1*t))
        if b<=N:
            a=b+1
            b=b+c

    return zf
def modulacja_za(zakodowany):
    za=[]
    a=0
    b=N//len(zakodowany)
    c=b-a
    for l in range(B):
        for i in range(a,b):
            t=i*ts
            
            if zakodowany[l]==1:
                za.append(a1*m.sin(2*m.pi*fn*t))
                
            if zakodowany[l]==0:
                za.append(a2*m.sin(2*m.pi*fn*t))
        if b<=N:
            a=b+1
            b=b+c

    return za
def modulacja_zp(zakodowany):
    zp=[]
    a=0
    b=N//len(zakodowany)
    c=b-a
    for l in range(B):
        for i in range(a,b):
            t=i*ts
            
            if zakodowany[l]==1:
                zp.append(m.sin(2*m.pi*fn*t+m.pi))
                
            if zakodowany[l]==0:
                zp.append(m.sin(2*m.pi*fn*t))
        if b<=N:
            a=b+1
            b=b+c

    return zp

def sygnal_bit(sig):
    t=[]
    n=len(sig)
    a=0
    b=n//B
    c=b-a
    
    for i in range(B):
        jedynki=0
        zera=0
        for j in range(a,b):
            if sig[j]==1:
                jedynki+=1
            elif sig[j]==0:
                zera+=1
        if jedynki>zera:
            t.append(1)
        elif zera>jedynki:
            t.append(0)  
        if b<=n:
            a=b+1
            b=b+c   
    return t


def demodulacja_za(za):
    #x(t)
    n=len(za)
    sin=np.zeros(n)
    for i in range(n):
        t=i*ts
        sin[i]=a1*m.sin(2*m.pi*fn*t)
        za[i]=za[i]*sin[i]
        
    #p(t)
    a=0
    b=n//B
    c=b-a
    
    zap=np.zeros(n)
    
    
    for i in range(B):
        for j in range(a,b):
            zap[j]=sum(za[a:j]) 
        if b<=n:
            a=b+1
            b=b+c
    
    #c(t)
    zac=np.zeros(n)
    a=0
    b=n//B
    c=b-a
   
    h=max(zap)//3
    for i in range(B):
        zap1 = []
        zap0 = []
        for j in range(a, b):
           if zap[j] > h:
               zap1.append(j)
           elif zap[j] < h:
               zap0.append(j)
               
        if len(zap1) > len(zap0):
            zac[a:b + 1] = 1
        elif len(zap1) < len(zap0):
            zac[a:b + 1] = 0
        if b <= n:
            a = b + 1
            b=b+c
            
    
    wyjscie=sygnal_bit(zac)
    return wyjscie


def demodulacja_zp(zp):
    #x(t)
    n=len(zp)
    sin=np.zeros(n)
    for i in range(n):
        t=i*ts
        sin[i]=a1*m.sin(2*m.pi*fn*t)
        zp[i]=zp[i]*sin[i]
        
    #p(t)
    a=0
    b=n//B
    c=b-a
    
    zpp=np.zeros(n)
    
    
    for i in range(B):
        for j in range(a,b):
            zpp[j]=sum(zp[a:j]) 
        if b<=n:
            a=b+1
            b=b+c
    
    #c(t)
    zpc=np.zeros(n)
    a=0
    b=n//B
    c=b-a
   
    h=max(zpp)//3
    for i in range(B):
        zpp1 = []
        zpp0 = []
        for j in range(a, b):
           if zpp[j] > h:
               zpp1.append(j)
           elif zpp[j] < h:
               zpp0.append(j)
               
        if len(zpp1) > len(zpp0):
            zpc[a:b + 1] = 1
        elif len(zpp1) < len(zpp0):
            zpc[a:b + 1] = 0
        if b <= n:
            a = b + 1
            b=b+c
            
    
    wyjscie=sygnal_bit(zpc)
    return wyjscie            
 

def demodulacja_zf(zf):
    #x(t)
    n=len(zf)
    sin1=np.zeros(n)
    sin2=np.zeros(n)
    z1=np.zeros(n)
    z2=np.zeros(n)
    
    for i in range(n):
        t=i*ts
        sin1[i]=a1*m.sin(2*m.pi*fn1*t)
        sin2[i]=a1*m.sin(2*m.pi*fn2*t)
        z1[i]=zf[i]*sin1[i]
        z2[i]=zf[i]*sin2[i]

        
    #p(t)
    a=0
    b=n//B
    c=b-a
    
    zfp=np.zeros(n)
    zfp2=np.zeros(n)
    zfp3=np.zeros(n)
    
    for i in range(B):
        for j in range(a,b):
            zfp2[j]=sum(z1[a:j])
            zfp3[j]=sum(z2[a:j])
            zfp[j]=-zfp2[j]+zfp3[j]
        if b<=n:
            a=b+1
            b=b+c
    
    #c(t)
    zfc=np.zeros(n)
    a=0
    b=n//B
    c=b-a
   
    h=max(zfp)//3
    for i in range(B):
        zfp1 = []
        zfp0 = []
        for j in range(a, b):
           if zfp[j] > h:
               zfp1.append(j)
           elif zfp[j] < h:
               zfp0.append(j)
               
        if len(zfp1) > len(zfp0):
            zfc[a:b + 1] = 1
        elif len(zfp1) < len(zfp0):
            zfc[a:b + 1] = 0
        if b <= n:
            a = b + 1
            b=b+c
            
    
    wyjscie=sygnal_bit(zfc)
    return wyjscie       

      
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
    
    generuj¹ca=np.hstack((parzyste,jednostkowa))
    c=np.dot(bit,generuj¹ca)%2
    c=c.astype('int').tolist()
    return c,parzyste


def generuj_bialy_szum(dlugosc):
    samples = np.random.normal(0, 1, size=dlugosc)
    samples = samples / max(samples)  # normalizacja do [-1, 1]
    return samples



def tlum(kod):
    n=np.zeros(len(kod))
    for i in range(len(n)):
        t=i*ts
        n[i]=m.exp(-beta*t)
    for i in range(len(kod)):
        for j in range(len(kod[i])):
            kod[i][j]=kod[i][j]*n[i]
    return kod



def dekoder(P,c):

    I = np.eye(4)
    H = np.concatenate((I, P.T),axis=1)
    s = np.dot(c,H.T)%2
    S = int(s[0]*1+s[1]*2+s[2]*4+s[3]*8)
    
    indeksy_bity = {1: 0, 2: 1, 3: 4, 4: 2, 5: 5, 6: 6, 7: 7, 8: 3, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14}
    if S != 0:
        naprawa = indeksy_bity[S]
        c[naprawa] = (c[naprawa] + 1) % 2
    
    return c[4:]
   

def BER(wejscie,wyjscie):
    E = np.sum(wejscie != wyjscie)
    N = len(wejscie)  
    BER =round( E / N,6)
    return BER
#######################################################

   
beta=10

alfa=1
B=15   
    
wejscie=[1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1]

tc=1 #czas trwania sygnalu

fn=200#czestotliwosc nosna
fs=40000#=2*max(fn,fm) czestotliwosc probkowania
ts=1/fs #okres peobkowania
N=int(tc*fs)
a1=1
a2=0.5
w=1
tb=tc/len(wejscie)
fn1=(w+0)/tb
fn2=(w+4)/tb

#####################################################
podzielone_tablice = [wejscie[i:i+11] for i in range(0, len(wejscie), 11)]



nadmiarowy0,p0=koder(podzielone_tablice[0],15)

nadmiarowy1,p1=koder(podzielone_tablice[1],15)

nadmiarowy2,p2=koder(podzielone_tablice[2],15)

nadmiarowy3,p3=koder(podzielone_tablice[3],15)



do_modulacji=[]
do_modulacji.append(nadmiarowy0)
do_modulacji.append(nadmiarowy1)
do_modulacji.append(nadmiarowy2)
do_modulacji.append(nadmiarowy3)

#print("do modulacji:",do_modulacji)
###################################



wybor_modulacji=3 #1 - ask 2 - psk 3 - fsk
wybor_modyfikacji=2# 1 szum -> tlum | 2- tlum -> szum



###########################


petla=len(do_modulacji)

zmodulowany_z=[]


#modulacja
if wybor_modulacji==1:     
    for i in range(petla):       
        zmodulowany_z.append(modulacja_za(do_modulacji[i]))  
if wybor_modulacji==2:  
    for i in range(petla):       
        zmodulowany_z.append(modulacja_zp(do_modulacji[i]))     
if wybor_modulacji==3:  
    for i in range(petla):       
        zmodulowany_z.append(modulacja_zf(do_modulacji[i]))          
        
#modyfikacje
if wybor_modyfikacji==1:          
    for i in range(petla):
        szum=generuj_bialy_szum(len(zmodulowany_z[i]))
        zmodulowany_z[i]=zmodulowany_z[i]+alfa*szum  
    zmodulowany_z=tlum(zmodulowany_z)


if wybor_modyfikacji==2:
    zmodulowany_z=tlum(zmodulowany_z)          
    for i in range(petla):
        szum=generuj_bialy_szum(len(zmodulowany_z[i]))
        zmodulowany_z[i]=zmodulowany_z[i]+alfa*szum  
    


#demodulacja
zdemodulowany_z=[]
if wybor_modulacji==1:
    for i in range(petla):
        zdemodulowany_z.append(demodulacja_za(zmodulowany_z[i]))
if wybor_modulacji==2:
    for i in range(petla):
        zdemodulowany_z.append(demodulacja_zp(zmodulowany_z[i]))
if wybor_modulacji==3:
    for i in range(petla):
        zdemodulowany_z.append(demodulacja_zf(zmodulowany_z[i]))


#print("dlugosc domodulacji",len(do_modulacji))
#print("dlugosc zmodulowanego",len(zmodulowany_z))
#print("dlugosc zdemodulowanego;",len(zdemodulowany_z))
#print("zdemodulowany_za:",zdemodulowany_z)





wyjscie=[]
for i in range(petla):
    wyjscie.append(dekoder(p0, zdemodulowany_z[i]))




print("wejscie",wejscie)
print("wyjscie",wyjscie)

print("BER:", BER(wejscie,wyjscie))
