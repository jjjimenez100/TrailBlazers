import pygame


class Player:
    up = [0, -10]
    down = [0, 10]
    right = [10, 0]
    left = [-10, 0]

    def __init__(self, x=30, y=30, headcolor = (255,255,255), trailcolor = (255,255,255)):
        self.x = x
        self.y = y
        self.headcolor = headcolor
        self.trailcolor = trailcolor
        self.dx = 0
        self.dy = 0
        self.trail = []
        self.trail.append(['head', x, y])

    def getHead(self):
        return self.trail[0]

    def move(self):
        self.getHead()[1] += self.dx
        self.getHead()[2] += self.dy
        self.getHead()[1] %= 800
        self.getHead()[2] %= 600
        self.trail.append(['',self.getHead()[1],self.getHead()[2]])

    def moveLeft(self):
        self.dx, self.dy = Player.left

    def moveRight(self):
        self.dx, self.dy = Player.right

    def moveUp(self):
        self.dx, self.dy = Player.up

    def moveDown(self):
        self.dx, self.dy = Player.down

    def show(self):
        for i in self.trail:
            box = pygame.Surface((10, 10))
            box = box.convert()
            box.fill(self.trailcolor)
            screen.blit(box, (i[1], i[2]))
        box = pygame.Surface((10, 10))
        box = box.convert()
        box.fill(self.headcolor)
        screen.blit(box, (self.getHead()[1], self.getHead()[2]))


def checkCollision(player1: Player, player2: Player):
    #check p1
    for i in player1.trail:
        if player2.getHead()[1] == i[1] and player2.getHead()[2] == i[2]:
            print('player 2 loses la')
            return True
    #check p2
    for i in player2.trail:
        if player1.getHead()[1] == i[1] and player1.getHead()[2] == i[2]:
            print('player 1 loses la')
            return True
    return False


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('game')

display = pygame.Surface(screen.get_size())
display = display.convert()
display.fill((0, 0, 0))
player1 = Player(30, 30, headcolor=(132,112,255),trailcolor=(0,255,0))
player2 = Player(780, 580, (255,112,132), trailcolor=(255,0,255))
clock = pygame.time.Clock()

done = False

while not done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.moveUp()
            if event.key == pygame.K_DOWN:
                player1.moveDown()
            if event.key == pygame.K_RIGHT:
                player1.moveRight()
            if event.key == pygame.K_LEFT:
                player1.moveLeft()
            if event.key == pygame.K_w:
                player2.moveUp()
            if event.key == pygame.K_s:
                player2.moveDown()
            if event.key == pygame.K_d:
                player2.moveRight()
            if event.key == pygame.K_a:
                player2.moveLeft()

    if not checkCollision(player1, player2):
        player1.move()
        player2.move()
    screen.blit(display, (0, 0))
    player1.show()
    player2.show()
    pygame.display.flip()
pygame.quit()
