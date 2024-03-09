#jeu louis et guillaume

import pygame
import os,sys
from pygame.locals import *
import random
from niveau0 import *


class Player(pygame.sprite.Sprite):
    def __init__(self,vie=3,point=0,x=6,y=3,vitesse =2, powered_up =50):
        pygame.sprite.Sprite.__init__(self)
        carImg.convert()
        self.image = carImg
        self.rect = carImg.get_rect()
        self.vie = vie
        self.point = point
        self.x = x
        self.y = y
        t=2 # a intégrer dans une classe pacman/Player..
        self.vitesse = vitesse  #à intégrer dans une classe pacman/player
        self.direction = "bas"
        self.powered_up = powered_up


    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y

    def is_power_up(self):
        if self.powered_up >0:
            self.powered_up = self.powered_up-1
            return True
        else:
            return False

    def comptage1(self):
            self.point +=1

    def get_point(self):
        return self.__point

    def get_vie(self):
        return self.vie

    def point_vie(self):
        self.vie-=1


#fonction qui doit faire réaparaître pacman
    def respawn(self):
        self.x= 6
        self.y =3
        self.afficher(screen)

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


    def get_pos(self):
        """for y, ligne in enumerate(niv):
            for x, cell in enumerate(ligne):
                if cell == 7:
                    return (x,y)"""
        return self.x,self.y


# fonction qui permet à pacman d'avancer

    def avancer(self,niv,dir):
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        tab[y][x]=0
        print("1) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)
        pygame.time.wait(25)
        # tentative chagnement de direction
        if dir == 'droite' and tab[y][x+1] in ( 0, 17):  #avancer vers la droite
            self.direction =dir

        elif dir == 'gauche' and tab[y][x-1] in ( 0, 17):  #avancer vers la ge
            self.direction =dir
        elif dir == 'bas' and tab[y+1][x] in ( 0, 17):  #avancer vers le b
            self.direction =dir
        elif dir == 'haut' and tab[y-1][x] in ( 0, 17):  #avancer vers le h
            self.direction =dir

        print("2) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)


        if self.direction == 'droite': #avancer vers la droite
            if tab[y][x+1] == 0 :
                x = x+1
            elif tab[y][x+1] ==17:
                self.comptage1()
                x = x+1
            elif tab[y][x+1] ==33:
                x = x+1
                self.is_power_up()
            #else:
                #erreur ?
                #print("tentative d'aller à droite : impoosible : obstacle")
        elif self.direction == 'gauche': #avancer vers g
            if tab[y][x-1] == 0 :
                x = x-1
            elif tab[y][x-1] ==17:
                self.comptage1()
                x = x-1
            elif tab[y][x-1] ==33:
                x = x-1
                self.is_power_up()
            #else:
                #erreur ?
                #print("tentative d'aller à gauche : impoosible : obstacle")
        elif  self.direction == 'bas': #avancer vers b
            if tab[y+1][x] == 0 :
                y = y+1
            elif tab[y+1][x] ==17:
                self.comptage1()
                y = y+1
            elif tab[y+1][x] ==33:
                y = y+1
                self.is_power_up()
            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        elif  self.direction == 'haut': #avancer vers h
            if tab[y-1][x] == 0 :
                y = y-1
            elif tab[y-1][x] ==17:
                self.comptage1()
                y = y-1
            elif tab[y-1][x] ==33:
                y = y-1
                self.is_power_up()
            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        self.x , self.y = x, y

        print("3) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)

        #tab[x][y] = 7 # on place la pacman aux nouvelles coordonnées

    def afficher(self, screen):
        pacman = pygame.Surface((16,16))
        pygame.draw.circle(pacman,(255,255,0),(8,8),8)
        pygame.draw.polygon(pacman,(0,0,0),((8,8),(16,8-t),(16,8+t)))
        angle= { 'droite' : 0, 'haut' : 90, 'gauche': 180, 'bas':270}
        pacman = pygame.transform.rotate(pacman, angle[self.direction])
        screen.blit(pacman, (self.x*16,self.y*16))


    def __str__(self):
        return str(self.point), str(self.vie), str(self.x), str(self.y)



class Ghost:
    def __init__(self,x=None,y=None,type=None,direction=None,cible=None):
        pygame.sprite.Sprite.__init__(self)
        if type == 'random' :
            Img = pygame.image.load('ghost-blinky.png')
            Img.convert()
            self.image = pygame.image.load('ghost-blinky.png')
            self.rect = Img.get_rect()
        if type == 'chercher':
            Img = pygame.image.load('ghost-inky.gif')  # il me renvoi cette erreur : AttributeError: 'Ghost' object has no attribute 'image'
            Img.convert()
            self.image = pygame.image.load('ghost-inky.gif')
            self.rect = Img.get_rect()

        self.cible = cible
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


    def afficher(self, screen):
        screen.blit(self.image, (self.x*16,self.y*16))






#fonction de recherche mais il ne me suive pas totalement

    def deplacement(self,joueur):
        if joueur.is_power_up():
            if joueur.x > self.x:
                self.direction = 'gauche'
            if joueur.x < self.x:
                self.direction = 'droite'
            if joueur.y > self.y:
                self.direction = 'haut'
            if joueur.y < self.y:
                self.direction = 'bas'
        else:
            if joueur.x > self.x:
                self.direction = 'droite'
            if joueur.x < self.x:
                self.direction = 'gauche'
            if joueur.y > self.y:
                self.direction = 'bas'
            if joueur.y < self.y:
                self.direction = 'haut'





#je n'arrive pas à faire disparaître pacman
#fantôme à tête chercheuse
    def tete_chercheuse(self,niv,joueur):
        self.deplacement(joueur)
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        #tab[y][x]=0
        print("1) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)
        pygame.time.wait(100)
        # tentative chagnement de direction
        if dir == 'droite' and tab[y][x+1] in ( 0, 17):  #avancer vers la droite
            self.direction =dir

        elif dir == 'gauche' and tab[y][x-1] in ( 0, 17):  #avancer vers la ge
            self.direction =dir
        elif dir == 'bas' and tab[y+1][x] in ( 0, 17):  #avancer vers le b
            self.direction =dir
        elif dir == 'haut' and tab[y-1][x] in ( 0, 17):  #avancer vers le h
            self.direction =dir

        print("2) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)


        if self.direction == 'droite': #avancer vers la droite
            if tab[y][x+1] == 0 :
                x = x+1
                tab[y][x]=0
            elif tab[y][x+1] ==17:
                x = x+1
            elif tab[y][x+1] == joueur.get_pos():
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0
                x=x+1

            #else:
                #erreur ?
                #print("tentative d'aller à droite : impoosible : obstacle")
        elif self.direction == 'gauche': #avancer vers g
            if tab[y][x-1] == 0 :
                x = x-1
                tab[y][x]=0
            elif tab[y][x-1] ==17:
                x = x-1
            elif tab[y][x-1] == joueur.get_pos():
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0
                x=x-1

            #else:
                #erreur ?
                #print("tentative d'aller à gauche : impoosible : obstacle")
        elif  self.direction == 'bas': #avancer vers b
            if tab[y+1][x] == 0 :
                y = y+1
                tab[y][x]=0
            elif tab[y+1][x] ==17:
                y = y+1
            elif tab[y+1][x] == joueur.get_pos():
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0
                y =y+1


            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        elif  self.direction == 'haut': #avancer vers h
            if tab[y-1][x] == 0 :
                y = y-1
                tab[y][x]=0
            elif tab[y-1][x] ==17:
                y = y-1
            elif tab[y-1][x] == joueur.get_pos():
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0
                y =y-1

            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        self.x , self.y = x, y

        print("3) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)



#fantôme radom


    def avancer(self,niv,joueur):
        if joueur.is_power_up():
            if joueur.x > self.x:
                self.direction = 'gauche'
            if joueur.x < self.x:
                self.direction = 'droite'
            if joueur.y > self.y:
                self.direction = 'haut'
            if joueur.y < self.y:
                self.direction = 'bas'
        else:
            self.choisir_direction()

        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        #tab[y][x]=0
        print("1) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)
        pygame.time.wait(100)
        # tentative chagnement de direction
        if dir == 'droite' and tab[y][x+1] in ( 0, 17,7):  #avancer vers la droite
            self.direction =dir

        elif dir == 'gauche' and tab[y][x-1] in ( 0, 17,7):  #avancer vers la ge
            self.direction =dir
        elif dir == 'bas' and tab[y+1][x] in ( 0, 17,7):  #avancer vers le b
            self.direction =dir
        elif dir == 'haut' and tab[y-1][x] in ( 0, 17,7):  #avancer vers le h
            self.direction =dir

        print("2) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)


        if self.direction == 'droite': #avancer vers la droite
            if tab[y][x+1] == 0 :
                x = x+1
                tab[y][x]=0
            elif tab[y][x+1] ==17:
                x = x+1
            elif tab[y][x+1] == joueur.get_pos():
                x=x+1
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0


            #else:
                #erreur ?
                #print("tentative d'aller à droite : impoosible : obstacle")
        elif self.direction == 'gauche': #avancer vers g
            if tab[y][x-1] == 0 :
                x = x-1
                tab[y][x]=0
            elif tab[y][x-1] ==17:
                x = x-1
            elif tab[y][x-1] == joueur.get_pos():
                x=x-1
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0


            #else:
                #erreur ?
                #print("tentative d'aller à gauche : impoosible : obstacle")
        elif  self.direction == 'bas': #avancer vers b
            if tab[y+1][x] == 0 :
                y = y+1
                tab[y][x]=0
            elif tab[y+1][x] ==17:
                y = y+1
            elif tab[y+1][x] == joueur.get_pos():
                y =y+1
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0



            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        elif  self.direction == 'haut': #avancer vers h
            if tab[y-1][x] == 0 :
                y = y-1
                tab[y][x]=0
            elif tab[y-1][x] ==17:
                y = y-1
            elif tab[y-1][x] == joueur.get_pos():
                y =y-1
                joueur.point_vie()
                joueur.respawn()
                tab[y][x]=0


            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        self.x , self.y = x, y

        print("3) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)


    def __str__(self):
        return  str(self.x), str(self.y)


class Game:
    def __init__(self):
        self.levelNum = 0
        self.niv = None
        self.liste_gomme=[]
        self.list_pacgomme=[]



    def affichage(self):
        global t
        self.get_niv()
        global joueur
        x = 0
        y = 0
        for ligne in self.get_niv():
            for block in ligne:
                if block == 1:
                    screen.blit(mur3,(x,y))

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

                if block == 7:  ## Pacman
##                    screen.blit(carImg, (x,y))
                    pass

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
                    pass
                    #screen.blit(fantome, (x,y))

                if block == 25:
                    pass
                    #screen.blit(fantome2, (x,y))

                if block == 30:
                    police = pygame.font.Font(None, 50)
                    texte1 = police.render("PAC-MAN ",True,(255,255,0))
                    screen.blit(texte1, (x,y)) # x-40 pour que ce soit au milieu

                if block == 31:
                    police = pygame.font.Font(None, 30)
                    texte3 = police.render("Jouer" ,True,WHITE)
                    screen.blit(texte3, (x,y))

                if block == 32:
                    police = pygame.font.Font(None, 30)
                    texte4 = police.render("Scores" ,True,WHITE)
                    screen.blit(texte4, (x,y))


                if block == 33:
                    screen.blit(power, (x,y))











                x += 16
            x=0
            y += 16


    def get_niv(self):
        if self.levelNum =1:
            self.niv = niv1


        return self.niv

    def set_labyrinthe(self, niveau):
        self.niv = niveau

# fonction liste gomme pas pu essayer car problème édupython
    def creer_listes_gomme(self):
        tab = get_niv()
        for ligne in tab:
            for block in ligne:
                if block == 33:
                    tab[y][x] = Pacgomme(y,x)
                    self.list_pacgomme.append(tab[y][x])
                if block == 17 :
                    tab[y][x] = Pastille(y,x)
                    self.liste_gomme.append(tab[y][x])


#tentative de passage au niveau suivant
    def fin_niveau(self):
        if self.liste_gomme == 0 and  self.list_pacgomme == 0:
            self.levelNum+=1
            self.get_niv()


#class pastille et pacgomme

class  Pastille():
   def __init__(self,x=None,y=None):
        pygame.sprite.Sprite.__init__(self)
        Img =  pygame.image.load('pellet.png')
        Img.convert()
        self.image = Img
        self.rect = Img.get_rect()
        self.x = x
        self.y = y

   def afficher(self, screen):
        screen.blit(self.image, (self.x*16,self.y*16))


class  Pacgomme():
   def __init__(self,x=None,y=None):
        pygame.sprite.Sprite.__init__(self)
        Img =  pygame.image.load('pellet.png')
        Img.convert()
        self.image = Img
        self.rect = Img.get_rect()
        self.x = x
        self.y = y

   def afficher(self, screen):
        screen.blit(self.image, (self.x*16,self.y*16))





#class

class Curseur():
    def __init__(self,x=6,y=5):
        self.x = x
        self.y = y


    def deplacement(self,niv,direction):
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        tab[y][x]=0
        print("1) ligne", y, "colonne", x, "direction", dir, "self.direction",self.direction)
        pygame.time.wait(25)
        # tentative chagnement de direction

        if  direction == 'bas': #avancer vers b
            if tab[y+1][x] == 0 :
                y = y+2

            #else:
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        elif  direction == 'haut': #avancer vers h
            if tab[y-1][x] == 0 :
                y = y-2
                #erreur ?
                #print("tentative d'aller en bas : impoosible : obstacle")
        self.x , self.y = x, y


    def afficher(self, screen):
        curseur = pygame.Surface((16,16))
        pygame.draw.polygon(curseur,(0,0,0),((8,8),(16),(8)))
        screen.blit(curseur, (self.x*16,self.y*16))










def init_display():
    global screen, porte, tile, mur, mur2, mur3, mur4, manger,power, murfin,murfin2, fantome,fond, fantome2, murfin3,murfin4, murcoin,murcoin2, multicoin, multicoin2, multicoin3, multicoin4, carImg, murcoin3, murcoin4, vie
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
    power = pygame.image.load('pellet-power.gif')









def main():
    global t

    pygame.init()
    pygame.mixer.init()
    init_display()

    clock = pygame.time.Clock()
    pygame.display.set_caption("PROZIS ALDE10 V3")
    game_over=False
    pygame.mouse.set_visible(False)


    global joueur
    joueur = Curseur ()
    if niv.get_niv() != niv0:
        joueur = Player()
    global ghost
    ghost = Ghost(13,1,"chercher")
    global ghost2
    ghost2 = Ghost(1,12,'random')
    global niv
    niv = Game()
    niv.set_labyrinthe(niv1)
    niv.creer_listes_gomme()


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


    pygame.display.flip()

    t=2 # a intégrer dans une classe pacman/Player..
    vitesse =2 #à intégrer dans une classe pacman/player

    while not game_over:
            keys = pygame.key.get_pressed()
            screen.fill(BLACK)
            clock.tick(80)

            t = t+vitesse
            if t == 8 :
                vitesse = -1
            if t == 0:
                vitesse = 1

            niv.affichage()
            joueur.avancer(niv,direction)


            if keys[pygame.K_UP]:
                direction = 'haut'

            if keys[pygame.K_DOWN]:
                direction = 'bas'

            if keys[pygame.K_LEFT]:
                direction = 'gauche'

            if keys[pygame.K_RIGHT]:
                direction = 'droite'

            if niv.get_niv() != niv0:
                ghost.tete_chercheuse(niv,joueur)
                ghost2.avancer(niv,joueur)
            joueur.avancer(niv,direction)
            niv.affichage()
            joueur.afficher(screen)
            if niv.get_niv() != niv0:
                ghost.afficher(screen)
                ghost2.afficher(screen)

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


