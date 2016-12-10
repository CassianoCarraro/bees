import sys
import constants

from random import randint
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
        self.run = False
        self.actionMenu = self.control.app.actionMenu

    def start(self):
        try:
            flies = int(self.actionMenu.txtFlies.value)
            frogs = int(self.actionMenu.txtFrogs.value)
            calories = int(self.actionMenu.txtCalories.value)
        except ValueError:
            return False;

        self.actionMenu.sumFlies.set_text(str(flies))
        self.actionMenu.sumFrogs.set_text(str(frogs))

        for i in range(0, flies):
            fly = Bee(self, self.sugarsList)
            fly.calories = calories

            self.addSubject(fly, self.animalsList[self.INDEX_FLIES])
            fly.start()

        for i in range(0, frogs):
            frog = Frog(self, self.animalsList[self.INDEX_FLIES])
            frog.calories = calories

            self.addSubject(frog, self.animalsList[self.INDEX_FROGS])
            frog.start()

        for i in range(0, randint(3, 10)):
            sugar = Sugar()
            self.addSubject(sugar, self.sugarsList)

        self.control.previousSecTime = self.control.secTime = self.control.frameCount = 0
        self.run = True

        return True

    def addSubject(self, subject, subjectList):
        subjectList.append(subject)
        self.control.drawingGroup.add(subject)

    def loop(self):
        if self.run:
            self.updateClock()
            flies = self.animalsList[self.INDEX_FLIES]
            frogs = self.animalsList[self.INDEX_FROGS]

            for i, animal in enumerate(flies):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)
                    self.control.update(0, True)
                    flies.remove(animal)

            for i, animal in enumerate(frogs):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)
                    self.control.update(0, True)
                    frogs.remove(animal)

            for i, sugar in enumerate(self.sugarsList):
                if sugar.eaten:
                    self.control.drawingGroup.remove(sugar)

    def updateClock(self):
        minutes = self.control.secTime // 60
        seconds = self.control.secTime % 60
        self.actionMenu.txtClock.value = "Tempo: {0:02}:{1:02}".format(minutes, seconds)
        self.actionMenu.txtClock.repaint()

    def updateSumFlies(self, num):
        self.actionMenu.sumFlies.value = str(int(self.actionMenu.sumFlies.value) + num)
        self.actionMenu.sumFlies.repaint()

    def updateSumFrogs(self, num):
        self.actionMenu.sumFlies.value = str(int(self.actionMenu.sumFrogs.value) + num)
        self.actionMenu.sumFlies.repaint()
