from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLineEdit
import pygame as pg
import sys
from gracz import *
from pilka import *

import time
import numpy as np
class Gra():
    def __init__(self):
        #inicjalizacja czcionki
        pg.font.init()

        pg.init()
        #wymiary okna
        self.width=1240
        self.height=720

        #tworzenie okna o podanych wymiarach
        self.okno=pg.display.set_mode((self.width,self.height))

        #zmienna która która w dalszej częsci przyjmie numer wygranego gracza
        self.wygrana=0

        
        #stworzenie 3 obiektów
        self.gracz1=Gracz1(self)
        self.gracz2=Gracz2(self)
        self.pilka=Pilka(self)

        #czas do pamiaru trwania meczu
        self.czas1=time.time()

        #Aby wykorzystać QT framework stworzyłem klase która tworzy okienko dialogowe
        #z zapytaniem czy napewno chcesz opuścić gre gdy naciśniemy "X" lub ESC
        class Exit(QWidget):
            def __init__(self):
                super().__init__()
                layout=QVBoxLayout()
                self.textBox=QLineEdit("Czy napewno chcesz wyjsc?")
                self.button=QPushButton("EXIT")
                self.button.clicked.connect(self.click)
                layout.addWidget(self.textBox)
                layout.addWidget(self.button)
                self.setLayout(layout)
                self.show()
            def click(self,text):
                sys.exit(0)
        
        #zapobieganie samozamykaniu się okna gry
        while True:
            #licznik FPS
            pg.time.Clock().tick(120)
            #zamknięcie okna tylko w momencie naciśniećia "X" na oknie lub klawiatrze
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    app=QApplication([])
                    nw=Exit()
                    app.exec_()
                    
                    
                elif event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE:
                    app=QApplication([])
                    nw=Exit()
                    app.exec_()
                    

            #wywołanie funckji pozwalającej na ruch obiektów
            self.ruch()

            #czyszczenie ekranu aby zapobiec zostawianiu śladu za poruszającym obiektem
            self.okno.fill((0,0,0))

            ##wywołanie funckji pozwalającej na rysowanie obiektów
            self.tworzenie()
            
            #aktualizacja okna ze zmianami
            pg.display.flip()

            #jesli liczba zyc spadnie nizej niz 0 to wywola sie funckja koniec()
            if self.gracz1.zycia==0:
                self.wygrana=2
                self.koniec()
            if self.gracz2.zycia==0:
                self.wygrana=1
                self.koniec()

            #obliczenie czasu gry
            self.czas=round(time.time()-self.czas1,2)

    #funkcja ruch
    def ruch(self):
        self.gracz1.ruch()
        self.gracz2.ruch()
        self.pilka.ruch()
        
      
    #funkcja rysoawnia
    def tworzenie(self):
        self.gracz1.tworzenie()
        self.gracz2.tworzenie()
        self.pilka.tworzenie()
       
        #napisy żyć
        zyciat1=pg.font.SysFont('comicsans',40).render("Życia: "+ str(self.gracz1.zycia),1,(255,255,255))
        self.okno.blit(zyciat1,(50,600))
        zyciat2=pg.font.SysFont('comicsans',40).render("Życia: "+ str(self.gracz2.zycia),1,(255,255,255))
        self.okno.blit(zyciat2,(1000,600))


     #funckja końca gry
    def koniec(self):
        #napisy końcowego okna 
        tekst=pg.font.SysFont('comicsans',40).render("koniec gry", True,(255,255,255))
        wynik=pg.font.SysFont('comicsans',40).render("wygrywa gracz numer -> "+str(self.wygrana), True,(255,255,255))
        czas=pg.font.SysFont('comicsans',40).render("Czas: " +str(self.czas), True,(255,255,255))
        
        #wywołanie napisów na pustym już oknie
        self.okno.fill((0,0,0))
        self.okno.blit(tekst,(self.width/2 -(tekst.get_width()/2),(self.height/2 - wynik.get_height()/2)))
        self.okno.blit(wynik,(self.width/2 -(czas.get_width()/2),(self.height/2 - czas.get_height()*1.5)))
        self.okno.blit(czas,(self.width/2 -(wynik.get_width()/2),(self.height/2 - wynik.get_height()*2.5)))

        #stworznie nowego pliku txt oraz zapisanie w nim wyniku gry
        file = open("wynik.txt","w")
        file.write("Koniec wygrany to gracz numer"+str(self.wygrana)+" z czasem "+ str(self.czas))
        file.close()


        pg.display.update()
        time.sleep(5)
        
      