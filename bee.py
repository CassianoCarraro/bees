import pygame
import os
from utils import loadImages

class Bee(pygame.sprite.Sprite):
    images = []
    imagesRotated = []

    def __init__(self, screenRect):
        pygame.sprite.Sprite.__init__(self)

        Bee.imagesRotated = Bee.images = loadImages('bee1.png', 'bee2.png', 'bee3.png')

        self.image = self.images[0]
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(screenRect.centerx - imgRect.centerx,
            screenRect.centery - imgRect.centery)
        self.animIdx = 0

    def update(self):
        self.animIdx = (self.animIdx + 1) % len(self.images)
        self.image = self.imagesRotated[self.animIdx]

    def setAngle(self, angle):
        Bee.imagesRotated = []
        for image in Bee.images:
            Bee.imagesRotated.append(pygame.transform.rotate(image, angle))