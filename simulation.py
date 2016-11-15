import sys
import constants

from bee import Bee
from frog import Frog

class Simulation:
    INDEX_FROGS = 0
    INDEX_FLIES = 1

    def __init__(self, control):
        self.control = control
        self.animalsList = [[] for i in range(2)];
        self.secTime = 0
        self.frameCount = 0
        self.run = False

    def start(self):
        actionMenu = self.control.actionMenu

        frogs = int(actionMenu.txtFrogs.value)
        for i in range(0, frogs):
            frog = Frog(self.control.screen, self.control.threadsStopEvent, self.animalsList[self.INDEX_FLIES])
            self.animalsList[self.INDEX_FROGS].append(frog)
            self.startAnimal(frog)

        flies = int(actionMenu.txtFlies.value)
        for i in range(0, flies):
            fly = Bee(self.control.screen, self.control.threadsStopEvent)
            self.animalsList[self.INDEX_FLIES].append(fly)
            self.startAnimal(fly)

        self.secTime = 0
        self.frameCount = 0
        self.run = True

    def startAnimal(self, animal):
        self.control.drawingGroup.add(animal)
        animal.start();

    def loop(self):
        if self.run:
            self.secTime = self.frameCount // constants.FPS

            minutes = self.secTime // 60
            seconds = self.secTime % 60
            self.control.actionMenu.txtClock.value = "{0:02}:{1:02}".format(minutes, seconds)
            self.control.actionMenu.txtClock.repaint()

            for i, animal in enumerate(self.animalsList[self.INDEX_FLIES]):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)

            self.frameCount += 1

