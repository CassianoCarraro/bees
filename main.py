import random
import pygame
import sys
import threading
from pygame.locals import *

from constants import *
from main_gui import MainGui
from pgu import gui
from simulation import Simulation

class Control(object):
    """docstring for Control"""
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption(APPTITLE)

        self.app = MainGui(self);
        self.app.connect(gui.QUIT, self.terminate, None)

        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.drawingGroup = pygame.sprite.RenderUpdates()
        self.run = True
        self.threadsStopEvent = threading.Event()
        self.simulation = Simulation(self)

    def update(self, dt):
        self.drawingGroup.update(dt)

    def draw(self):
        rectSimulation = self.app.getRenderArea()
        self.screen.set_clip(rectSimulation)
        self.screen.fill(WHITE, rectSimulation)

        updateList = self.drawingGroup.draw(self.screen)

        pguUpdateList = self.app.update()
        if (pguUpdateList):
            updateList += pguUpdateList

    def mainLoop(self):
        while self.run:
            dt = self.clock.tick(self.fps) / 1000.0
            self.app.loop()
            self.update(dt)
            self.draw()
            self.simulation.loop()

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
