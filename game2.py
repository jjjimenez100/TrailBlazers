from Settings import *
from Utilities import *
from Classes.Label import Label
from Classes.Scoreboard import Scoreboard
from Classes.Player import Player
from Label import Label as joshLabel
import Colors
import Settings

def Gameover(winner: str, text: str):
    sprites.empty()
    sprites.add(text)
    text.text = winner + ' wins walao sad boi'

def restart(p1, p2):
    p1.restart(1)
    p2.restart(2)
    sprites.remove(trails)
    trails.empty()

def redrawScreen(screen, display):
    sprites.clear(screen, display)
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()

def init():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('game')

    display = pygame.image.load('images/bg.png')
    display = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(display, (0, 0))

    p1 = Player(1)
    p2 = Player(2)
    gameover = Label(32)
    sb = Scoreboard()

    clock = pygame.time.Clock()
    fps = 60
    done = False
    p1creating, p2creating = False, False
    gameScreen = True
    bgMusic = pygame.mixer.Sound("bg.ogg").play(-1)
    gameTitle = joshLabel("MainFont.otf", "Trail Blazers", 50, Colors.YELLOW1,
                          (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2)-120))
    easy = joshLabel("MainFont.otf", "F1             Easy Mode", 20, Colors.YELLOW1,
                          (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2)-35))
    normal = joshLabel("MainFont.otf", "        F2            Normal Mode", 20, Colors.YELLOW1,
                     (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2)+5))
    hard = joshLabel("MainFont.otf", "F3            Hard Mode", 20, Colors.YELLOW1,
                     (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2)+45))
    about = joshLabel("MainFont.otf", "Game    Developers:      jjjimenez100     &&     jh-diaz", 12, Colors.YELLOW1,
                     (Settings.SCREEN[0] // 2, Settings.SCREEN[1]-75))
    images = joshLabel("MainFont.otf", "Image and Music Resources:  opengameart.org", 12, Colors.YELLOW1,
                     (Settings.SCREEN[0] // 2, Settings.SCREEN[1]-55))
    fonts = joshLabel("MainFont.otf", "Font   Family   Resources:     font1001.com", 12, Colors.YELLOW1,
                       (Settings.SCREEN[0] // 2, Settings.SCREEN[1] - 35))
    gameScreenLabels = pygame.sprite.Group(gameTitle, easy, normal, hard, about, images, fonts)

    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if not gameScreen:
                bgMusic.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_LEFT:
                        p2.changeDirection('left')
                    if event.key == pygame.K_RIGHT:
                        p2.changeDirection('right')
                    if event.key == pygame.K_UP:
                        p2.changeDirection('up')
                    if event.key == pygame.K_DOWN:
                        p2.changeDirection('down')
                    if event.key == pygame.K_SPACE:
                        p1creating = True
                    if event.key == pygame.K_w:
                        p1.changeDirection('up')
                    if event.key == pygame.K_s:
                        p1.changeDirection('down')
                    if event.key == pygame.K_a:
                        p1.changeDirection('left')
                    if event.key == pygame.K_d:
                        p1.changeDirection('right')
                    if event.key == pygame.K_RETURN:
                        p2creating = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        p1creating = False
                    if event.key == pygame.K_RETURN:
                        p2creating = False

        if not gameScreen:
            if p1creating:
                p1.createTrail()
            if p2creating:
                p2.createTrail()

            for i in range(0, len(p1.trails)):
                if p2.checkOutOfBounds() or p2.rect.colliderect(p1.trails[i]):
                    # Gameover('p1', gameover)
                    sb.addScore('p1')
                    restart(p1, p2)
                    break
                if i - (len(p1.trails) - 5) < 0 and p1.rect.colliderect(p1.trails[i]):
                    # Gameover('p2', gameover)
                    sb.addScore('p2')
                    restart(p1, p2)
                    break
            for i in range(0, len(p2.trails)):
                if p1.checkOutOfBounds() or p1.rect.colliderect(p2.trails[i]):
                    # Gameover('p2', gameover)
                    sb.addScore('p2')
                    restart(p1, p2)
                    break
                if i - (len(p2.trails) - 5) < 0 and p2.rect.colliderect(p2.trails[i]):
                    # Gameover('p1', gameover)
                    sb.addScore('p1')
                    restart(p1, p2)
                    break

            if p1.rect.colliderect(p2.rect):
                # Gameover('tie', gameover)
                restart(p1, p2)

            redrawScreen(screen, display)
        else:
            gameScreenLabels.clear(screen, display)
            gameScreenLabels.update()
            gameScreenLabels.draw(screen)
            pygame.display.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    init()

