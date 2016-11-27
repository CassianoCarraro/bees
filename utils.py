import pygame
import os

def loadImage(file):
	file = os.path.join('media', file)
	surface = pygame.image.load(file)
	return surface.convert_alpha()

def loadImages(files):
	return [loadImage(file) for file in files]

def scaleImage(image, percent):
	dimension = image.get_rect().size
	percent = float(percent) / 100
	return pygame.transform.scale(image, (int(dimension[0] + dimension[0] * percent), int(dimension[0] + dimension[1] * percent)))