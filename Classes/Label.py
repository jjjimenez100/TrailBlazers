from Settings import *
from Utilities import *

class Label(pygame.sprite.Sprite):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        sprites.add(self)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = ''
        self.center = 400, 300

    def update(self):
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
