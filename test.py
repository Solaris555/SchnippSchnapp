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
        vari.append('cards\\' + cardList[i][0] + cardList[i][1] + '.gif')
        i += 1

def makeVar(j):
    
    loadCards()
    for j in range(len(vari)):
        variablen[j] = vari[j]
        return j
                    
print (variablen)
