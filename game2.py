from Settings import Settings
from Classes.Utilities import *
from Classes.Label import Label
from Classes.Scoreboard import Scoreboard
from Classes.Player import Player
from Classes.MainScreen import MainScreen
from Classes.InstructionScreen import InstructionScreen
import pygame

def Gameover(winner: str, text: str):
    sprites.empty()
    sprites.add(text)
    text.text = winner + ' wins!'


def restart(player1, player2):
    player1.restart(1)
    player2.restart(2)
    sprites.remove(trails)
    trails.empty()


def redrawScreen(screen, display, sprites):
    sprites.clear(screen, display)
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()


def createGameScreen(labels):
    spriteGroup = pygame.sprite.Group()
    for label in labels:
        spriteGroup.add(label)

    return spriteGroup


def initMainScreen():
    playOrStopMusic()
    return createGameScreen(MainScreen().initLabels())

def initInstructionsScreen():
    return createGameScreen(InstructionScreen().initLabels())

def playOrStopMusic(playBack: bool = True):
    if (playBack):
        #GAME = pygame.mixer.Sound(Settings.SOUNDS_DIRECTORY+"bg.ogg").play(-1)
        pass

def init():
    pygame.init()
    screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
    pygame.display.set_caption(Settings.GAME_TITLE)
    display = pygame.image.load(Settings.IMAGES_DIRECTORY + "spaceBackground.png")
    display = pygame.transform.scale(display, (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
    screen.blit(display, (0, 0))
    gameover = Label(32)
    sb = Scoreboard()

    p1 = Player(1)
    p2 = Player(2)

    clock = pygame.time.Clock()

    startingTimer = 4
    counter = startingTimer

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    countdown = Label(64)
    countdown.text = str(counter-1)
    sprites.add(countdown)
    countdownFinished = False

    fps = 60
    done = False
    p1creating, p2creating = False, False
    gameScreen = True
    instructions = False

    gameScreenSprites = initMainScreen()
    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if not gameScreen:
                if event.type == pygame.USEREVENT and not countdownFinished:
                    counter -= 1
                    if counter > 0:
                        pygame.mixer.Sound("resources/sounds/select.ogx").play()
                        countdown.text = str(counter)
                    else:
                        countdownFinished = True
                        countdown.text = ''
                        p1.changeDirection('down')
                        p2.changeDirection('up')
                if event.type == pygame.KEYDOWN and countdownFinished:
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
                if event.type == pygame.KEYUP and countdownFinished:
                    if event.key == pygame.K_SPACE:
                        p1creating = False
                    if event.key == pygame.K_RETURN:
                        p2creating = False
            elif instructions:
                # Instruction screen keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        instructions = False
                        gameScreen = False
                        gameScreenSprites.clear(screen, display)

            else:
                # Game Screen keys
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound("resources/sounds/select.ogx").play()
                    if event.key == pygame.K_F1 or event.key == pygame.K_F2 or event.key == pygame.K_F3:
                        if event.key == pygame.K_F1:
                            Settings.GAME_DIFFICULTY = 0
                            p1.changeDifficulty(0)
                            p2.changeDifficulty(0)
                        elif event.key == pygame.K_F2:
                            Settings.GAME_DIFFICULTY = 1
                            p1.changeDifficulty(1)
                            p2.changeDifficulty(1)
                        elif event.key == pygame.K_F3:
                            Settings.GAME_DIFFICULTY = 2
                            p1.changeDifficulty(2)
                            p2.changeDifficulty(2)
                        gameScreenSprites.clear(screen, display)
                        gameScreenSprites = initInstructionsScreen()
                        instructions = True

        if not gameScreen:
            if p1creating:
                p1.createTrail()
            if p2creating:
                p2.createTrail()

            for i in range(0, len(p1.trails)):
                if p2.rect.colliderect(p1.trails[i]) and countdownFinished:
                    if not p2.exploded:
                        p2.explode()
                    p1.stop()
                    if not p2.exploding:
                        countdownFinished = False
                        restart(p1, p2)
                        sb.addScore('p1')
                        counter = startingTimer
                        p1creating, p2creating = False, False
                    break
                if i - (len(p1.trails) - 5) < 0 and p1.rect.colliderect(p1.trails[i]) and countdownFinished:
                    if not p1.exploded:
                        p1.explode()
                    p2.stop()
                    if not p1.exploding:
                        countdownFinished = False
                        restart(p1, p2)
                        sb.addScore('p2')
                        counter = startingTimer
                        p1creating, p2creating = False, False
                    break
            for i in range(0, len(p2.trails)):
                if p1.checkOutOfBounds() or p1.rect.colliderect(p2.trails[i]) and countdownFinished:
                    if not p1.exploded:
                        p1.explode()
                    p2.stop()
                    if not p1.exploding:
                        countdownFinished = False
                        restart(p1, p2)
                        sb.addScore('p2')
                        counter = startingTimer
                        p1creating, p2creating = False, False
                    break
                if i - (len(p2.trails) - 5) < 0 and p2.rect.colliderect(p2.trails[i]) and countdownFinished:
                    if not p2.exploded:
                        p2.explode()
                    p1.stop()
                    if not p2.exploding:
                        countdownFinished = False
                        restart(p1, p2)
                        sb.addScore('p1')
                        counter = startingTimer
                        p1creating, p2creating = False, False
                    break

            if sb.p1score >= Settings.GAMEPLAY_MAX_SCORE:
                Gameover('Player 1', gameover)
            if sb.p2score >= Settings.GAMEPLAY_MAX_SCORE:
                Gameover('Player 2', gameover)

            if p2.checkOutOfBounds():
                if not p2.exploded:
                    p2.explode()
                p1.stop()
                if not p2.exploding:
                    countdownFinished = False
                    restart(p1, p2)
                    sb.addScore('p1')
                    counter = startingTimer
                    p1creating, p2creating = False, False
            if p1.checkOutOfBounds():
                if not p1.exploded:
                    p1.explode()
                p2.stop()
                if not p1.exploding:
                    countdownFinished = False
                    restart(p1, p2)
                    sb.addScore('p2')
                    counter = startingTimer
                    p1creating, p2creating = False, False
            if p1.rect.colliderect(p2.rect):
                if not p1.exploded:
                    p1.explode()
                if not p2.exploded:
                    p2.explode()
                if not p2.exploding:
                    restart(p1, p2)
                    counter = startingTimer
                    countdownFinished = False
                    p1creating, p2creating = False, False

            redrawScreen(screen, display, sprites)
        else:
            redrawScreen(screen, display, gameScreenSprites)

    pygame.quit()
    quit()


if __name__ == '__main__':
    init()

