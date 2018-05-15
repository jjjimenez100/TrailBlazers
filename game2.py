from Settings import *
from Utilities import *


class Player(pygame.sprite.Sprite):
    left = (-5, 0)
    right = (5, 0)
    up = (0, -5)
    down = (0, 5)

    def __init__(self, player: int, color: tuple):
        p1 = loadImage('player1.png')
        p2 = loadImage('player2.png')
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        if player == 1:
            self.image = p1
            self.image = pygame.transform.rotate(self.image, 180)
        elif player == 2:
            self.image = p2
        # self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.dir = ''
        if player == 1:
            self.rect.center = 40, 40
            self.dir = 'down'
        elif player == 2:
            self.rect.center = SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40
            self.dir = 'up'
        self.dx = 0
        self.dy = 0
        self.trails = []
        if GAME_DIFFICULTY == 0:
            self.speed = 5
        else:
            self.speed = 7
        Player.left = (-self.speed, 0)
        Player.right = (self.speed, 0)
        Player.up = (0, -self.speed)
        Player.down = (0, self.speed)
        self.last = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if GAME_DIFFICULTY != 2:
            self.rect.centerx %= SCREEN_WIDTH
            self.rect.centery %= SCREEN_HEIGHT

    def rotate(self, degrees: int):
        self.image = pygame.transform.rotate(self.image, degrees)

    def createWall(self):
        now = pygame.time.get_ticks()
        if now - self.last >= 100:
            trail = Trail(self.rect.centerx, self.rect.centery, self.dir)
            self.trails.append(trail)
            sprites.add(trail)
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
        if GAME_DIFFICULTY == 2:
            return self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 800 or self.rect.bottom > 600
        return False


class Trail(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage('sd.png')
        if dir == 'left' or dir == 'right':
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = x, y


class Label(pygame.sprite.Sprite):
    def __init__(self, size: int):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = ''
        self.center = 400, 300

    def update(self):
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


def Gameover(winner: str, text: str):
    sprites.empty()
    sprites.add(text)
    text.text = winner + ' wins walao sad boi'



def init():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('game')

    display = pygame.image.load('bg.png')
    display = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(display, (0, 0))

    global sprites
    sprites = pygame.sprite.Group()
    p1 = Player(1, (107, 190, 0))
    sprites.add(p1)
    p2 = Player(2, (200, 0, 69))
    sprites.add(p2)
    gameover = Label(32)
    sprites.add(gameover)

    clock = pygame.time.Clock()
    fps = 60
    done = False
    p1creating, p2creating = False, False

    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p1.changeDirection('left')
                if event.key == pygame.K_RIGHT:
                    p1.changeDirection('right')
                if event.key == pygame.K_UP:
                    p1.changeDirection('up')
                if event.key == pygame.K_DOWN:
                    p1.changeDirection('down')
                if event.key == pygame.K_SPACE:
                    p2creating = True
                if event.key == pygame.K_w:
                    p2.changeDirection('up')
                if event.key == pygame.K_s:
                    p2.changeDirection('down')
                if event.key == pygame.K_a:
                    p2.changeDirection('left')
                if event.key == pygame.K_d:
                    p2.changeDirection('right')
                if event.key == pygame.K_KP_ENTER:
                    p1creating = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    p2creating = False
                if event.key == pygame.K_KP_ENTER:
                    p1creating = False

        if p1creating:
            p1.createWall()
        if p2creating:
            p2.createWall()

        for i in range(0, len(p1.trails)):
            if p2.checkOutOfBounds() or p2.rect.colliderect(p1.trails[i]):
                Gameover('p1', gameover)
            if i - (len(p1.trails) - 10) < 0 and p1.rect.colliderect(p1.trails[i]):
                Gameover('p2', gameover)
        for i in range(0, len(p2.trails)):
            if p1.checkOutOfBounds() or p1.rect.colliderect(p2.trails[i]):
                Gameover('p2', gameover)
            if i - (len(p2.trails) - 10) < 0 and p2.rect.colliderect(p2.trails[i]):
                Gameover('p1', gameover)

        if p1.rect.colliderect(p2.rect):
            Gameover('tie', gameover)

        sprites.clear(screen, display)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    quit()


if __name__ == '__main__':
    init()
