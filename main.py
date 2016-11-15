import random
import pygame
import sys
import threading
from pygame.locals import *

from action_menu import ActionMenu
from constants import *
from pgu import gui
from simulation import Simulation

class Control(object):
    """docstring for Control"""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ecossistema')

        self.app = gui.App();
        self.app.connect(gui.QUIT, self.terminate, None)

        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.screenRect = pygame.draw.rect(self.screen, WHITE, Rect((0, 0), (GAMERECTWIDTH, WINDOWHEIGHT)))
        self.menuRect = pygame.draw.rect(self.screen, LIGHTGRAY, Rect((GAMERECTWIDTH, 0), (MENUWIDTH, WINDOWHEIGHT)))

        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.actionMenu = ActionMenu(self)
        self.drawingGroup = pygame.sprite.RenderUpdates()
        self.run = True
        self.threadsStopEvent = threading.Event()
        self.simulation = Simulation(self)
        self.app.init(self.actionMenu.init(), self.screen, self.menuRect)

        "self.drawGrid();"
        pygame.display.update()

    def update(self, dt):
        self.drawingGroup.update(dt)

    def draw(self):
        "self.drawGrid()"
        self.screen.fill(WHITE)
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
            self.app.loop()
            self.update(dt)
            self.draw()

    def terminate(self, ev):
        self.threadsStopEvent.set()
        self.run = False
        self.app.quit()

def main():
    app = Control()
    app.mainLoop()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
