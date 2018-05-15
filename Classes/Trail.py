from Utilities import *

class Trail(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        pygame.sprite.Sprite.__init__(self)
        trails.add(self)
        sprites.add(self)
        self.image = loadImage('images/sd.png')
        if dir == 'left' or dir == 'right':
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
