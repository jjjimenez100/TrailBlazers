import pygame

class Player(pygame.sprite.Sprite):
    p1 = pygame.image.load('player1.png')
    p2 = pygame.image.load('player2.png')
    left = (-5,0)
    right = (5,0)
    up = (0,-5)
    down = (0,5)
    def __init__(self, player, color):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        if player==1:
            self.image = Player.p1
            self.image = pygame.transform.rotate(self.image, 180)
        elif player==2:
            self.image = Player.p2
        self.rect = self.image.get_rect()
        if player==1:
            self.rect.center = 40,40
        elif player==2:
            self.rect.center = 760, 560
        self.dx = 0
        self.dy = 0
        self.dir = 'down'
        self.trails = []

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        trail = Trail(self.rect.centerx,self.rect.centery, self.color)
        self.trails.append(trail)
        sprites.add(trail)

    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.image, degrees)

    def changeDirection(self, dir):
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

    def checkOutOfBounds(self):
        return self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 800 or self.rect.bottom > 600

class Trail(pygame.sprite.Sprite):
    def __init__(self,x,y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = x,y


class Label(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = ''
        self.center = 400,300

    def update(self):
        self.image = self.font.render(self.text, True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

def init():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('game')

    display = pygame.Surface(screen.get_size())
    display = display.convert()
    display.fill((0, 0, 0))
    screen.blit(display, (0,0))

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
                if event.key == pygame.K_w:
                    p2.changeDirection('up')
                if event.key == pygame.K_s:
                    p2.changeDirection('down')
                if event.key == pygame.K_a:
                    p2.changeDirection('left')
                if event.key == pygame.K_d:
                    p2.changeDirection('right')

        for i in p1.trails:
            if p2.rect.colliderect(i) or p2.checkOutOfBounds():
                sprites.empty()
                sprites.add(gameover)
                gameover.text = 'boom explosion p1 wins walao'
        for i in p2.trails:
            if p1.rect.colliderect(i) or p1.checkOutOfBounds():
                sprites.empty()
                sprites.add(gameover)
                gameover.text = 'p2 wins walao sad boi'

        sprites.clear(screen, display)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    quit()

if __name__ == '__main__':
    init()