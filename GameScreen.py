from pygame.sprite import Sprite
from game2 import Label
from Utilities import *
import pygame

class GameScreen(Sprite):
    def __init__(self, backgroundLocation:str="", labels:[Label]=[], positions:[(int, int)]=[]):
        self.image = loadImage(backgroundLocation)
        self.rect = self.image.get_rect()
        self.labels = labels
        self.positions = self.positions
        # Midnight snack break