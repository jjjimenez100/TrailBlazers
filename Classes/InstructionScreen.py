from Classes import Colors
from Classes.MenuLabel import Label
from Settings import *
class InstructionScreen:
    def __init__(self):
        self.gameInstructions = "Game Instructions"

        self.playerOneMovement = "Player One Movement:"
        self.playerOneUp = "W - Up"
        self.playerOneDown = "S - Down"
        self.playerOneRight = "A - Left"
        self.playerOneLeft = "D - Right"
        self.playerOneTrail = "Spacebar - Trail"

        self.playerTwoMovement = "Player Two Movement"
        self.playerTwoUp = "Up Arrow - Up"
        self.playerTwoDown = "Down Arrow - Down"
        self.playerTwoRight = "Right Arrow - Right"
        self.playerTwoLeft = "Left Arrow - Left"
        self.playerTwoTrail = "Enter - Trail"

        self.wallCollisions = "There are wall collisions on hard mode."
        self.trailInstruction = " Just let your opponent hit your trail."

        self.toContinue = " Press spacebar to continue"

        self.secondaryFontSize = (Settings.SCREEN_WIDTH//10)-65
        self.primaryFontSize = (Settings.SCREEN_WIDTH//10)-40

        self.primaryColor = Colors.YELLOW1
        self.secondaryColor = Colors.WHITE
    def initLabels(self) -> [Label]:
        labels = []

        labels.append(Label(Settings.MAIN_FONT, self.gameInstructions, self.primaryFontSize, self.primaryColor,
                                    (Settings.SCREEN[0] / 2, 50)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneMovement, self.secondaryFontSize, self.primaryColor,
                                    (Settings.SCREEN[0] / 2, 100)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneUp, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 120)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneDown, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 140)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneLeft, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 160)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneRight, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 180)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerOneTrail, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 200)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoMovement, self.secondaryFontSize, self.primaryColor,
                                    (Settings.SCREEN[0] / 2, 240)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoUp, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 260)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoDown, self.secondaryFontSize, self.secondaryColor,
                                       (Settings.SCREEN[0] / 2, 280)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoLeft, self.secondaryFontSize, self.secondaryColor,
                                       (Settings.SCREEN[0] / 2, 300)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoRight, self.secondaryFontSize, self.secondaryColor,
                                        (Settings.SCREEN[0] / 2, 320)))
        labels.append(Label(Settings.SECONDARY_FONT, self.playerTwoTrail, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 340)))
        labels.append(Label(Settings.SECONDARY_FONT, self.wallCollisions, self.secondaryFontSize, self.primaryColor,
                                    (Settings.SCREEN[0] / 2, 390)))
        labels.append(Label(Settings.SECONDARY_FONT, self.trailInstruction, self.secondaryFontSize, self.primaryColor,
                                     (Settings.SCREEN[0] / 2, 410)))
        labels.append(Label(Settings.SECONDARY_FONT, self.toContinue, self.secondaryFontSize, self.secondaryColor, (Settings.SCREEN[0] / 2, 460)))

        return labels
