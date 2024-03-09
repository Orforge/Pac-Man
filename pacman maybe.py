#jeu louis et guillaume

import pygame
import os,sys
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,vie=3,point=0,x=0,y=0):
        pygame.sprite.Sprite.__init__(self)
        carImg = pygame.image.load('start.png')
        carImg.convert()
        self.image = carImg
        self.rect = carImg.get_rect()
        self.vie = vie
        self.point = point
        self.x = x
        self.y = y

    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y

    """def get_pos(self):
        for ligne in niv:
            for block in ligne:
                if block == 7:
                    x = ligne
                    y = block
        return x,y"""


    def comptage1(self):
            self.point +=1

    def get_point(self):
        return self.__point

    def get_vie(self):
        return self.vie

    def point_vie(self):
        self.vie-=1

    def power_up(self):
        n=20
        while n>0:
            n=n-1
            return n


    """def get_pos(self,niv):
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    if block == 7:
                        ligne= self.y
                        block = self.x"""
    def get_posx(self,niv):
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    if block == 7:
                        self.x = x
                        return self.x


    def get_posy(self,niv):
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    if block == 7:
                        self.y = y
                        return self.y


    def get_pos(self, niv):
        for y, ligne in enumerate(niv):
            for x, cell in enumerate(ligne):
                if cell == 7:
                    return (x,y)

    def avancer(self,niv,direction):

        if direction == 'droite':
            self.image = pygame.image.load('start.png')
            pygame.time.wait(150)
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 7 and   niv[x][y+1] == 0   :
                            niv[x][y]=0
                            niv[x][y+1]=7
                            return
                        if  block == 7 and niv[x][y+1] ==17:
                            niv[x][y]=0
                            niv[x][y+1]=7
                            self.comptage1()
                            return
                        if block == 7 and niv[x][y+1] ==32:
                            niv[x][y]=0
                            niv[x][y+1]=7
                            self.power_up()
                            return
                    except IndexError:
                        pass

        if direction == 'gauche':
            self.image = pygame.image.load('gauche.png')
            pygame.time.wait(150)
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 7 and   niv[x][y-1] == 0 :
                            niv[x][y]=0
                            niv[x][y-1]=7
                            return
                        if block == 7 and niv[x][y-1] ==17:
                            niv[x][y]=0
                            niv[x][y-1]=7
                            self.comptage1()
                            return
                        if block == 7 and niv[x][y-1] ==32:
                            niv[x][y]=0
                            niv[x][y-1]=7
                            self.power_up()
                            return
                    except IndexError:
                        pass

        if direction == 'bas':
            self.image = pygame.image.load('bas.png')
            pygame.time.wait(150)
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 7 and   niv[x+1][y] == 0 :
                            niv[x][y]=0
                            niv[x+1][y]=7
                            return
                        if block == 7 and niv[x+1][y] ==17:
                            niv[x][y]=0
                            niv[x+1][y]=7
                            self.comptage1()
                            return
                        if block == 7 and niv[x+1][y] ==32:
                            niv[x][y]=0
                            niv[x+1][y]=7
                            self.power_up()
                            return
                    except IndexError:
                        pass

        if direction == 'haut':
            self.image = pygame.image.load('haut.png')
            pygame.time.wait(150)
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 7 and   niv[x-1][y] == 0 :
                            niv[x][y]=0
                            niv[x-1][y]=7
                            return
                        if block == 7 and niv[x-1][y] ==17:
                            niv[x][y]=0
                            niv[x-1][y]=7
                            self.comptage1()
                            return
                        if block == 7 and niv[x-1][y] ==32:
                            niv[x][y]=0
                            niv[x-1][y]=7
                            self.power_up()
                            return

                    except IndexError:
                        pass
        """
        if direction == 'droite':
            direc= niv[x][y+1]
        if direction == 'gauche':
            direc= niv[x][y-1]
        if direction == 'bas':
            direc= niv[+1][y]
        if direction == 'haut':
            direc= niv[x-1][y]
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):

                    try:

                        if block == 7 and   direc == 0 :
                            niv[x][y]=0
                            direc=7
                            return
                        if block == 7 and direc ==17:
                            niv[x][y]=0
                            direc=7
                            self.comptage1()
                            return
                    except IndexError:
                        pass"""


    def __str__(self):
        return str(self.point), str(self.vie), str(self.x), str(self.y)



class Ghost:
    def __init__(self,direction=None,x=0,y=0):
        pygame.sprite.Sprite.__init__(self)
        Img = pygame.image.load('ghost-blinky.png')
        Img.convert()
        self.image = Img
        self.rect = Img.get_rect()
        self.direction = direction
        self.x = x
        self.y = y

    def choisir_direction(self):
        self.direction  = random.choice(['droite','gauche','bas','haut'])

    def get_posx(self,niv):
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    if block == 24:
                        y= self.x
                        return self.x

    def get_posy(self,niv):
        for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    if block == 24:
                        x= self.y
                        return self.y

    def get_pos(self, niv):
        for y, ligne in enumerate(niv):
            for x, cell in enumerate(ligne):
                if cell == 24:
                    return (x,y)



    def fuite(self,joueur,niv):
        if joueur.power_up:
            self.get_posx(niv)
            self.get_posy(niv)
            joueur.get_posx(niv)
            joueur.get_posy(niv)
            if joueur.get_vie() == 0 :
                return
            self.x, self.y = self.get_pos(niv)
            (x,y) = joueur.get_pos(niv)

            if self.x > x and niv[self.y][self.x-1] in (17, 0,7):
                self.direction = 'droite'

            elif self.x < x and niv[self.y][self.x+1] in (17, 0,7):
                self.direction = 'gauche'
            elif self.y > y and niv[self.y-1][self.x] in (17, 0,7):
                self.direction = 'bas'
            elif self.y < y and niv[self.y+1][self.x] in (17, 0,7):
                self.direction = 'haut'
        else:
           self.direction = 'bas'
        print(self.direction)





    def recherche(self,joueur,niv) :
        self.get_posx(niv)
        self.get_posy(niv)
        joueur.get_posx(niv)
        joueur.get_posy(niv)
        if joueur.get_vie() == 0 :
            return
        self.x, self.y = self.get_pos(niv)
        (x,y) = joueur.get_pos(niv)

        if self.x > x and niv[self.y][self.x-1] in (17, 0,7):
            self.direction = 'gauche'

        elif self.x < x and niv[self.y][self.x+1] in (17, 0,7):
            self.direction = 'droite'
        elif self.y > y and niv[self.y-1][self.x] in (17, 0,7):
            self.direction = 'haut'
        elif self.y < y and niv[self.y+1][self.x] in (17, 0,7):
            self.direction = 'bas'
        else :
            self.direction = 'bas'
        print(self.direction)



##        #ciblex = joueur.get_posx(niv)        cibley =
##        for x,ligne in enumerate( niv):
##                for y,block in enumerate (ligne):
##                    if  self.get_posy(niv) > joueur.get_posy(niv):
##                        self.direction = 'bas'
##                    if  self.get_posy(niv)  < joueur.get_posy(niv):
##                        self.direction = 'bas'
##                    if self.get_posx(niv) > joueur.get_posx(niv):
##                        self.direction = 'gauche'
##                    if self.get_posx(niv) < joueur.get_posx(niv):
##                        self.direction = 'gauche'



#fantôme à tête chercheuse

    def tete_chercheuse(self,niv,joueur):
        self.recherche(joueur,niv)
        """if joueur.power_up():
            self.fuite(joueur,niv)"""
        self.image = pygame.image.load('ghost-blinky.png')
        if self.direction == 'droite':
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 24 and   niv[x][y+1] == 0 :
                            niv[x][y]=0
                            niv[x][y+1]=24
                            return
                        if block == 24 and niv[x][y+1] ==17:
                            niv[x][y]=17
                            niv[x][y+1]=24
                            return
                        if block == 24 and block ==7:
                            niv[x][y]=0
                            niv[x][y+1]=24
                            niv[2][1]=7
                            joueur.point_vie()

                            return

                    except IndexError:
                        pass

        if self.direction == 'gauche':
            self.image = pygame.image.load('ghost-blinky.png')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 24 and   niv[x][y-1] == 0 :
                            niv[x][y]=0
                            niv[x][y-1]=24
                            return
                        if block == 24 and niv[x][y-1] ==17:
                            niv[x][y]=17
                            niv[x][y-1]=24
                            return
                        if block == 24 and niv[x][y-1] ==7:
                            niv[x][y]=0
                            niv[x][y-1]=24
                            niv[2][1]=7
                            joueur.point_vie()
                            return
                    except IndexError:
                        pass

        if self.direction == 'bas':
            self.image = pygame.image.load('ghost-blinky.png')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 24 and   niv[x+1][y] == 0 :
                            niv[x][y]=0
                            niv[x+1][y]=24
                            return
                        if block == 24 and niv[x+1][y] ==17:
                            niv[x][y]=17
                            niv[x+1][y]=24
                            return
                        if block == 24 and niv[x+1][y] ==7:
                            niv[x][y]=0
                            niv[x+1][y]=24
                            niv[2][1]=7
                            joueur.point_vie()
                            return
                    except IndexError:
                        pass

        if self.direction == 'haut':
            self.image = pygame.image.load('ghost-blinky.png')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 24 and   niv[x-1][y] == 0 :
                            niv[x][y]=0
                            niv[x-1][y]=24
                            return
                        if block == 24 and niv[x-1][y] ==17:
                            niv[x][y]=17
                            niv[x-1][y]=24
                            return
                        if block == 24 and  niv[x-1][y] ==7:
                            niv[x][y]=0
                            niv[x-1][y]=24
                            niv[2][1]=7
                            joueur.point_vie()
                            return

                    except IndexError:
                        pass





#fantôme radom


    def avancer(self,niv,joueur):
        self.choisir_direction()
        self.image = pygame.image.load('ghost-inky.gif')
        if self.direction == 'droite':
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    self.image = pygame.image.load('ghost-inky.gif')
                    try:
                        if block == 25 and   niv[x][y+1] == 0 :
                            niv[x][y]=0
                            niv[x][y+1]=25
                            self.choisir_direction()
                            return
                        if block == 25 and niv[x][y+1] ==17:
                            niv[x][y]=17
                            niv[x][y+1]=25
                            self.choisir_direction()
                            return
                        if block == 25 and block ==7:
                            niv[x][y]=0
                            niv[x][y+1]=25
                            niv[2][1]=7
                            joueur.point_vie()
                            self.choisir_direction()

                            return

                    except IndexError:
                        pass

        if self.direction == 'gauche':
            self.image = pygame.image.load('ghost-inky.gif')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 25 and   niv[x][y-1] == 0 :
                            niv[x][y]=0
                            niv[x][y-1]=25
                            self.choisir_direction()
                            return
                        if block == 25 and niv[x][y-1] ==17:
                            niv[x][y]=17
                            niv[x][y-1]=25
                            self.choisir_direction()
                            return
                        if block == 25 and niv[x][y-1] ==7:
                            niv[x][y]=0
                            niv[x][y-1]=25
                            niv[2][1]=7
                            self.choisir_direction()
                            joueur.point_vie()
                            return
                    except IndexError:
                        pass

        if self.direction == 'bas':
            self.image = pygame.image.load('ghost-inky.gif')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 25 and   niv[x+1][y] == 0 :
                            niv[x][y]=0
                            niv[x+1][y]=25
                            self.choisir_direction()
                            return
                        if block == 25 and niv[x+1][y] ==17:
                            niv[x][y]=17
                            niv[x+1][y]=25
                            return
                        if block == 25 and niv[x+1][y] ==7:
                            niv[x][y]=0
                            niv[x+1][y]=25
                            niv[2][1]=7
                            joueur.point_vie()
                            return
                    except IndexError:
                        pass

        if self.direction == 'haut':
            self.image = pygame.image.load('ghost-inky.gif')
            for x,ligne in enumerate( niv):
                for y,block in enumerate (ligne):
                    try:
                        if block == 25 and   niv[x-1][y] == 0 :
                            niv[x][y]=0
                            niv[x-1][y]=25
                            return
                        if block == 25 and niv[x-1][y] ==17:
                            niv[x][y]=17
                            niv[x-1][y]=25
                            return
                        if block == 25 and  niv[x-1][y] ==7:
                            niv[x][y]=0
                            niv[x-1][y]=25
                            niv[2][1]=7
                            joueur.point_vie()
                            return

                    except IndexError:
                        pass


    def __str__(self):
        return  str(self.x), str(self.y)





def affichage(niv):
    global joueur
    x = 0
    y = 0
    for ligne in niv:
        for block in ligne:
            if block == 1:
                screen.blit(mur3,(x,y))
                print(x,y)

            if block == 2:
                    screen.blit(murcoin,(x,y))

            if block == 3:
                    screen.blit(murcoin2,(x,y))

            if block == 4:
                    screen.blit(multicoin,(x,y))

            if block == 5:
                    screen.blit(murcoin4,(x,y))

            if block == 6 :
                    screen.blit(mur,(x,y))

            if block == 7:
                    screen.blit(joueur.image, (x,y))

            if block == 8:
                    screen.blit(murcoin3, (x,y))

            if block == 9:
                    screen.blit(mur, (x,y))

            if block == 10:
                    screen.blit(murfin2, (x,y))

            if block == 11 :
                    screen.blit(murfin3, (x,y))

            if block == 12:
                    screen.blit(murfin4, (x,y))

            if block == 13:
                    screen.blit(murfin, (x,y))

            if block == 14:
                    screen.blit(multicoin2, (x,y))

            if block == 15:
                   screen.blit(murfin2, (x,y))

            if block == 16:
                    screen.blit(murfin2, (x,y))

            if block == 17:
                    screen.blit(manger, (x,y))

            if block == 18:
                    police = pygame.font.Font(None, 25)
                    texte1 = police.render("Score : " + str(joueur.point),True,WHITE)
                    screen.blit(texte1, (x,y))
            if block == 19:
                    screen.blit(multicoin4, (x,y))

            if block == 20:
                    screen.blit(murfin3, (x,y))

            if block == 21:
                    screen.blit(vie, (x,y))


            if block == 22:
                    police = pygame.font.Font(None, 25)
                    texte2 = police.render("" + str(joueur.vie),True,WHITE)
                    screen.blit(texte2, (x,y))

            if block == 23:
                    screen.blit(porte, (x,y))

            if block == 24:
                    screen.blit(fantome, (x,y))

            if block == 25:
                    screen.blit(fantome2, (x,y))
            """
            if block == 28:
                    screen.blit(fond, (x,y))"""
            if block == 32:
                    screen.blit(fond, (x,y))










            x += 16
        x=0
        y += 16




def menu ():
    screen = pygame.display.set_mode((256, 256))
    pygame.mouse.set_visible(True)
    rect = pygame.draw.rect(screen,(255,0,0),pygame.Rect(100, 200, 100, 100))








def init_display():
    global screen, porte, tile, mur, mur2, mur3, mur4, manger, murfin,murfin2, fantome,fond, fantome2, murfin3,murfin4, murcoin,murcoin2, multicoin, multicoin2, multicoin3, multicoin4, carImg, murcoin3, murcoin4, vie
    screen = pygame.display.set_mode((240, 240))
    mur = pygame.image.load('wall.png')
    mur2 = pygame.image.load('wall2.png')
    mur3 = pygame.image.load('wall3.png')
    mur4 = pygame.image.load('wall4.png')
    manger = pygame.image.load('pellet.png')
    murfin = pygame.image.load('wallend.png')
    murfin2 = pygame.image.load('wallend2.png')
    murfin3 = pygame.image.load('wall-end-r.gif')
    murfin4 = pygame.image.load('wall-end-l.gif')
    murcoin = pygame.image.load('wall-corner-ul.gif')
    murcoin2 = pygame.image.load('wall-corner-ur.gif')
    murcoin3 =  pygame.image.load('wall-corner-lr.gif')
    murcoin4 =  pygame.image.load('wall-corner-ll.gif')
    multicoin = pygame.image.load('wall-t-top.png')
    multicoin2 = pygame.image.load('wall-t-bottom2.png')
    multicoin3 = pygame.image.load('wall-t-bottom3.png')
    multicoin4 = pygame.image.load('wall-t-left.gif')
    carImg = pygame.image.load('start.png')
    vie = pygame.image.load('life.gif')
    porte = pygame.image.load('ghost-door.gif')
    fantome = pygame.image.load('ghost-blinky.png')
    fantome2 = pygame.image.load('ghost-inky.gif')
    fond = pygame.image.load('pellet-power.gif')









def main():
    pygame.init()
    pygame.mixer.init()
    init_display()

    clock = pygame.time.Clock()
    pygame.display.set_caption("PROZIS ALDE10 V3")
    game_over=False
    pygame.mouse.set_visible(False)


    global joueur
    joueur = Player()
    global ghost
    ghost = Ghost()
    global ghost2
    ghost2 = Ghost()


    joueur.rect.topleft = 0, 0
    allsprites = pygame.sprite.Group(joueur)

    BLACK = (0,0,0)
    global WHITE
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    global direction
    direction = 'droite'

    niveau1 = [     [2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 3],
                    [6, 32, 17, 17, 17, 17, 17, 9, 17, 17, 17, 17, 17, 24, 6],
                    [6, 17, 2, 1, 1, 3, 17, 9, 17, 2, 1, 1, 3, 17, 6],
                    [6, 17, 5, 1, 1, 8, 7, 10, 17, 5, 1, 1, 8, 17, 6],
                    [6, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 6],
                    [6, 17, 13, 17, 17, 17, 12, 4, 11, 17, 17 , 17, 13, 17, 6],
                    [6, 17, 6, 17, 13, 17, 17, 10, 17, 17, 13, 17, 6, 17, 6],
                    [6, 17, 6, 17, 19, 20, 17, 17, 17, 12, 14, 17, 6, 17, 6],
                    [6, 17, 15, 17, 15, 17, 25, 17, 17, 17, 15, 17, 15, 17, 6],
                    [6, 17, 17, 17, 17, 17, 2, 23, 3, 17, 17, 17, 17, 17, 6],
                    [6, 17, 17, 12, 3, 17, 6, 0, 6, 17, 2, 11, 17, 17, 6],
                    [6, 17, 17, 17, 15, 17, 5, 1, 8, 17, 15, 17, 17, 17, 6],
                    [6, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 26, 6],
                    [5,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
                    [18, 0, 0, 0, 0, 0, 0, 0, 0, 21, 22, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    pygame.display.flip()


    while not game_over:
            keys = pygame.key.get_pressed()
            screen.fill(BLACK)
            clock.tick(80)
            """menu()"""


            affichage(niveau1)
            pygame.display.flip()
            """pygame.time.wait(125)"""
            joueur.avancer(niveau1,direction)
            pygame.display.flip()

            ghost.tete_chercheuse(niveau1,joueur)
            ghost2.avancer(niveau1,joueur)
            affichage(niveau1)

            if keys[pygame.K_UP]:
                direction = 'haut'
                affichage(niveau1)




            if keys[pygame.K_DOWN]:
                direction = 'bas'
                affichage(niveau1)




            if keys[pygame.K_LEFT]:
                direction = 'gauche'
                affichage(niveau1)



            if keys[pygame.K_RIGHT]:

                direction = 'droite'
                affichage(niveau1)


            for event in pygame.event.get():

                if event.type == pygame.QUIT :
                    game_over = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_over = True
                elif joueur.get_vie() == 0:
                    game_over = True

                pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()


