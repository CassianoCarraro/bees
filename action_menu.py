import sys
import pygame

from pygame.locals import *
from pgu import gui

class ActionMenu:

    def __init__(self, control):
        self.control = control

    def init(self):
        container = gui.Table()

        container.tr()
        container.td(gui.Label("Nº Moscas:"))
        self.txtFlies = gui.Input(size=5)
        container.td(self.txtFlies)

        container.tr()
        container.td(gui.Label("Nº Sapos:"))
        self.txtFrogs = gui.Input(size=5)
        container.td(self.txtFrogs)

        container.tr()
        btnStart = gui.Button("Iniciar")
        btnStart.connect(gui.CLICK, self.start)
        container.td(btnStart);

        return container

    def start(self):
        self.control.simulation.start()
