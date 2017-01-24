import pygame, random, sys, os, itertools
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
FARBE = ['herz_', 'karo_', 'pik_', 'kreuz_']
WERT = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'bube', 'dame', 'koenig', 'ass']
BUTTONS = '234567890wertzuiosdfghjkxcvbnm'
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
vari = []
vari1 = []
vari2 = []
player = True



_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def main():
    global FPSCLOCK, DISPLAYSURF
    player = True
    pygame.init()

    # Set the width and height of the screen [width, height]
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("My Game")


    # Loop until the user clicks the close button.
    

    # Used to manage how fast the screen updates
    FPSCLOCK = pygame.time.Clock()

    background_image = pygame.image.load("background.jpg").convert()
    loadCards()
  

     

    # -------- Main Program Loop -----------

    while True:
        # --- Main event loop
        for event in pygame.event.get():


            
            if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_a and player == True):        
                            random.shuffle(vari1)
                            player = False
                    if (event.key == pygame.K_l and player == False):
                            random.shuffle(vari2)
                            player = True
                            
            elif event.type == pygame.QUIT:
                terminate()
                           
                              
        # --- Game logic should go here
        testMatch()

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        #DISPLAYSURF.fill(WHITE)

        # --- Drawing code should go here
        DISPLAYSURF.blit(background_image, [0, 0])
        DISPLAYSURF.blit(get_image(vari1[0] + '.gif'), [slotx1 + 2, sloty + 2])
        DISPLAYSURF.blit(get_image(vari2[0] + '.gif'), [slotx2 + 2, sloty + 2])
        cardSlot1 = pygame.draw.rect(DISPLAYSURF,BLACK,[slotx1, sloty, slotWidth, slotHeight], 2)
        cardSlot2 = pygame.draw.rect(DISPLAYSURF,BLACK,[slotx2, sloty, slotWidth, slotHeight], 2)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()

        # --- Limit to 60 frames per second
        FPSCLOCK.tick(60)

#Functions
def getButton():

    
    i = random.randrange(0, (len(BUTTONS) - 1))
    buttonList.append('K_' + BUTTONS[i])
    
def getCards():
    
    for farbe in FARBE:
        for wert in WERT:
            cardList.append ( (farbe, wert) )

def loadCards():

    getCards()
    i = 0
    for i in range(len(cardList)):
        
        vari1.append(cardList[i][0] + cardList[i][1])
        random.shuffle(vari1)
        vari2.append(cardList[i][0] + cardList[i][1])
        i += 1
def terminate():
        pygame.quit()
        sys.exit()

def testMatch():
        splitFarbe1, splitWert1 = vari1[0].split('_')
        splitFarbe2, splitWert2 = vari2[0].split('_') 
        if (splitWert1 == splitWert2):
                 terminate()
    


# Close the window and quit.
if __name__ == '__main__':
    main()
pygame.quit()
