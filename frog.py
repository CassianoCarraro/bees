from animal import Animal
from random import randint

class Frog(Animal):

    def __init__(self, screenRect, threadStopEvent):
        Animal.__init__(self, screenRect, threadStopEvent, 'frog.png')
        self.speed = randint(50, 80)
        self.moveFreq = 15

    #def setAngle(self, angle):
        #Frog.imagesRotated = []
        #for image in Frog.images:
            #Frog.imagesRotated.append(pygame.transform.rotate(image, angle))