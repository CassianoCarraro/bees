from animal import Animal
from random import randint

class Frog(Animal):

    def __init__(self, screenRect, threadStopEvent, fliesList):
        Animal.__init__(self, screenRect, threadStopEvent, 'frog.png')
        self.speed = randint(50, 80)
        self.moveFreq = 15
        self.fliesList = fliesList

    def update(self, dt):
        Animal.update(self, dt)
        flyCollidedIndex = self.rect.collidelist(self.fliesList);
        
        if flyCollidedIndex > -1:
            self.fliesList[flyCollidedIndex].die()
            

    #def setAngle(self, angle):
        #Frog.imagesRotated = []
        #for image in Frog.images:
            #Frog.imagesRotated.append(pygame.transform.rotate(image, angle))