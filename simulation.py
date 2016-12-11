import sys
import constants

from random import randint
from fly import Fly
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
        self.addedSugarAt = 0

    def start(self):
        try:
            flies = int(self.actionMenu.txtFlies.value)
            frogs = int(self.actionMenu.txtFrogs.value)
            calories = int(self.actionMenu.txtCalories.value)
        except ValueError:
            return False;

        for i in range(0, flies):
            fly = Fly(self, self.sugarsList)
            fly.calories = calories

            self.addSubject(fly, self.animalsList[self.INDEX_FLIES])
            fly.start()

        for i in range(0, frogs):
            frog = Frog(self, self.animalsList[self.INDEX_FLIES])
            frog.calories = calories

            self.addSubject(frog, self.animalsList[self.INDEX_FROGS])
            frog.start()

        for i in range(0, randint(3, 10)):
            self.addSugar()

        self.control.previousSecTime = self.control.secTime = self.control.frameCount = 0
        self.run = True

        return True

    def addSubject(self, subject, subjectList):
        subjectList.append(subject)
        self.control.drawingGroup.add(subject)

    def loop(self):
        if self.run:
            seconds = self.updateClock()
            flies = self.animalsList[self.INDEX_FLIES]
            frogs = self.animalsList[self.INDEX_FROGS]

            for i, animal in enumerate(flies):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)
                    flies.remove(animal)

            for i, animal in enumerate(frogs):
                if (not animal.alive):
                    self.control.drawingGroup.remove(animal)
                    frogs.remove(animal)

            for i, sugar in enumerate(self.sugarsList):
                if sugar.eaten:
                    self.control.drawingGroup.remove(sugar)

            if (seconds == 59):
                self.addedSugarAt = 0

            if (seconds % constants.SUGARFREQ == 0 and seconds > self.addedSugarAt):
                self.addedSugarAt = seconds
                self.addSugar()

    def updateClock(self):
        minutes = self.control.secTime // 60
        seconds = self.control.secTime % 60
        self.actionMenu.txtClock.value = "Tempo: {0:02}:{1:02}".format(minutes, seconds)
        self.actionMenu.txtClock.repaint()

        return seconds

    def updateSum(self, num, className):
        if (className == "Fly"):
            self.actionMenu.sumFlies.value = str(int(self.actionMenu.sumFlies.value) + num)
            self.actionMenu.sumFlies.repaint()
        elif (className == "Frog"):
            self.actionMenu.sumFrogs.value = str(int(self.actionMenu.sumFrogs.value) + num)
            self.actionMenu.sumFrogs.repaint()
        elif (className == "Sugar"):
            self.actionMenu.sumSugar.value = str(int(self.actionMenu.sumSugar.value) + num)
            self.actionMenu.sumSugar.repaint()

    def addSugar(self):
        sugar = Sugar(self)
        self.addSubject(sugar, self.sugarsList)
