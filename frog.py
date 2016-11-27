from animal import Animal
from random import randint

class Frog(Animal):

    def __init__(self, screen, threadStopEvent, fliesList):
        Animal.__init__(self, screen, threadStopEvent, 'frog.png')
        self.speed = randint(50, 80)
        self.moveFreq = randint(15, 20)
        self.fliesList = fliesList

    def update(self, dt):
        Animal.update(self, dt)

        fly = self.fliesList[self.rect.collidelist(self.fliesList)]
        if fly.alive:
            self.calories = self.calories + 1
            fly.die()

