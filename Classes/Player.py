from Settings import *
from Utilities import *
from Classes.Trail import Trail


class Player(pygame.sprite.Sprite):
    def __init__(self, player: int):
        pygame.sprite.Sprite.__init__(self)
        sprites.add(self, layer=3)
        p1 = loadImage('images/player1.png')
        p2 = loadImage('images/player2.png')
        self.explosions = loadImages('images/explosions/explosion0.png', 'images/explosions/explosion1.png',
                                     'images/explosions/explosion2.png',
                                     'images/explosions/explosion3.png', 'images/explosions/explosion4.png',
                                     'images/explosions/explosion5.png',
                                     'images/explosions/explosion6.png', 'images/explosions/explosion7.png',
                                     'images/explosions/explosion8.png',
                                     'images/explosions/explosion9.png', 'images/explosions/explosion10.png', )
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

        self.speed = 5
        Player.left = (-self.speed, 0)
        Player.right = (self.speed, 0)
        Player.up = (0, -self.speed)
        Player.down = (0, self.speed)
        self.exploded = False

        self.dx, self.dy = 0, 0
        self.trails = []
        self.last = 0
        self.exploding = False
        self.explodingc = 0

    def changeDifficulty(self, difficulty=0):
        if difficulty==0:
            self.speed = 3
        else:
            self.speed = 5
        Player.left = (-self.speed, 0)
        Player.right = (self.speed, 0)
        Player.up = (0, -self.speed)
        Player.down = (0, self.speed)

    def explode(self):
        self.exploding = True
        self.exploded = True

    def changeexplosion(self):
        self.image = self.explosions[self.explodingc]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.explodingc += 1
        if self.explodingc > 10:
            self.exploding = False
            self.explodingc = 0
        self.last = pygame.time.get_ticks()

    def stop(self):
        self.dx, self.dy = 0,0

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
            self.rect.center = Settings.SCREEN_WIDTH - 40, Settings.SCREEN_HEIGHT - 40
            self.dir = 'up'
        self.exploded = False
        self.trails.clear()
        self.dx, self.dy = 0, 0
        self.last = 0

    def update(self):
        now = pygame.time.get_ticks()
        if not self.exploding:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            if Settings.GAME_DIFFICULTY != 2:
                self.rect.centerx %= Settings.SCREEN_WIDTH
                self.rect.centery %= Settings.SCREEN_HEIGHT
        elif self.exploding and now - self.last >= 50:
            self.changeexplosion()

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
            return self.rect.top < 0 or self.rect.left < 0 or self.rect.right > Settings.SCREEN_WIDTH or self.rect.bottom > Settings.SCREEN_HEIGHT
        return False
