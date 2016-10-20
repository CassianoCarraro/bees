import random, pygame, sys
from pygame.locals import *
from bee import Bee
from frog import Frog

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

angles = (( 45,   0,  -45),
          ( 90,   0,  -90),
          (135, 180, -135))

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, drawing_group, bee, frog

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    frog = Frog(DISPLAYSURF.get_rect())
    bee = Bee(DISPLAYSURF.get_rect())

    drawing_group = pygame.sprite.RenderUpdates()
    drawing_group.add(bee)
    drawing_group.add(frog)


    #showStartScreen()
    runGame()


def runGame():
    DISPLAYSURF.fill(WHITE)
    drawGrid()
    pygame.display.update()
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()


        keystate = pygame.key.get_pressed()
        xdir = keystate[K_RIGHT] - keystate[K_LEFT]
        ydir = keystate[K_DOWN]  - keystate[K_UP]

        bee.setAngle(angles[ydir+1][xdir+1])
        bee.rect = bee.rect.move((xdir * 8, ydir * 8)).clamp(DISPLAYSURF.get_rect())

        if bee.rect.colliderect(frog):
            raise SystemExit, "You win!"

        DISPLAYSURF.fill(WHITE)
        drawGrid()

        drawing_group.update()
        update_list = drawing_group.draw(DISPLAYSURF)

        pygame.display.update(update_list)
        FPSCLOCK.tick(FPS)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()