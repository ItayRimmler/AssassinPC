import pygame as pg
import c
import numpy as np
import random as r
import queue as qu


# Initiate game...
def play():
    pg.init()
    return pg.display.set_mode((c.W, c.H))


# Quit command...
def q():
    pg.quit()


# Update command...
def upd():
    pg.display.update()


