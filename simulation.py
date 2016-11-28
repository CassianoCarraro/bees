import sys
import constants

from bee import Bee
from frog import Frog
from sugar import Sugar

class Simulation:
    INDEX_FROGS = 0
    INDEX_FLIES = 1

    def __init__(self, control):
        self.control = control
        self.animalsList = [[] for i in range(2)];
        self.sugarsList = []
        self.secTime = 0
        self.frameCount = 0
        self.run = False
        self.actionMenu = self.control.app.actionMenu

    def start(self):
        frogs = int(self.actionMenu.txtFrogs.value)
        for i in range(0, frogs):
            frog = Frog(self.control.screen, self.control.threadsStopEvent, self.animalsList[self.INDEX_FLIES])
            self.animalsList[self.INDEX_FROGS].append(frog)
            self.startAnimal(frog)

        flies = int(self.actionMenu.txtFlies.value)
        for i in range(0, flies):
            fly = Bee(self.control.screen, self.control.threadsStopEvent, self.sugarsList)
            self.animalsList[self.INDEX_FLIES].append(fly)
            self.startAnimal(fly)

        sugar = Sugar()
        self.addObject(sugar)
        self.sugarsList.append(sugar)

        self.secTime = 0
        self.frameCount = 0
        self.run = True

    def startAnimal(self, animal):
        self.addObject(animal)
        animal.start()

    def addObject(self, obj):
        self.control.drawingGroup.add(obj)

    def loop(self):
        if self.run:
            self.secTime = self.frameCount // constants.FPS

            minutes = self.secTime // 60
            seconds = self.secTime % 60
            self.actionMenu.txtClock.value = "Tempo: {0:02}:{1:02}".format(minutes, seconds)
            self.actionMenu.txtClock.repaint()

            for i, animal in enumerate(self.animalsList[self.INDEX_FLIES]):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)

            for i, sugar in enumerate(self.sugarsList):
                if sugar.eaten:
                    self.control.drawingGroup.remove(sugar)

            self.frameCount += 1

