import pygame
import random
import os

from data import *
from images import *

class piece(pygame.sprite.Sprite):
    def __init__(self):
        self.rotationCount = 0
        self.piece = 0
        
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        #draw shapes of pieces
        pieceO = range(2)
        Opoints = [(0,0), (50,0), (50,50), (0,50)]
        pieceO[0] = pygame.Surface( (50,50) )
        pieceO[1] = pygame.Surface( (50,50) )
        for L in Oblocks:
            for C in L:
                pieceO[Oblocks.index(L)].blit(redBlock, C )
        #pygame.draw.polygon(pieceO[0], red, Opoints)
        #pygame.draw.polygon(pieceO[1], red, Opoints)

        pieceL = range(4)
        pieceL[0] = pygame.Surface( (50,75) )
        pieceL[1] = pygame.Surface( (75,50) )
        pieceL[2] = pygame.Surface( (50,75) )
        pieceL[3] = pygame.Surface( (75,50) )
        for L in Lblocks:
            for C in L:
                pieceL[Lblocks.index(L)].blit(blueBlock, C )

        pieceJ = range(4)
        pieceJ[0] = pygame.Surface( (50,75) )
        pieceJ[1] = pygame.Surface( (75,50) )
        pieceJ[2] = pygame.Surface( (50,75) )
        pieceJ[3] = pygame.Surface( (75,50) )
        for L in Jblocks:
            for C in L:
                pieceJ[Jblocks.index(L)].blit(goldBlock, C )

        pieceI = range(2)
        pieceI[0] = pygame.Surface( (25,100) )
        pieceI[1] = pygame.Surface( (100,25) )
        for L in Iblocks:
            for C in L:
                pieceI[Iblocks.index(L)].blit(greenBlock, C )

        pieceS = range(2)
        pieceS[0] = pygame.Surface( (50,75) )
        pieceS[1] = pygame.Surface( (75,50) )
        for L in Sblocks:
            for C in L:
                pieceS[Sblocks.index(L)].blit(violetBlock, C )

        pieceZ = range(2)
        pieceZ[0] = pygame.Surface( (50,75) )
        pieceZ[1] = pygame.Surface( (75,50) )
        for L in Zblocks:
            for C in L:
                pieceZ[Zblocks.index(L)].blit(orangeBlock, C )
        
        pieceT = range(4)
        pieceT[0] = pygame.Surface( (75,50) )
        pieceT[1] = pygame.Surface( (50,75) )
        pieceT[2] = pygame.Surface( (75,50) )
        pieceT[3] = pygame.Surface( (50,75) )
        for L in Tblocks:
            for C in L:
                pieceT[Tblocks.index(L)].blit(greyBlock, C )
    
        self.images = [pieceO, pieceL, pieceJ, pieceI, pieceS, pieceZ, pieceT]
        
        for Im in self.images:
            for eachIm in Im:
                eachIm.set_colorkey(black)
        
        #choose a type
        
        i = random.randrange(1,9)        

        self.magicNumber = 1
        
        self.piece = i
        
        self.backToTop(i)

    def backToTop(self, i):
        if i == 1:
            self.location = [(100, 50), (125,50), (100,75), (125,75)]
            self.rect = (100,50,50,50)
            self.piece = 1
        elif i == 2:
            self.location = [(100, 50), (100,75), (100,100), (125,100)]
            self.rect = (100,50,50,75)
            self.piece = 2
        elif i == 3:
            self.location = [(125, 50), (125,75), (125,100), (100,100)]
            self.rect = (100,50,50,75)
            self.piece = 3
        elif i == 4:
            self.location = [(100, 50), (100,75), (100,100), (100,125)]
            self.rect = (100,50,25,100)
            self.piece = 4
        elif i == 5:
            self.location = [(100, 50), (100,75), (125,75), (125,100)]
            self.rect = (100,50,50,75)
            self.piece = 5
        elif i == 6:
            self.location = [(125, 50), (125,75), (100,75), (100,100)]
            self.rect = (100,50,50,75)
            self.piece = 6
        elif i == 7:
            self.location = [(100, 50), (125,50), (150,50), (125,75)]
            self.rect = (100,50,75,50)
            self.piece = 7
        else:
            self.location = [(100, 50), (125,50), (100,75), (125,75)]
            self.rect = (100,50,50,50)
            self.piece = 8
            self.image = magicImg[self.magicNumber]
            return
        self.image = self.images[i-1][0]

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.rotate()
            else:
                self.move(pygame.key.name(event.key))

    def move(self, key):
        (x1,y1,x2,y2) = self.rect
        x = 0
        y = 0
        if key == 'up':
            pass
        elif key == 'down':
            if y1+y2 < 500 and self.checkGrid(0,blocksize) == False:
                y = 25
            else:
                self.restart()
                return
        elif key == 'left':
            if x1 > 0 and self.checkGrid(-blocksize,0) == False:
                x = -25
            else:
                return
        elif key == 'right':
            if x1+x2 < 200 and self.checkGrid(blocksize,0) == False:
                x = 25
            else:
                return
        for i in range(len(self.location)):
            (xloc,yloc) = self.location[i]
            xloc += x
            yloc += y
            self.location[i] = (xloc,yloc)
        x1 += x
        y1 += y
        self.rect = (x1,y1, x2, y2)
        screen.blit(background, (0, 0))

    def fall(self):
        (x1,y1,x2,y2) = self.rect
        y = 0
        if y1+y2 < 500 and self.checkGrid(0,blocksize) == False:
            y = 25
        else:
            self.restart()
            return
        for i in range(len(self.location)):
            (xloc,yloc) = self.location[i]
            yloc += y
            self.location[i] = (xloc,yloc)
        Xpos, Ypos = zip(*self.location)
        self.rect = (min(Xpos),min(Ypos),x2,y2)

    def rotatePiece(self,Rlist,pieceID):
        for idx in range(len(Rlist[self.rotationCount])):
            self.location[idx] = (self.location[idx][0]+Rlist[self.rotationCount][idx][0],
                                self.location[idx][1]+Rlist[self.rotationCount][idx][1])
        if self.rotationCount == len(Rlist)-1:
            self.rotationCount = 0
        else:
            self.rotationCount += 1
        (a,b,c,d) = self.rect
        Xpos, Ypos = zip(*self.location)
        self.rect = (min(Xpos),min(Ypos),d,c)
        self.image = self.images[pieceID][self.rotationCount]

    #Wrapper function for performing rotations
    def rotate(self):
        (x1,y1,x2,y2) = self.rect
        if (x1 > 125) or (x1 < 25):
            return
        if self.piece == 1:
            pass
        elif self.piece == 2:
            self.rotatePiece(Lrotations,1)
        elif self.piece == 3:
            self.rotatePiece(Jrotations,2)
        elif self.piece == 4:
            self.rotatePiece(Irotations,3)
        elif self.piece == 5:
            self.rotatePiece(Srotations,4)
        elif self.piece == 6:
            self.rotatePiece(Zrotations,5)
        elif self.piece == 7:
            self.rotatePiece(Trotations,6)

    def checkGrid(self, Xvalue,Yvalue):
        (a,b,c,d) = self.rect
        
        for t in self.location:
            (x,y) = t
            if myGrid.getBlock((x+Xvalue)/blocksize,(y+Yvalue)/blocksize) != 0:
                return True
        return False

    def restart(self):
        if self.piece == 8:
            myGrid.cascade()
            i = random.randrange(1,9)
            self.rotationCount = 0
            self.backToTop(i)
            return
        #add current block positions to grid
        for t in self.location:
            (x,y) = t
            myGrid.addToGrid(x/blocksize,y/blocksize,self.piece)
        #choose new piece
        i = random.randrange(1,9)
        self.rotationCount = 0
        self.backToTop(i)
    
    def updateMagicNumber(self):
        self.magicNumber = random.randrange(7)
        self.image = magicImg[self.magicNumber]
        

class grid():
    def __init__(self):
        self.Grid = []
        for i in range(rows):
            self.Grid += [columns * [0]]

    def getBlock(self,y,x):
        return self.Grid[x][y]
    
    def setBlock(self,y,x,e):
        self.grid[x][y] = e

    def addToGrid(self, y,x,piece):
        #Adds landed piece to grid
        #self.Grid[x][y] = piece
        
        self.Grid[x] = self.Grid[x][:y] + [piece] + self.Grid[x][y+1:]
        self.redraw()
    
    def getCol(self,x):
        col = []
        for j in range(rows):
            col += [self.getBlock(x,j)]
        return col
            
    def cascade(self):
        for i in range(columns):
            col = self.getCol(i)
            for idx in range( len(col) ):
                if col[idx] == 0:
                    col = [0] + col[:idx] + col[idx+1:]
            for idx in range( len(col) ):
                self.addToGrid(i, idx, col[idx])

    def redraw(self):
        for i in range(rows):
            for j in range(columns):
                if self.Grid[i][j] == 1:
                    block.blit(redBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 2:
                    block.blit(blueBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 3:
                    block.blit(goldBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 4:
                    block.blit(greenBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 5:
                    block.blit(violetBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 6:
                    block.blit(orangeBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )
                elif self.Grid[i][j] == 7:
                    block.blit(greyBlock, (0,0) )
                    screen.blit(block, (j*25, i*25) )

    def printgrid(self):
        for line in self.Grid:
            print line
            print '\n'

    def clearline(self):
        linecount = 0
        for i in range(20):
            if 0 not in self.Grid[i]:
                self.Grid = self.Grid[:i] + self.Grid[i+1:]
                self.Grid = [emptyRow] + self.Grid
                linecount += 1
        myDisplay.recieveScore(10*linecount)

class display():
    def __init__(self):
        self.box = pygame.Surface((300,500))
        self.box.blit(titleScreen, (0,0) )
        self.playerScore = 0
    
    def recieveScore(self, value):
        self.playerScore += value
    
    def update(self):
        self.box = self.box.copy()
        screen.blit(self.box, (200,0) )
        if pygame.font:
            font = pygame.font.SysFont("arial", 26)
            text = font.render( str(self.playerScore), 1, red, black )
            self.box.blit(text, (150,225) )

# Set the height and width of the screen
size=[500,500]
screen=pygame.display.set_mode(size)

#Height and width of a "block" unit
blocksize = 25

rows = 20
columns = 8

emptyRow = 8*[0]

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]
yellow = [255, 255, 127]
violet = [148, 0, 211]
orange = [255, 69, 0]

block = pygame.Surface( (25,25) )

if not pygame.font: print 'Warning, fonts disabled'

pygame.display.set_caption("Tetris")

background = pygame.Surface([200,500])
#background = background.convert()
background.blit( backImg, (0,0) )

pygame.init()
clock = pygame.time.Clock()
random.seed()

pieces = range(1,5)

myPiece = piece()

myGrid = grid()

myDisplay = display()

allsprites = pygame.sprite.RenderPlain((myPiece))

fallcount = 0

DIM = 10

while True:
    clock.tick(10)
    for event in pygame.event.get():
        myPiece.event_handler(event)
        if event.type == pygame.QUIT:
            os.sys.exit()
    screen.blit(background, (0, 0))
    fallcount += 1
    if fallcount == 10:
        myPiece.fall()
        fallcount = 0
    if myPiece.piece == 8:
        myPiece.updateMagicNumber()
    myGrid.redraw()
    myGrid.clearline()
    myDisplay.update()
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip() 
