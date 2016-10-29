import random
import pygame
import sys
import threading
from pygame.locals import *

from constants import *
from bee import Bee
from frog import Frog

class Control(object):
    """docstring for Control"""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ecossistema')
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.screenRect = self.screen.get_rect()
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.drawingGroup = pygame.sprite.RenderUpdates()
        self.run = True
        self.threadsStopEvent = threading.Event()

        frog = Frog(self.screenRect, self.threadsStopEvent)
        frog.start();

        frog2 = Frog(self.screenRect, self.threadsStopEvent)
        frog2.start();

        bee = Bee(self.screenRect, self.threadsStopEvent)
        bee.start();

        bee2 = Bee(self.screenRect, self.threadsStopEvent)
        bee2.start();

        bee3 = Bee(self.screenRect, self.threadsStopEvent)
        bee3.start();

        self.drawingGroup.add(frog)
        self.drawingGroup.add(frog2)
        self.drawingGroup.add(bee)
        self.drawingGroup.add(bee2)
        self.drawingGroup.add(bee3)

        self.drawGrid();
        pygame.display.update()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
                break

    def update(self, dt):
        self.drawingGroup.update(dt)

    def draw(self):
        self.drawGrid()
        updateList = self.drawingGroup.draw(self.screen)
        pygame.display.update(updateList)

    def drawGrid(self):
        self.screen.fill(WHITE)
        for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
            pygame.draw.line(self.screen, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
            pygame.draw.line(self.screen, DARKGRAY, (0, y), (WINDOWWIDTH, y))

    def mainLoop(self):
        while self.run:
            dt = self.clock.tick(self.fps) / 1000.0
            self.eventLoop()
            self.update(dt)
            self.draw()

    def terminate(self):
        self.threadsStopEvent.set()
        self.run = False

def main():
    app = Control()
    app.mainLoop()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()