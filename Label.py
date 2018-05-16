from pygame.sprite import Sprite
import pygame

class Label(Sprite):

    def __init__(self, fontStyles : str, text : str, size : int, fontColor : (int,int,int),
                 position: (int, int), isBold = False, isItalic = False):
        Sprite.__init__(self)
        self.fontStyles = fontStyles
        self.text = text
        self.size = size
        self.fontColor = fontColor
        self.isBold = isBold
        self.isItalic = isItalic
        self.position = position

    def update(self):
        self.image = pygame.font.Font(self.fontStyles, self.size)\
            .render(self.text, True, self.fontColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]