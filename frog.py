import pygame
import os
from utils import loadImages

class Frog(pygame.sprite.Sprite):
    images = []
    imagesRotated = []

    def __init__(self, screenRect):
        pygame.sprite.Sprite.__init__(self)
        Frog.imagesRotated = Frog.images = Frog.images = loadImages('frog.png')
        self.image = self.images[0]
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(50,
            50)
        self.animIdx = 0

    def update(self):
        self.animIdx = (self.animIdx + 1) % len(self.images)
        self.image = self.imagesRotated[self.animIdx]

    def setAngle(self, angle):
        Frog.imagesRotated = []
        for image in Frog.images:
            Frog.imagesRotated.append(pygame.transform.rotate(image, angle))