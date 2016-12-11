import sys
import pygame
import constants

from pygame.locals import *
from pgu import gui

class ActionMenu(object):
    btnStart = None
    txtFlies = None
    txtFrogs = None
    txtCalories = None
    txtClock = None
    sumFrogs = None
    sumFlies = None
    sumSugar = None

    def __init__(self, control):
        self.control = control

    def init(self):
        container = gui.Table(width=constants.MENUWIDTH)
        insideContainer = gui.Table(width=constants.MENUWIDTH - 50)
        insideContainer.style.padding_top = 20

        insideContainer.tr()
        insideContainer.td(gui.Label("Moscas"), align=-1)
        self.txtFlies = gui.Input(size=15)
        insideContainer.tr()
        insideContainer.td(self.txtFlies, align=-1)

        insideContainer.tr()
        insideContainer.td(gui.Label("Sapos"), align=-1)
        self.txtFrogs = gui.Input(size=15)
        insideContainer.tr()
        insideContainer.td(self.txtFrogs, align=-1)

        insideContainer.tr()
        insideContainer.td(gui.Label("Calorias"), align=-1)
        self.txtCalories = gui.Input(size=15)
        insideContainer.tr()
        insideContainer.td(self.txtCalories, align=-1)

        insideContainer.tr()
        self.btnStart = gui.Button("Iniciar")
        self.btnStart.style.margin_top = self.btnStart.style.margin_bottom = 10
        self.btnStart.connect(gui.CLICK, self.start)
        insideContainer.td(self.btnStart, align=0);

        insideContainer.tr()
        self.txtClock = gui.Label("Tempo: 00:00", background=constants.LIGHTGRAY)
        self.txtClock.style.margin_top = 20
        insideContainer.td(self.txtClock, align=0)

        insideContainer.tr()
        lblSumFlies = gui.Label("Total Moscas", background=constants.LIGHTGRAY)
        lblSumFlies.style.margin_top = 20
        insideContainer.td(lblSumFlies, align=-1)
        insideContainer.tr()
        self.sumFlies = gui.Label("0     ", background=constants.LIGHTGRAY)
        insideContainer.td(self.sumFlies, align=-1)

        insideContainer.tr()
        lblSumFrogs = gui.Label("Total Sapos", background=constants.LIGHTGRAY)
        lblSumFrogs.style.margin_top = 5
        insideContainer.td(lblSumFrogs, align=-1)
        insideContainer.tr()
        self.sumFrogs = gui.Label("0     ", background=constants.LIGHTGRAY)
        insideContainer.td(self.sumFrogs, align=-1)

        insideContainer.tr()
        lblSumSugar = gui.Label("Total Açúcar", background=constants.LIGHTGRAY)
        lblSumSugar.style.margin_top = 5
        insideContainer.td(lblSumSugar, align=-1)
        insideContainer.tr()
        self.sumSugar = gui.Label("0     ", background=constants.LIGHTGRAY)
        insideContainer.td(self.sumSugar, align=-1)

        container.tr()
        container.td(insideContainer, align=0)

        return container

    def start(self):
        if (self.control.simulation.start()):
            self.btnStart.disabled = True
