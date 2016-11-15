from animal import Animal
from random import randint

class Bee(Animal):

    def __init__(self, screen, threadStopEvent):
        Animal.__init__(self, screen, threadStopEvent, 'bee1.png', 'bee2.png', 'bee3.png')
        self.speed = randint(100, 200)
        self.moveFreq = 2

    def update(self, dt):
        Animal.update(self, dt)


    #def setAngle(self, angle):
        #Bee.imagesRotated = []
        #for image in self.images:
            #Bee.imagesRotated.append(pygame.transform.rotate(image, angle))
    #def clone():
