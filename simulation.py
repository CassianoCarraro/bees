import sys

from bee import Bee
from frog import Frog

class Simulation:
    INDEX_FROGS = 0
    INDEX_FLIES = 1

    def __init__(self, control):
        self.control = control
        self.animalsList = [[] for i in range(2)];

    def start(self):
        actionMenu = self.control.actionMenu

        frogs = int(actionMenu.txtFrogs.value)
        for i in range(0, frogs):
            frog = Frog(self.control.screenRect, self.control.threadsStopEvent, self.animalsList[self.INDEX_FLIES])
            self.animalsList[self.INDEX_FROGS].append(frog)
            self.startAnimal(frog)

        flies = int(actionMenu.txtFlies.value)
        for i in range(0, flies):
            fly = Bee(self.control.screenRect, self.control.threadsStopEvent)
            self.animalsList[self.INDEX_FLIES].append(fly)
            self.startAnimal(fly)

    def startAnimal(self, animal):
        self.control.drawingGroup.add(animal)
        animal.start();
