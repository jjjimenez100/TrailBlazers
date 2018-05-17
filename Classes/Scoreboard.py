import Classes.Label as l
from Classes.Utilities import *
from Settings import *

class Scoreboard():
    def __init__(self):
        self.p1score = 0
        self.p2score = 0
        self.title = l.Label(32)
        self.title.text = 'Scoreboard'
        self.title.center = Settings.SCREEN_WIDTH/2, 16
        sprites.add(self.title)
        self.playerTitle = l.Label(24)
        self.playerTitle.text = 'Player 1 | Player 2'
        self.playerTitle.center = Settings.SCREEN_WIDTH/2, 44
        sprites.add(self.playerTitle)
        self.p1scorelbl = l.Label(24)
        self.p1scorelbl.text = str(self.p1score)
        self.p1scorelbl.center = Settings.SCREEN_WIDTH/2 - 50, 72
        sprites.add(self.p1scorelbl)
        self.p2scorelbl = l.Label(24)
        self.p2scorelbl.text = str(self.p2score)
        self.p2scorelbl.center = Settings.SCREEN_WIDTH/2 + 50, 72
        sprites.add(self.p2scorelbl)

    def addScore(self, player):
        if player=='p1':
            self.p1score+=1
            self.p1scorelbl.text = str(self.p1score)
        if player=='p2':
            self.p2score+=1
            self.p2scorelbl.text = str(self.p2score)
