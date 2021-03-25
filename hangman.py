#variables
import pygame
import random
import re
newran = ''
word = ''
new = ''

pygame.init()
#screen dimensions
screen = pygame.display.set_mode((800, 600))
#name/logo
pygame.display.set_caption("Hangman")
icon = pygame.image.load('51Wm6VppYEL.png')
pygame.display.set_icon(icon)
#colors
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#hangman base
hangbase = pygame.image.load('download.v3.png')
hangbaseX = 217
hangbaseY = 60
#hangman head
manhead = pygame.image.load('2download.png')
manheadX = 270.5
manheadY = 163
#text
font = pygame.font.Font(None, 50)
texttop = font.render('select a difficulty', True, black)
textleft = font.render('easy', True, black)
textmid = font.render('medium', True, black)
textright = font.render('hard', True, black)

textA = font.render('a', True, black)
textB = font.render('b', True, black)
textC = font.render('c', True, black)
textD = font.render('d', True, black)
textE = font.render('e', True, black)
textF = font.render('f', True, black)
textG = font.render('g', True, black)
textH = font.render('h', True, black)
textI = font.render('i', True, black)
textJ = font.render('j', True, black)
textK = font.render('k', True, black)
textL = font.render('l', True, black)
textM = font.render('m', True, black)
textN = font.render('n', True, black)
textO = font.render('o', True, black)
textP = font.render('p', True, black)
textQ = font.render('q', True, black)
textR = font.render('r', True, black)
textS = font.render('s', True, black)
textT = font.render('t', True, black)
textU = font.render('u', True, black)
textV = font.render('v', True, black)
textW = font.render('w', True, black)
textX = font.render('x', True, black)
textY = font.render('y', True, black)
textZ = font.render('z', True, black)

        
#text dimensions
textRectop = texttop.get_rect()
textRectop.center = (800//2, 425)

textRecleft = textleft.get_rect()
textRecleft.center = (250, 475)

textRecmid = textmid.get_rect()
textRecmid.center = (800//2, 475)

textRecright = textright.get_rect()
textRecright.center = (550, 475)

recA = textA.get_rect()
recA.center = (250,405)

recB = textB.get_rect()
recB.center = (290,405)

recC = textC.get_rect()
recC.center = (330,405)

recD = textD.get_rect()
recD.center = (370,405)

recE = textE.get_rect()
recE.center = (410,405)

recF = textF.get_rect()
recF.center = (450,405)

recG = textG.get_rect()
recG.center = (490,405)

recH = textH.get_rect()
recH.center = (540,405)

recI = textI.get_rect()
recI.center = (290,455)

recJ = textJ.get_rect()
recJ.center = (330,455)

recK = textK.get_rect()
recK.center = (370,455)

recL = textL.get_rect()
recL.center = (410,455)

recM = textM.get_rect()
recM.center = (450,455)

recN = textN.get_rect()
recN.center = (490,455)

recO = textO.get_rect()
recO.center = (290,505)

recP = textP.get_rect()
recP.center = (330,505)

recQ = textQ.get_rect()
recQ.center = (370,505)

recR = textR.get_rect()
recR.center = (410,505)

recS = textS.get_rect()
recS.center = (450,505)

recT = textT.get_rect()
recT.center = (490,505)

recU = textU.get_rect()
recU.center = (290,555)

recV = textV.get_rect()
recV.center = (330,555)

recW = textW.get_rect()
recW.center = (370,555)

recX = textX.get_rect()
recX.center = (410,555)

recY = textY.get_rect()
recY.center = (450,555)

recZ = textZ.get_rect()
recZ.center = (490,555)





#hangman base function
def base():
    screen.blit(hangbase, (hangbaseX, hangbaseY))
#functions for easy, medium, difficult click
def difclicke():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecleft).collidepoint(pos):
        return True
    return False

def difclickm():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecmid).collidepoint(pos):
        return True
    return False

def difclickh():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecright).collidepoint(pos):
        return True
    return False
#funciton for reseting screen
def letters():
    screen.blit(textA, recA)
    screen.blit(textB, recB)
    screen.blit(textC, recC)
    screen.blit(textD, recD)
    screen.blit(textE, recE)
    screen.blit(textF, recF)
    screen.blit(textG, recG)
    screen.blit(textH, recH)
    screen.blit(textI, recI)
    screen.blit(textJ, recJ)
    screen.blit(textK, recK)
    screen.blit(textL, recL)
    screen.blit(textM, recM)
    screen.blit(textN, recN)
    screen.blit(textO, recO)
    screen.blit(textP, recP)
    screen.blit(textQ, recQ)
    screen.blit(textR, recR)
    screen.blit(textS, recS)
    screen.blit(textT, recT)
    screen.blit(textU, recU)
    screen.blit(textV, recV)
    screen.blit(textW, recW)
    screen.blit(textX, recX)
    screen.blit(textY, recY)
    screen.blit(textZ, recZ)

def blanksc():
    global newran
    while running:
        screen.fill(white)
        base()
        font = pygame.font.Font(None, 90)
        newtxt = font.render(str(newran), True, black)
        textRecran = newtxt.get_rect()
        textRecran.center = (800//2, 100)
        screen.blit(newtxt, textRecran)
        letters()
        pygame.display.update()
 
#function for selecting difficulty
def selection():
    #write for loop, for len(rword), screen.blit x amount of _'s
    global newran
    global word
    screen.blit(texttop, textRectop)
    screen.blit(textleft, textRecleft)
    screen.blit(textmid, textRecmid)
    screen.blit(textright, textRecright)
    base()

    with open("wordlist.txt", 'r') as file:
        data = file.readlines()
        data = ''.join(data)

        if difclicke() == True:
            strl = ''
            wordlist = re.findall(r'\b[a-zA-Z]{4,5}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word, blanksc())

        elif difclickm() == True:
            strl = ''
            wordlist = re.findall(r'\b[a-zA-Z]{6}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word, blanksc())

        elif difclickh() == True:
            wordlist = re.findall(r'\b[a-zA-Z]{7}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word, new, blanksc())

def guess():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(recA).collidepoint(pos):
        if 'a' in word:
            textA = font.render('a', True, green)
        elif 'a' not in word:
            textA = font.render('a', True, red)
                
        elif pygame.mouse.get_pressed()[0] and pygame.Rect(recB).collidepoint(pos):
            if 'b' in word:
                textB = font.render('b', True, green)
            elif 'b' not in word:
                textB = font.render('b', True, red)
        
def game():
    selection()
    

#main line    
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
    game()

    pygame.display.update()
