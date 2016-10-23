from animal import Animal

class Frog(Animal):

    def __init__(self, screenRect, threadStopEvent):
        Animal.__init__(self, screenRect, threadStopEvent, 'frog.png')

    #def setAngle(self, angle):
        #Frog.imagesRotated = []
        #for image in Frog.images:
            #Frog.imagesRotated.append(pygame.transform.rotate(image, angle))