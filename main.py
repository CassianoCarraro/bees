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

    def __init__(self):
        self.display = pygame.display
        self.screen = self.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.display.set_caption(APPTITLE)
        self.app = MainGui(self);
        self.app.connect(gui.QUIT, self.terminate, None)

        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.drawingGroup = pygame.sprite.RenderUpdates()
        self.run = True
        self.threadsStopEvent = threading.Event()
        self.simulation = Simulation(self)
        self.secTime = 0
        self.previousSecTime = 0
        self.frameCount = 0

    def update(self, dt):
        self.secTime = self.frameCount // self.fps
        self.drawingGroup.update(dt)
        self.display.flip()

        if self.previousSecTime < self.secTime:
            self.previousSecTime = self.secTime
        self.frameCount += 1

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
            self.simulation.loop()
            self.app.loop()
            self.draw()

            dt = self.clock.tick(self.fps) / 1000.0
            self.update(dt)

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
