from Settings import *
from Classes.Utilities import *

class Label(pygame.sprite.Sprite):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        sprites.add(self, layer = 2)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = ''
        self.center = Settings.SCREEN_WIDTH/2, Settings.SCREEN_HEIGHT/2

    def update(self):
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
