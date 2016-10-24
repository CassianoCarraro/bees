from animal import Animal
from random import randint

class Bee(Animal):

    def __init__(self, screenRect, threadStopEvent):
        Animal.__init__(self, screenRect, threadStopEvent, 'bee1.png', 'bee2.png', 'bee3.png')
        self.speed = randint(100, 200)
        self.moveFreq = 2

    #def setAngle(self, angle):
        #Bee.imagesRotated = []
        #for image in self.images:
            #Bee.imagesRotated.append(pygame.transform.rotate(image, angle))
    #def clone():