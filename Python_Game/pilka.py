import pygame as pg
import class1
from numpy import random
class Pilka():
    def __init__(self,gra):
        #przekazanie obiektu gry
        self.gra=gra
        
        #stworzenie wymiarów i pozycji pilki
        self.pilka=pg.Rect(720,360,20,20)

        #ustawienie predkosci pilki
        self.predkoscx=10
        self.predkoscy=10

    def ruch(self):
        #poruszanie pilki
        self.pilka.x+=self.predkoscx
        self.pilka.y+=self.predkoscy

        #zamiana kierunki jesli uderzy w sciane
        if self.pilka.top<=0 or self.pilka.bottom>=720:
            self.predkoscy*=-1

        #gdy pilka wleci na sciane gracza zmiejszenie zyc oraz ustawienie pilki na srodku
        if self.pilka.right>=1240:
            self.pilka=pg.Rect(720,360,20,20)

            #losowanie kierunku po straceniu życia
            self.predkoscy*=random.choice([1,-1])
            self.predkoscx*=random.choice([1,-1])
            self.gra.gracz2.zycia-=1

         #gdy pilka wleci na sciane gracza zmiejszenie zyc oraz ustawienie pilki na srodku
        if self.pilka.left<=0:
            self.pilka=pg.Rect(720,360,20,20)

            #losowanie kierunku po straceniu życia
            self.predkoscy*=random.choice((1,-1))
            self.predkoscx*=random.choice([1,-1])
            self.gra.gracz1.zycia-=1

       

        #odbijanie od tarczy
        if self.pilka.colliderect(self.gra.gracz1.g1) or self.pilka.colliderect(self.gra.gracz2.g2):
            self.predkoscx*=-1
       
                
    def tworzenie(self):
        #rysowanie pilki
        pg.draw.ellipse(self.gra.okno,(0,150,255),self.pilka)
