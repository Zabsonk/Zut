import pygame as pg
from abc import ABC, abstractmethod
class Gracz(ABC):
    def __init__(self,gra):
        #przekazanie obiektu gry 
        self.gra=gra
       
        #ustawienie zyc i predkosci dla kazdego gracza
        self.predkoscy=10
        self.zycia=3

    @abstractmethod
    def kolor(self):
        pass
    @abstractmethod
    def ruch(self):
        pass
    @abstractmethod
    def polozenie(self):
        pass

    def tworzenie(self):
        #rysowanie kazdej z tarczy
        pg.draw.rect(self.gra.okno,self.kolor(),self.polozenie())

class Gracz1(Gracz):
    def __init__(self,gra):
        #przekazanie elementów klasy głównej(predkosc,zycia)
        super().__init__(gra)

       #pozycja gracza nr1
        self.g1=pg.Rect(10,250,10,160)

    def kolor(self):
        return (242,85,96)
    def polozenie(self):
        return self.g1
    def ruch(self):
        #sterowanie poprzez sprawdzanie naciśniętego przycisku
        if pg.key.get_pressed()[pg.K_s]:
           self.g1.y+=self.predkoscy
        if pg.key.get_pressed()[pg.K_w]:
           self.g1.y-=self.predkoscy

        #blokada jesli uderzy w sciane
        if self.g1.top<=0:
            self.g1.top=0
        if self.g1.bottom>=740:
            self.g1.bottom=740

class Gracz2(Gracz):
    def __init__(self,gra):
        #przekazanie elementów klasy głównej(predkosc,zycia)
        super().__init__(gra)

        #pozycja gracza nr1
        self.g2=pg.Rect(1220,250,10,160)

    def kolor(self):
        return (255,165,0)
    def polozenie(self):
        return self.g2
    def ruch(self):
        #sterowanie poprzez sprawdzanie naciśniętego przycisku
        if pg.key.get_pressed()[pg.K_DOWN]:
           self.g2.y+=self.predkoscy
        if pg.key.get_pressed()[pg.K_UP]:
           self.g2.y-=self.predkoscy
        #blokada jesli uderzy w sciane
        if self.g2.top<=0:
            self.g2.top=0
        if self.g2.bottom>=740:
            self.g2.bottom=740