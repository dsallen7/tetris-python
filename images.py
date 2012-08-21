import pygame
import random
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('IMG', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    #image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

magicImg = range(7)

for i in range(7):
    magicImg[i], magicRect = load_image('magic'+str(i+1)+'.bmp', -1)

redBlock, redRect = load_image('red.bmp', -1)
blueBlock, blueRect = load_image('blue.bmp', -1)
goldBlock, goldRect = load_image('gold.bmp', -1)
greenBlock, greenRect = load_image('green.bmp', -1)
greyBlock, greyRect = load_image('grey.bmp', -1)
orangeBlock, orangeRect = load_image('orange.bmp', -1)
violetBlock, violetRect = load_image('violet.bmp', -1)

titleScreen ,titleRect = load_image('tetris.bmp', -1)

backImg, backRect = load_image('background.bmp')