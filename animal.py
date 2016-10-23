import pygame
import constants
import time

from point import Point
from threading import Thread
from random import randint
from utils import loadImages

class Animal(pygame.sprite.Sprite, Thread):

    def __init__(self, screenRect, threadStopEvent, *images):
        Thread.__init__(self)
        pygame.sprite.Sprite.__init__(self)

        self.calories = 0
        self.imagesRotated = self.images = loadImages(images)
        self.image = self.images[0]
        self.p = Point(0, 0)
        self.animationStatus = 0
        self.screenRect = screenRect
        self.threadStopEvent = threadStopEvent

        self.rect = self.image.get_rect()

    def update(self):
        self.animationStatus = (self.animationStatus + 1) % len(self.images)
        self.image = self.images[self.animationStatus]

    def move(self):
        self.p.x = randint(-100, 100)
        self.p.y = randint(-100, 100)

        self.rect = self.rect.move(self.p.x, self.p.y).clamp(self.screenRect)

    def die(self):
        self.calories = 0

    def run(self):
        while (not self.threadStopEvent.is_set()):
            self.move()
            time.sleep(0.5)