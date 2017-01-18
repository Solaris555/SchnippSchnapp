import pygame, random, sys
from pygame.locals import *


cardList = []

def getCards():
    
    for farbe in ['herz_', 'karo_', 'pik_', 'kreuz_']:
        for wert in ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'bube', 'dame', 'koenig', 'ass']:
            cardList.append ( (farbe, wert) )
            



getCards()

print(cardList[0][0] + cardList[0][1])
