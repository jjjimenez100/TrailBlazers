from Settings import Settings
from Utilities import *
from Classes.Trail import Trail

class Player(pygame.sprite.Sprite):
    def __init__(self, player: int):
        pygame.sprite.Sprite.__init__(self)
        sprites.add(self)
        p1 = loadImage('images/player1.png')
        p2 = loadImage('images/player2.png')

        self.dir = ''
        if player == 1:
            self.image = p1
            self.rect = self.image.get_rect()
            self.rect.center = 40, 40
            self.dir = 'down'
            self.image = pygame.transform.rotate(self.image, 180)
        elif player == 2:
            self.image = p2
            self.rect = self.image.get_rect()
            self.rect.center = Settings.SCREEN_WIDTH - 40, Settings.SCREEN_HEIGHT - 40
            self.dir = 'up'

        if Settings.GAME_DIFFICULTY == 0:
            self.speed = 5
        else:
            self.speed = 7
        Player.left = (-self.speed, 0)
        Player.right = (self.speed, 0)
        Player.up = (0, -self.speed)
        Player.down = (0, self.speed)

        self.dx, self.dy = 0,0
        self.trails = []
        self.last = 0

    def restart(self, player: int):
        p1 = loadImage('images/player1.png')
        p2 = loadImage('images/player2.png')

        if player == 1:
            self.image = p1
            self.rect = self.image.get_rect()
            self.rect.center = 40, 40
            self.dir = 'down'
            self.image = pygame.transform.rotate(self.image, 180)
        elif player == 2:
            self.image = p2
            self.rect = self.image.get_rect()
            self.rect.center = SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40
            self.dir = 'up'

        self.trails.clear()
        self.dx, self.dy = 0,0
        self.last = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if Settings.GAME_DIFFICULTY != 2:
            self.rect.centerx %= Settings.SCREEN_WIDTH
            self.rect.centery %= Settings.SCREEN_HEIGHT

    def rotate(self, degrees: int):
        self.image = pygame.transform.rotate(self.image, degrees)

    def createTrail(self):
        now = pygame.time.get_ticks()
        if now - self.last >= 100:
            trail = Trail(self.rect.centerx, self.rect.centery, self.dir)
            self.trails.append(trail)
            self.last = pygame.time.get_ticks()

    def changeDirection(self, dir: str):
        if dir == 'left' and self.dir != 'right':
            self.dx, self.dy = self.left
            if self.dir == 'up':
                self.rotate(90)
            if self.dir == 'down':
                self.rotate(-90)
            self.dir = 'left'
        if dir == 'up' and self.dir != 'down':
            self.dx, self.dy = self.up
            if self.dir == 'right':
                self.rotate(90)
            if self.dir == 'left':
                self.rotate(-90)
            self.dir = 'up'
        if dir == 'right' and self.dir != 'left':
            self.dx, self.dy = self.right
            if self.dir == 'down':
                self.rotate(90)
            if self.dir == 'up':
                self.rotate(-90)
            self.dir = 'right'
        if dir == 'down' and self.dir != 'up':
            self.dx, self.dy = self.down
            if self.dir == 'left':
                self.rotate(90)
            if self.dir == 'right':
                self.rotate(-90)
            self.dir = 'down'

    def checkOutOfBounds(self) -> bool:
        if Settings.GAME_DIFFICULTY == 2:
            return self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 800 or self.rect.bottom > 600
        return False
