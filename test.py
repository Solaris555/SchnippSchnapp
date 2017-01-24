import pygame, random, sys
from pygame.locals import *


cardList = []
vari = []
variablen = []
def getCards():
    
    for farbe in ['herz_', 'karo_', 'pik_', 'kreuz_']:
        for wert in ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'bube', 'dame', 'koenig', 'ass']:
            cardList.append ( (farbe, wert) )
            


def loadCards():
    
    getCards()
    i = 0

    for i in range(len(cardList)):
        vari.append(cardList[i][0] + cardList[i][1])
        i += 1

def makeVar(j):
    
    loadCards()

#def shuffleCards():
    
loadCards()
herz_2 = vari[0]
#print(len(vari))
print (herz_2)
