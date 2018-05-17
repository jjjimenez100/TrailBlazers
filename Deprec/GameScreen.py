from pygame.sprite import Sprite
from Utilities import *
from Label  import Label

class GameScreen(Sprite):
    def __init__(self, backgroundLocation : str, backgroundMusicLocation : str):
        Sprite.__init__(self)

        self.image = loadImage(backgroundLocation)
        self.backgroundMusic = loadSound(backgroundMusicLocation)
        self.backgroundMusic.play()

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.menu = 0
        self.labels = []

    def addLabel(self, newLabel : Label):
        self.labels.append(newLabel)

