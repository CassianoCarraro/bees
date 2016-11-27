import pygame

from sprite import Sprite
from point import Point
from utils import *

class Sugar(Sprite):
    def __init__(self):
    	Sprite.__init__(self)
    	self.image = loadImage('sugar.png')
    	self.image = scaleImage(self.image, -92)
    	self.rect = self.image.get_rect()

    	initPoint = self.genPoint()
        self.rect.center = [initPoint.x, initPoint.y]

        self.eaten = False