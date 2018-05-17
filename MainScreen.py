import Colors
import pygame
from Label import Label
from Settings import *

class MainScreen:
    def __init__(self):
        self.gameTitle = "Trail Blazers"
        self.easy = "F1             Easy Mode"
        self.normal = "        F2            Normal Mode"
        self.hard = "F3            Hard Mode"
        self.about = "Game    Developers:      jjjimenez100     &&     jh-diaz"
        self.images = "Image and Music   Resources:  opengameart.org"
        self.fonts = "Font   Family     Resources:     font1001.com"
        #self.music = pygame.mixer.Sound("bg.ogg").play(-1)
        self.mainColor = Colors.YELLOW1
        self.secondaryColor = Colors.WHITE
        self.aboutFontSize = Settings.SCREEN_WIDTH // 50
        self.gameTitleFontSize = Settings.SCREEN_WIDTH // 10
        self.modesFontSize = Settings.SCREEN_WIDTH // 25

    def initLabels(self) -> [Label]:
        labels = []
        labels.append(Label("MainFont.otf", self.gameTitle, self.gameTitleFontSize, Colors.YELLOW1,
                              (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2) - 120)))
        labels.append(Label("MainFont.otf", self.easy, self.modesFontSize, Colors.YELLOW1,
                         (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2) - 35)))
        labels.append(Label("MainFont.otf", self.normal, self.modesFontSize, Colors.YELLOW1,
                           (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2) + 5)))
        labels.append(Label("MainFont.otf", self.hard, self.modesFontSize, Colors.YELLOW1,
                         (Settings.SCREEN[0] // 2, (Settings.SCREEN[1] // 2) + 45)))
        labels.append(Label("Cunia.ttf", self.about, self.aboutFontSize, Colors.WHITE,
                          (Settings.SCREEN[0] // 2, Settings.SCREEN[1] - 75)))
        labels.append(Label("Cunia.ttf", self.images, self.aboutFontSize, Colors.WHITE,
                           (Settings.SCREEN[0] // 2, Settings.SCREEN[1] - 55)))
        labels.append(Label("Cunia.ttf", self.fonts, self.aboutFontSize, Colors.WHITE,
                          (Settings.SCREEN[0] // 2, Settings.SCREEN[1] - 35)))

        return labels

