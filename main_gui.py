import sys
import pygame
import constants

from action_menu import ActionMenu
from pygame.locals import *
from pgu import gui

class DrawingArea(gui.Widget):

    def __init__(self, width, height):
        gui.Widget.__init__(self, width=width, height=height)
        self.imageBuffer = pygame.Surface((width, height))
        self.imageBuffer.fill(constants.WHITE)

    def paint(self, surf):
        surf.blit(self.imageBuffer, (0, 0))

    def saveBackground(self):
        disp = pygame.display.get_surface()
        self.imageBuffer.blit(disp, self.get_abs_rect())

class MainGui(gui.Desktop):
    simulationArea = None
    menuArea = None
    actionMenu = None
    control = None

    def __init__(self, control):
        gui.Desktop.__init__(self)

        self.control = control
        screen = self.control.screen

        self.simulationArea = DrawingArea(constants.GAMERECTWIDTH,
                                          screen.get_height())

        self.menuArea = gui.Container(width=constants.MENUWIDTH)

        tbl = gui.Table(height=screen.get_height(), background=constants.LIGHTGRAY)
        tbl.tr()
        tbl.td(self.simulationArea)
        tbl.td(self.menuArea, valign=-1)

        self.actionMenu = ActionMenu(control)
        self.menuArea.add(self.actionMenu.init(), 0, 0)

        self.init(tbl, screen)

    def getRenderArea(self):
        return self.simulationArea.get_abs_rect()
