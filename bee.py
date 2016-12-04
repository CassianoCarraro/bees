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

        sugar = self.sugarsList[self.rect.collidelist(self.sugarsList)]
        #if(not sugar.eaten):
            #sugar.eaten = True

    def die(self):
        Animal.die(self)
        self.simulation.updateSumFlies(-1)
