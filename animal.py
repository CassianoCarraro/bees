import pygame
import constants
import time
import math

from sprite import Sprite
from point import Point
from threading import Thread
from random import randint
from utils import *

class Animal(Sprite, Thread):

    def __init__(self, screen, threadStopEvent, *images):
        Thread.__init__(self)
        Sprite.__init__(self)

        self.alive = True
        self.imagesRotated = self.images = loadImages(images)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        initPoint = self.genPoint()
        self.rect.center = [initPoint.x, initPoint.y]
        self.exact_position = list(self.rect.center)

        self.animationStatus = 0
        self.screen = screen
        self.vec = None
        self.target = None
        self.distance = 0
        self.speed = 100
        self.moveFreq = 1

        self.threadStopEvent = threadStopEvent
        self.calories = 0

    def update(self, dt):
        if (not self.alive):
            return

        self.animationStatus = (self.animationStatus + 1) % len(self.images)
        self.image = self.images[self.animationStatus]

        if self.target:
            travelled = math.hypot(self.vec[0] * dt, self.vec[1] * dt)
            self.distance -= travelled
            if self.distance <= 0:
                self.target = None
            else:
                self.exact_position[0] += self.vec[0] * dt
                self.exact_position[1] += self.vec[1] * dt
                self.rect.center = self.exact_position
        self.updateLabel()

    def move(self):
        self.target = self.genPoint()
        x = self.target.x - self.exact_position[0]
        y = self.target.y - self.exact_position[1]
        self.distance = math.hypot(x, y)
        try:
            self.vec = self.speed * x / self.distance, self.speed * y / self.distance
        except ZeroDivisionError:
            pass

    def die(self):
        self.alive = False

    def updateLabel(self):
        label = pygame.font.SysFont("monospace", 13).render(str(self.calories), 1, (0, 0, 0))
        self.screen.blit(label, (self.rect.left, self.rect.top - 20))
        pygame.display.update(pygame.display.update())

    def run(self):
        while (not self.threadStopEvent.is_set() and self.alive):
            self.move()
            time.sleep(self.moveFreq)
