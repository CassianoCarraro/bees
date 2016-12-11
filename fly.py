import constants

from animal import Animal
from random import randint

class Fly(Animal):

    def __init__(self, simulation, sugarsList):
        Animal.__init__(self, simulation, 'bee1.png', 'bee2.png', 'bee3.png')
        self.speed = randint(100, 200)
        self.moveFreq = 2
        self.sugarsList = sugarsList

    def update(self, dt):
        Animal.update(self, dt)
        self.updateCollision()

    def updateCollision(self):
        sugar = self.verifyCollision(self.sugarsList)
        if(sugar is not None and not sugar.eaten):
            sugar.eat()
            self.calories = self.calories + constants.SUGARCALORIES
            if self.calories >= constants.FLYCALMULTIPLY:
                self.multiply()

    def multiply(self):
        fly = Fly(self.simulation, self.sugarsList)
        self.calories = fly.calories = self.calories // 2
        self.simulation.addSubject(fly, self.simulation.animalsList[self.simulation.INDEX_FLIES])
        fly.start()
