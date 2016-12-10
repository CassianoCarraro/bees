from animal import Animal
from random import randint

class Bee(Animal):

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
            sugar.eaten = True
            self.calories = self.calories + 1
            if self.calories >= 10:
                self.multipy()

    def multipy(self):
        fly = Bee(self.simulation, self.sugarsList)
        self.calories = fly.calories = calories / 2
        self.simulation.addSubject(fly, self.simulation.animalsList[self.simulation.INDEX_FLIES])
        fly.start()

    def die(self):
        Animal.die(self)
        self.simulation.updateSumFlies(-1)
