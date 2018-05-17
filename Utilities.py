import pygame


sprites = pygame.sprite.LayeredUpdates()
trails = pygame.sprite.Group()

def loadImage(filePath : str) -> pygame.Surface:
    try:
        image = pygame.image.load(filePath)
    except pygame.error:
        raise SystemExit("Error loading image %s : %s" %(filePath, pygame.get_error()))

    return image

def loadImages(*filePaths : [str]) -> [pygame.Surface]:
    images = []
    for filePath in filePaths:
        images.append(loadImage(filePath))

    return images

def loadSound(filePath : str) -> pygame.mixer.Sound:
    try:
        sound = pygame.mixer.Sound(filePath)
    except pygame.error:
        raise SystemExit("Error loading sound %s : %s" %(filePath, pygame.get_error()))

    return sound

def loadSounds(*filePaths : [str]) -> [pygame.mixer.Sound]:
    sounds = []
    for filePath in filePaths:
        sounds.append(loadSound(filePath))

    return sounds