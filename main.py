import pygame, random, sys
from pygame.locals import *



# Define Variables
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
bgColor = WHITE
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
slotWidth = 82
slotHeight = 110
sloty = 250
slotx1 = 220
slotx2 = 480
buttonList = []
cardList = []
card = []

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()

    # Set the width and height of the screen [width, height]
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("My Game")


    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    FPSCLOCK = pygame.time.Clock()

    background_image = pygame.image.load("background.jpg").convert()
    loadCards()
    
    
    # -------- Main Program Loop -----------

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP or event.type == pygame.K_ESCAPE:
                done = True
          #  elif event.type == pygame.K_LSHIFT or event.type == pygame.KEYUP:
                
            
        # --- Game logic should go here



        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        DISPLAYSURF.fill(WHITE)

        # --- Drawing code should go here
        DISPLAYSURF.blit(background_image, [0, 0])
        DISPLAYSURF.blit(card1, [slotx1 + 2, sloty + 2])
        cardSlot1 = pygame.draw.rect(DISPLAYSURF,BLACK,[slotx1, sloty, slotWidth, slotHeight], 2)
        cardSlot2 = pygame.draw.rect(DISPLAYSURF,BLACK,[slotx2, sloty, slotWidth, slotHeight], 2)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        FPSCLOCK.tick(60)

#Functions
def getButton():

    buttons = '234567890wertzuiosdfghjkxcvbnm'
    i = random.randrange(0, (len(buttons) - 1))
    buttonList.append('K_' + buttons[i])
    
def getCards():
    
    for farbe in ['herz_', 'karo_', 'pik_', 'kreuz_']:
        for wert in ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'bube', 'dame', 'koenig', 'ass']:
            cardList.append ( (farbe, wert) )

def loadCards():

    getCards()
    i = 0
    for i in range(len(cardList)):
        j = i + 1
        card[j] = pygame.image.load('cards\\' + cardList[i][0] + cardList[i][1] + '.gif').convert()
        i += 1


# Close the window and quit.
if __name__ == '__main__':
    main()
pygame.quit()
