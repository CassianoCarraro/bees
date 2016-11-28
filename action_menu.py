import sys
import pygame
import constants

from pygame.locals import *
from pgu import gui

class ActionMenu(object):
    txtFlies = None
    txtFrogs = None
    txtClock = None

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
        btnStart = gui.Button("Iniciar")
        btnStart.style.margin_top = btnStart.style.margin_bottom = 10
        btnStart.connect(gui.CLICK, self.start)
        insideContainer.td(btnStart, align=0);

        insideContainer.tr()
        self.txtClock = gui.Label("Tempo: 00:00", background=constants.LIGHTGRAY)
        insideContainer.td(self.txtClock)

        container.tr()
        container.td(insideContainer, align=0)

        return container

    def start(self):
        self.control.simulation.start()
