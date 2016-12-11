import pygame

from sprite import Sprite
from point import Point
from utils import *

class Sugar(Sprite):
    def __init__(self, simulation):
        Sprite.__init__(self)
        self.image = loadImage('sugar.png')
        self.image = scaleImage(self.image, -92)
        self.rect = self.image.get_rect()
        self.simulation = simulation

        initPoint = self.genPoint()
        self.rect.center = [initPoint.x, initPoint.y]

        self.eaten = False
        self.simulation.updateSum(1, self.__class__.__name__)

    def eat(self):
    	self.eaten = True
    	self.simulation.updateSum(-1, self.__class__.__name__)
