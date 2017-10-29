# Modules importeren
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

# Lengte en hoogte definieren
lengthscreen, heightscreen = 400, 400

# Scherm maken
DISPLAYSURF = pygame.display.set_mode((lengthscreen, heightscreen), 0, 32)
pygame.display.set_caption('Appels vangen')

# Kleuren definiëren
#           R     G     B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# Variabelen definiëren
rect1x = 300
rect1y = 325

rect2x = 100
rect2y = 325

ellipse1x = randint(0, 400)
ellipse1y = 0

score1 = 0
score2 = 0
levens1 = 7
levens2 = 7

pauze = False
gameoverm = False
gameovers = False
multiplayer = False
menu = True

valsnelheid = 2

appelgeraakt1 = False
appelgeraakt2 = False


def variabelen():
    global rect1x, rect1y, rect2x, rect2y, rect1x, ellipse1x, ellipse1y, score1, score2, levens1, levens2, pauze, gameoverm, gameovers, multiplayer, menu, valsnelheid, appelgeraakt1, appelgeraakt2
    rect1x = 300
    rect1y = 325

    rect2x = 100
    rect2y = 325

    ellipse1x = randint(0, 400)
    ellipse1y = 0

    score1 = 0
    score2 = 0
    levens1 = 7
    levens2 = 7

    pauze = False
    gameoverm = False
    gameovers = False
    multiplayer = False
    menu = True

    valsnelheid = 2

    appelgeraakt1 = False
    appelgeraakt2 = False


variabelen()
# Font maken
fontObj1 = pygame.font.Font('freesansbold.ttf', 15)
fontObj2 = pygame.font.Font('freesansbold.ttf', 30)
fontObj3 = pygame.font.Font('freesansbold.ttf', 23)
fontObj4 = pygame.font.Font('freesansbold.ttf', 15)
fontObj5 = pygame.font.Font('freesansbold.ttf', 10)

# Teksten maken
textlevens1 = fontObj1.render('Levens B: %s' % levens1, True, BLACK)
textscore1 = fontObj1.render('Score B: %s' % score1, True, BLACK)
textlevens2 = fontObj1.render('Levens O: %s' % levens2, True, BLACK)
textscore2 = fontObj1.render('Score O: %s' % score2, True, BLACK)
textpauze = fontObj2.render('PAUZE', True, BLACK)
texthome = fontObj2.render('AppelSpel', True, BLACK)
textplayermodem = fontObj3.render('Multiplayer', True, BLACK)
textplayermodes = fontObj3.render('Singleplayer', True, BLACK)
textplay = fontObj5.render('Om te spelen druk op spatiebalk', True, BLACK)
textswitchmultisingleplayer = fontObj5.render('Druk op P om te switchen tussen single- en multiplayer', True,
                                              BLACK)

textBwin = fontObj2.render('Speler B heeft gewonnen!', True, NAVYBLUE)
textOwin = fontObj2.render('Speler O heeft gewonnen!', True, ORANGE)
textgelijkspel = fontObj2.render('Gelijkspel!', True, BLACK)
textgameover = fontObj2.render('GAME OVER!', True, BLACK)

textterugnaarspel = fontObj4.render('Druk op ESC om terug naar het spel te gaan', True, BLACK)
textterugnaarhomescherm = fontObj4.render('Druk op H om naar het homescherm te gaan', True, BLACK)
textopnieuw = fontObj4.render('Klik op een willekeurige toets om opnieuw te beginnen', True, BLACK)

# !!!Hier altijd alle vormen tekenen, ook al komt het later pas in het spel!!!
pygame.draw.rect(DISPLAYSURF, NAVYBLUE, (rect1x, rect1y, 50, 50))
pygame.draw.rect(DISPLAYSURF, ORANGE, (rect2x, rect2y, 50, 50))
pygame.draw.ellipse(DISPLAYSURF, RED, (ellipse1x, ellipse1y, 50, 50))


# controleren of twee vormen elkaar raken
def vormenraken(vorm1x, vorm2x, vorm1y, vorm2y, width, height, vorm):
    if vorm == "circle":
        if vorm1x >= vorm2x - width / 2 and vorm1x <= vorm2x + width / 2 and vorm1y >= vorm2y - height / 2 and vorm1y <= vorm2y + height / 2:
            return True
        else:
            return False
    elif vorm == "rect":
        if vorm1x >= vorm2x and vorm1x <= vorm2x + width and vorm1y >= vorm2y and vorm1y <= vorm2y + height:
            return True
        else:
            return False


def vormrand(vormx):
    if vormx >= 400:
        vormx = 0
    elif vormx <= 0:
        vormx = 400
    return vormx


def appelgrond(vormy, vormx):
    global levens1, levens2
    if vormy >= 400:
        vormy = 0
        vormx = randint(0, 400)
        levens1 -= 1
        levens2 -= 1
        return vormy, vormx
    else:
        return vormy, vormx


def appelzijkant(vormx):
    if vormx < 25:
        vormx = randint(0, 400)
    if vormx > 375:
        vormx = randint(0, 400)
    return vormx


# Game loop
while True:
    # Scherm wit maken
    DISPLAYSURF.fill(WHITE)
    if not pauze and not gameoverm and not gameovers and not menu and multiplayer:
        for event in pygame.event.get():
            # Controleren of moet worden afgesloten
            if event.type == QUIT or event.type == KEYUP and event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
            # Kijken of toets wordt ingedrukt en vierkant bewegen
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    rect1x += 20
                elif event.key == K_LEFT:
                    rect1x -= 20
                if event.key == K_d:
                    rect2x += 20
                elif event.key == K_a:
                    rect2x -= 20
                elif event.key == K_c:
                    levens1 = 10000
                    levens2 = 10000
                elif event.key == K_p:
                    variabelen()

            # Kijken of de ESC wordt ingedrukt zo ja -> pauze
            if event.type == KEYUP and event.key == K_ESCAPE:
                pauze = True
        # Appel verplaatsen
        ellipse1y += valsnelheid

        # kijken of het vierkant in de zijkant zit
        rect1x = vormrand(rect1x)
        rect2x = vormrand(rect2x)

        # Controleren of appel grond raakt
        ellipse1y, ellipse1x = appelgrond(ellipse1y, ellipse1x)

        # Controleren of appel vierkant raakt
        if vormenraken(rect1x, ellipse1x, rect1y, ellipse1y, 50, 50, "circle"):
            appelgeraakt1 = True
            score1 += 1
            if score1 == 10 or score1 == 20 or score1 == 30 or score1 == 40 or score1 == 50 or score1 == 60:
                valsnelheid += 1
        if vormenraken(rect2x, ellipse1x, rect2y, ellipse1y, 50, 50, "circle"):
            appelgeraakt2 = True
            score2 += 1
            if score2 == 10 or score2 == 20 or score2 == 30 or score2 == 40 or score2 == 50 or score2 == 60:
                valsnelheid += 1

        if appelgeraakt1 == True and appelgeraakt2 == False:
            levens2 -= 1
        elif appelgeraakt2 == True and appelgeraakt1 == False:
            levens1 -= 1

        if appelgeraakt1 or appelgeraakt2:
            ellipse1y = 0
            ellipse1x = randint(0, 400)

        appelgeraakt1 = False
        appelgeraakt2 = False

        # Controleren of levens op zijn
        if levens1 == 0 and levens2 == 0:
            if score1 > score2:
                gameoverm = True
                pygame.time.wait(2000)
            elif score2 > score1:
                gameoverm = True
                pygame.time.wait(2000)
            else:
                gameoverm = True
                pygame.time.wait(2000)

        elif levens1 == 0 and levens2 > 0:
            gameoverm = True
            pygame.time.wait(2000)

        elif levens2 == 0 and levens1 > 0:
            gameoverm = True
            pygame.time.wait(2000)

        # Controleren of appel in zijkant zit
        ellipse1x = appelzijkant(ellipse1x)

        # Tekst en vormen tekenen
        textlevens1 = fontObj1.render('Levens B: %s' % levens1, True, BLACK)
        textscore1 = fontObj1.render('Score B: %s' % score1, True, BLACK)
        textlevens2 = fontObj1.render('Levens O: %s' % levens2, True, BLACK)
        textscore2 = fontObj1.render('Score O: %s' % score2, True, BLACK)

        pygame.draw.ellipse(DISPLAYSURF, RED, (ellipse1x, ellipse1y, 50, 50))
        pygame.draw.rect(DISPLAYSURF, NAVYBLUE, (rect1x, rect1y, 50, 50))
        pygame.draw.rect(DISPLAYSURF, ORANGE, (rect2x, rect2y, 50, 50))

        DISPLAYSURF.blit(textscore1, (5, 5))
        DISPLAYSURF.blit(textlevens1, (315, 5))
        DISPLAYSURF.blit(textscore2, (5, 20))
        DISPLAYSURF.blit(textlevens2, (315, 20))

    # Singleplayer
    elif not pauze and not gameoverm and not gameovers and not menu:
        for event in pygame.event.get():
            # Controleren of moet worden afgesloten
            if event.type == QUIT or event.type == KEYUP and event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
            # Kijken of toets wordt ingedrukt en vierkant bewegen
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    rect1x += 20
                elif event.key == K_LEFT:
                    rect1x -= 20
                elif event.key == K_c:
                    levens = 1000
                elif event.key == K_p:
                    variabelen()
                    multiplayer = True

                elif event.key == K_c:
                    levens1 = 10000
                    levens2 = 10000
            # Kijken of de ESC wordt ingedrukt zo ja -> pauze
            if event.type == KEYUP and event.key == K_ESCAPE:
                pauze = True

        # Appel verplaatsen
        ellipse1y += valsnelheid

        # kijken of het vierkant in de zijkant zit
        rect1x = vormrand(rect1x)

        # Controleren of appel grond raakt
        ellipse1y, ellipse1x = appelgrond(ellipse1y, ellipse1x)

        # Controleren of appel vierkant raakt
        if vormenraken(rect1x, ellipse1x, rect1y, ellipse1y, 50, 50, "circle"):
            ellipse1y = 0
            ellipse1x = randint(0, 400)
            score1 += 1
            if score1 == 10 or score1 == 20 or score1 == 30 or score1 == 40 or score1 == 50 or score1 == 60:
                valsnelheid += 1

        # Controleren of levens op zijn
        if levens1 == 0:
            gameovers = True
            pygame.time.wait(2000)

        # Controleren of appel in zijkant zit
        ellipse1x = appelzijkant(ellipse1x)

        # Tekst en vormen tekenen
        textlevens1 = fontObj1.render('Levens: %s' % levens1, True, BLACK)
        textscore1 = fontObj1.render('Score: %s' % score1, True, BLACK)
        pygame.draw.ellipse(DISPLAYSURF, RED, (ellipse1x, ellipse1y, 50, 50))
        pygame.draw.rect(DISPLAYSURF, NAVYBLUE, (rect1x, rect1y, 50, 50))
        DISPLAYSURF.blit(textscore1, (5, 5))
        DISPLAYSURF.blit(textlevens1, (320, 5))
    # pauzescherm
    elif not gameoverm and not gameovers and not menu:
        for event in pygame.event.get():
            all_keys = pygame.key.get_pressed()
            # Controleren of moet worden afgesloten
            if event.type == QUIT or event.type == KEYUP and event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
            # Kijken of de ESC wordt ingedrukt zo ja -> start
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pauze = False
                elif event.key == K_h:
                    menu = True
                    pauze = False
                    pass

        if multiplayer:
            # Teksten tekenen
            textlevens1 = fontObj1.render('Levens B: %s' % levens1, True, BLACK)
            textscore1 = fontObj1.render('Score B: %s' % score1, True, BLACK)
            textlevens2 = fontObj1.render('Levens O: %s' % levens2, True, BLACK)
            textscore2 = fontObj1.render('Score O: %s' % score2, True, BLACK)

            DISPLAYSURF.blit(textpauze, (
            ((lengthscreen / 2) - (fontObj2.size('PAUZE')[0] / 2)), heightscreen - (heightscreen / 6) * 5))
            DISPLAYSURF.blit(textterugnaarspel, (
            ((lengthscreen / 2) - (fontObj4.size('Druk op ESC om terug naar het spel te gaan')[0] / 2)),
            heightscreen - (heightscreen / 6) * 4))
            DISPLAYSURF.blit(textterugnaarhomescherm, (
            ((lengthscreen / 2) - (fontObj4.size('Druk op H om naar het homescherm te gaan')[0] / 2)),
            heightscreen - (heightscreen / 6) * 3))
            DISPLAYSURF.blit(textscore1, (5, 5))
            DISPLAYSURF.blit(textlevens1, (315, 5))
            DISPLAYSURF.blit(textscore2, (5, 20))
            DISPLAYSURF.blit(textlevens2, (315, 20))

        else:
            # Teksten tekenen
            textlevens1 = fontObj1.render('Levens: %s' % levens1, True, BLACK)
            textscore1 = fontObj1.render('Score: %s' % score1, True, BLACK)

        DISPLAYSURF.blit(textpauze, (
        ((lengthscreen / 2) - (fontObj2.size('PAUZE')[0] / 2)), heightscreen - (heightscreen / 6) * 5))
        DISPLAYSURF.blit(textterugnaarspel, (
        ((lengthscreen / 2) - (fontObj4.size('Druk op ESC om terug naar het spel te gaan')[0] / 2)),
        heightscreen - (heightscreen / 6) * 4))
        DISPLAYSURF.blit(textterugnaarhomescherm, (
        ((lengthscreen / 2) - (fontObj4.size('Druk op H om naar het homescherm te gaan')[0] / 2)),
        heightscreen - (heightscreen / 6) * 3))
        DISPLAYSURF.blit(textscore1, (5, 5))
        DISPLAYSURF.blit(textlevens1, (315, 5))

    # gameover multiplayer scherm
    elif not menu:
        for event in pygame.event.get():
            # Controleren of moet worden afgesloten
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
                else:
                    variabelen()

        if levens1 == 0 and levens2 == 0:
            if score1 > score2:
                DISPLAYSURF.blit(textBwin, (((lengthscreen / 2) - (fontObj2.size('Speler B heeft gewonnen!')[0] / 2)),
                                            heightscreen - (heightscreen / 6) * 3.5))
            elif score2 > score1:
                DISPLAYSURF.blit(textOwin, (((lengthscreen / 2) - (fontObj2.size('Speler O heeft gewonnen!')[0] / 2)),
                                            heightscreen - (heightscreen / 6) * 3.5))
            else:
                DISPLAYSURF.blit(textgelijkspel, (
                ((lengthscreen / 2) - (fontObj2.size('Gelijkspel!')[0] / 2)), heightscreen - (heightscreen / 6) * 3.5))

        elif levens1 == 0 and levens2 > 0:
            DISPLAYSURF.blit(textOwin, (((lengthscreen / 2) - (fontObj2.size('Speler O heeft gewonnen!')[0] / 2)),
                                        heightscreen - (heightscreen / 6) * 3.5))

        elif levens2 == 0 and levens1 > 0:
            DISPLAYSURF.blit(textBwin, (((lengthscreen / 2) - (fontObj2.size('Speler B heeft gewonnen!')[0] / 2)),
                                        heightscreen - (heightscreen / 6) * 3.5))

        # Teksten tekenen
        textlevens1 = fontObj1.render('Levens B: %s' % levens1, True, BLACK)
        textscore1 = fontObj1.render('Score B: %s' % score1, True, BLACK)
        textlevens2 = fontObj1.render('Levens O: %s' % levens2, True, BLACK)
        textscore2 = fontObj1.render('Score O: %s' % score2, True, BLACK)

        DISPLAYSURF.blit(textgameover, (
        ((lengthscreen / 2) - (fontObj2.size('GAME OVER!')[0] / 2)), heightscreen - (heightscreen / 6) * 4.5))
        DISPLAYSURF.blit(textopnieuw, (
        ((lengthscreen / 2) - (fontObj4.size('Klik op een willekeurige toets om opnieuw te beginnen')[0] / 2)),
        heightscreen - (heightscreen / 6) * 2.5))

        DISPLAYSURF.blit(textscore1, (5, 5))
        DISPLAYSURF.blit(textlevens1, (315, 5))
        DISPLAYSURF.blit(textscore2, (5, 20))
        DISPLAYSURF.blit(textlevens2, (315, 20))
    # Gameover singleplayer
    elif not menu:
        for event in pygame.event.get():
            # Controleren of moet worden afgesloten
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
                else:
                    variabelen()

        textlevens1 = fontObj1.render('Levens: %s' % levens1, True, BLACK)
        textscore1 = fontObj1.render('Score: %s' % score1, True, BLACK)

        DISPLAYSURF.blit(textscore1, (5, 5))
        DISPLAYSURF.blit(textlevens1, (315, 5))
        DISPLAYSURF.blit(textgameover, (
        ((lengthscreen / 2) - (fontObj2.size('GAME OVER!')[0] / 2)), heightscreen - (heightscreen / 6) * 4.5))
        DISPLAYSURF.blit(textopnieuw, (
        ((lengthscreen / 2) - (fontObj4.size('Klik op een willekeurige toets om opnieuw te beginnen')[0] / 2)),
        heightscreen - (heightscreen / 6) * 2.5))
    # Startscherm
    else:
        for event in pygame.event.get():
            # Controleren of moet worden afgesloten
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    menu = False
                elif event.key == K_p:
                    if multiplayer:
                        multiplayer = False
                    elif not multiplayer:
                        multiplayer = True

        DISPLAYSURF.blit(texthome, (
            ((lengthscreen / 2) - (fontObj2.size('AppelSpel')[0] / 2)), heightscreen - (heightscreen / 6) * 5))
        DISPLAYSURF.blit(textplay, (((lengthscreen / 2) - (fontObj5.size('Om te spelen druk op spatiebalk')[0] / 2)),
                                    heightscreen - (heightscreen / 6) * 4))
        DISPLAYSURF.blit(textswitchmultisingleplayer, (
        ((lengthscreen / 2) - (fontObj5.size('Druk op P om te switchen tussen single- en multiplayer')[0] / 2)),
        heightscreen - (heightscreen / 6) * 3))

        if multiplayer:
            DISPLAYSURF.blit(textplayermodem, (
                ((lengthscreen / 2) - (fontObj3.size('Multiplayer')[0] / 2)), heightscreen - (heightscreen / 6) * 2))
        else:
            DISPLAYSURF.blit(textplayermodes, (
                ((lengthscreen / 2) - (fontObj3.size('Singleplayer')[0] / 2)), heightscreen - (heightscreen / 6) * 2))
    # Scherm updaten
    pygame.display.update()
    fpsClock.tick(FPS)
