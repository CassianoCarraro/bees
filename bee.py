from animal import Animal

class Bee(Animal):

    def __init__(self, screenRect, threadStopEvent):
        Animal.__init__(self, screenRect, threadStopEvent, 'bee1.png', 'bee2.png', 'bee3.png')

    #def setAngle(self, angle):
        #Bee.imagesRotated = []
        #for image in self.images:
            #Bee.imagesRotated.append(pygame.transform.rotate(image, angle))
    #def clone():