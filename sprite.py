import pygame
import constants

from random import randint
from point import Point

class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

	def genPoint(self):
		return Point(randint(0, constants.GAMERECTWIDTH), randint(0, constants.WINDOWHEIGHT))

	def verifyCollision(self, subjects):
		subject = None
		collideIndex = self.rect.collidelist(subjects)
		if collideIndex != -1:
			subject = subjects[collideIndex]
		return subject