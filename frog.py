from animal import Animal
from random import randint

class Frog(Animal):

    def __init__(self, simulation, fliesList):
        Animal.__init__(self, simulation, 'frog.png')
        self.speed = randint(50, 80)
        self.moveFreq = randint(15, 20)
        self.fliesList = fliesList

    def update(self, dt):
        Animal.update(self, dt)

        fly = self.fliesList[self.rect.collidelist(self.fliesList)]
        if fly.alive:
            self.calories = self.calories + 1
            fly.die()

    def die(self):
        self.simulation.updateSumFrogs(-1)
