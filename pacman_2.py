#jeu louis et guillaume

import pygame
import os,sys
from pygame.locals import *
import random
from niveau0 import *

#class player ainsi que tout ses attributs

class Player(pygame.sprite.Sprite):
    def __init__(self,vie=3,point=0,x=3,y=8,vitesse =2, powered_up =5, etat = False): #constructeur
        pygame.sprite.Sprite.__init__(self)
        carImg.convert()
        self.image = carImg     #image de pacman
        self.rect = carImg.get_rect()   #rectancle placé sur pacman pour faire ça bouche
        self.vie = vie      #le nombre de vie de pacman
        self.point = point     #score du joueur
        self.x = x
        self.y = y
        t=2 # a intégrer dans une classe pacman/Player..
        self.vitesse = vitesse  #à intégrer dans une classe pacman/player
        self.direction = "bas"     #direction dans laquelle pacman part au début du jeu
        self.powered_up = powered_up  #permet à pacman de manger les fantômes
        self.etat  =  etat   #état du pacman pour savoir si il est apte ou pas à manger les fantômes

    #foncions get qui vont renvoyer les coordonnées du joueur
    def get_x(self):
        return self.__x     #retourne la position de x


    def get_y(self):
        return self.__y    #retourne la position de y

    #fonciton power_up qui pemet à pacman de manger les fantômes
    def is_power_up(self):
        if self.etat == True:
             self.powered_up = self.powered_up-1
        if self.powered_up == 0:
            self.etat = False

    # fonction qui va gérer le score du joueur
    def comptage1(self):
        self.point +=1    #il gagne un point à chaque pac-gomme mangé
    def manger_fantome(self):
        self.point +=50      #si le pacman mange un fantôme il gagne 50 points

    def get_point(self):
        return self.__point

    def get_vie(self):
        return self.vie
    # fonction qui gère les points de vie du joueur
    def point_vie(self):
        self.vie-=1    #si il se fait manger il perd une vie


#fonction qui doit faire réaparaître pacman
    def respawn(self):
        self.x= 3    #à chaque fois que le pacman respawn il réapparaît aux coordonnées (3,8)
        self.y =8
        self.afficher(screen)  #affiche le pacman à l'écran quand il respawn

#fonction qui retrouve la position de pacman
    def get_pos(self):
        return (self.x,self.y)


# fonction qui permet à pacman d'avancer

    def avancer(self,niv,dir,ghost1,ghost2):
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        tab[y][x]=0
        pygame.time.wait(100)
        # tentative chagnement de direction
        if dir == 'droite' and tab[y][x+1] in ( 0, 17):  #avancer vers la droite
            self.direction =dir

        elif dir == 'gauche' and tab[y][x-1] in ( 0, 17):  #avancer vers la gauche
            self.direction =dir
        elif dir == 'bas' and tab[y+1][x] in ( 0, 17):  #avancer vers le bas
            self.direction =dir
        elif dir == 'haut' and tab[y-1][x] in ( 0, 17):  #avancer vers le haut
            self.direction =dir

        if self.direction == 'droite': #avancer vers la droite
            if (x+1,y) ==  ghost1.get_pos() :
                if self.etat == True :
                    ghost1.respawn()
                    eatfantôme.play()
                    x=x+1
            if (x+1,y) == ghost2.get_pos()  :
                if self.etat == True:
                    ghost2.respawn()
                    eatfantôme.play()
                    x=x+1
            elif tab[y][x+1] == 0 :
                x = x+1
            elif tab[y][x+1] ==17:
                self.comptage1()
                son.play()
                x = x+1
            elif tab[y][x+1] ==33:
                x = x+1
                self.etat = True
                if self.powered_up == 0:
                    self.powered_up = 25

        elif self.direction == 'gauche': #avancer vers g
            if (x-1,y) == ghost1.get_pos()  :
                if self.etat == True :
                    ghost1.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    x=x-1
            if (x-1,y) == ghost2.get_pos()  :
                if self.etat == True:
                    ghost2.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    x=x-1

            if tab[y][x-1] == 0 :
                x = x-1
            elif tab[y][x-1] ==17:
                self.comptage1()
                son.play()
                x = x-1
            elif tab[y][x-1] ==33:
                x = x-1
                self.etat = True
                if self.powered_up == 0:
                    self.powered_up = 25

        elif  self.direction == 'bas': #avancer vers b
            if (x,y+1) == ghost1.get_pos()  :
                if self.etat == True :
                    ghost1.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    y=y+1
            if (x,y+1) == ghost2.get_pos()  :
                if self.etat == True:
                    ghost2.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    y=y+1
            if tab[y+1][x] == 0 :
                y = y+1
            elif tab[y+1][x] ==17:
                self.comptage1()
                son.play()
                y = y+1
            elif tab[y+1][x] ==33:
                y = y+1
                self.etat = True
                if self.powered_up == 0:
                    self.powered_up = 25

        elif  self.direction == 'haut': #avancer vers h
            if  (x,y-1) == ghost1.get_pos() :
                if self.etat == True :
                    ghost1.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    y=y-1
            if (x,y-1) == ghost2.get_pos()  :
                if self.etat == True:
                    ghost2.respawn()
                    eatfantôme.play()
                    self.manger_fantome()
                    y=y-1
            if tab[y-1][x] == 0 :
                y = y-1
            elif tab[y-1][x] ==17:
                self.comptage1()
                son.play()
                y = y-1
            elif tab[y-1][x] ==33:
                y = y-1
                self.etat = True
                if self.powered_up == 0:
                    self.powered_up = 25

        self.x , self.y = x, y


        #tab[x][y] = 7 # on place la pacman aux nouvelles coordonnées

    #fonction d'affiche de pacman
    def afficher(self, screen):
        pacman = pygame.Surface((16,16))
        pygame.draw.circle(pacman,(255,255,0),(8,8),8)
        pygame.draw.polygon(pacman,(0,0,0),((8,8),(16,8-t),(16,8+t)))
        angle= { 'droite' : 0, 'haut' : 90, 'gauche': 180, 'bas':270}
        pacman = pygame.transform.rotate(pacman, angle[self.direction])
        screen.blit(pacman, (self.x*16,self.y*16))


    def __str__(self):
        return str(self.point), str(self.vie), str(self.x), str(self.y)
# class des fantômes


class Ghost:
    def __init__(self,x=None,y=None,type=None,direction=None,cible=None):
        pygame.sprite.Sprite.__init__(self)
        if type == 'random' :
            Img = pygame.image.load('ghost-blinky.png')
            Img.convert()
            self.image = pygame.image.load('ghost-blinky.png')
            self.rect = Img.get_rect()
        if type == 'chercher':
            Img = pygame.image.load('ghost-inky.gif')
            Img.convert()
            self.image = pygame.image.load('ghost-inky.gif')
            self.rect = Img.get_rect()

        self.cible = cible
        self.direction = direction
        self.x = x
        self.y = y

    #fonction qui choisi au hasard une direction
    def choisir_direction(self):
        self.direction  = random.choice(['droite','gauche','bas','haut'])

    #fonction qui permet d'afficher le  fantômes

    def afficher(self, screen):
        screen.blit(self.image, (self.x*16,self.y*16))

#fonction qui retrouve la position des fantômes
    def get_pos(self):
        return self.x,self.y

#fonction qui doit faire réaparaître
    def respawn(self):
        self.x= 10   #à chaque fois que les fantômes respawn ils réapparaissent aux coordonnées (7,10)
        self.y =13
        self.afficher(screen)  #affiche les fantômes à l'écran quand ils respawn






#fonction de recherche du fantôme tête chercheuse

    def chercher(self,joueur):
        if joueur.etat == True:
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






#fantôme à tête chercheuse
    def tete_chercheuse(self,niv,joueur):
        self.chercher(joueur)
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

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

        if self.direction == 'droite': #avancer vers la droite
            if (x+1,y) == joueur.get_pos():
                x = x+1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
            elif tab[y][x+1] == 0 :
                x = x+1
                tab[y][x]=0
            elif tab[y][x+1] ==17:
                x = x+1
            elif tab[y][x+1] ==33:
                x = x+1
            elif tab[y][x+1] ==23:
                x = x+1

        elif self.direction == 'gauche': #avancer vers g
            if (x-1,y) == joueur.get_pos():
                x = x-1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
            elif tab[y][x-1] == 0 :
                x = x-1
                tab[y][x]=0
            elif tab[y][x-1] ==17:
                x = x-1
            elif tab[y][x-1] ==33:
                x = x-1
            elif tab[y][x-1] ==23:
                x = x-1

        elif  self.direction == 'bas': #avancer vers b
            if (x,y+1) == joueur.get_pos():
                y = y+1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()

            elif tab[y+1][x] == 0 :
                y = y+1
                tab[y][x]=0
            elif tab[y+1][x] ==17:
                y = y+1
            elif tab[y+1][x] ==33:
                y = y+1
            elif tab[y+1][x] ==23:
                y = y+1

        elif  self.direction == 'haut': #avancer vers h
            if (x,y-1) == joueur.get_pos():
                y = y-1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
            elif tab[y-1][x] == 0 :
                y = y-1
                tab[y][x]=0
            elif tab[y-1][x] ==17:
                y = y-1
            elif tab[y-1][x] ==33:
                y = y-1
            elif tab[y-1][x] ==23:
                y = y-1

        self.x , self.y = x, y


#fantôme random


    def avancer(self,niv,joueur):
        if joueur.etat == True:
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

        if self.direction == 'droite': #avancer vers la droite
            if (x+1,y) == joueur.get_pos():
                x =x+1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
            elif tab[y][x+1] == 0 :
                x = x+1
                tab[y][x]=0
            elif tab[y][x+1] ==17:
                x = x+1
            elif tab[y][x+1] ==33:
                x = x+1
            elif tab[y][x+1] ==23:
                x = x+1

        elif self.direction == 'gauche': #avancer vers g
            if (x-1,y) == joueur.get_pos():
                x =x-1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
                tab[y][x]=0
            elif tab[y][x-1] == 0 :
                x = x-1
                tab[y][x]=0
            elif tab[y][x-1] ==17:
                x = x-1
            elif tab[y][x-1] ==33:
                x = x-1
            elif tab[y][x-1] ==23:
                x = x-1

        elif  self.direction == 'bas': #avancer vers b
            if (y+1,x) == joueur.get_pos():
                y =y+1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
                tab[y][x]=0
            elif tab[y+1][x] == 0 :
                y = y+1
            elif tab[y+1][x] ==17:
                y = y+1
            elif tab[y+1][x] ==33:
                y = y+1
            elif tab[y+1][x] ==23:
                y = y+1

        elif  self.direction == 'haut': #avancer vers h
            if (y-1,x) == joueur.get_pos():
                y =y-1
                joueur.point_vie()
                mort.play()
                pygame.time.wait(100)
                joueur.respawn()
                #tab[y][x]=0
            elif tab[y-1][x] == 0 :
                y = y-1
                tab[y][x]=0
            elif tab[y-1][x] ==17:
                y = y-1
            elif tab[y-1][x] ==33:
                y = y-1
            elif tab[y-1][x] ==23:
                y = y-1

        self.x , self.y = x, y

    def __str__(self):
        return  str(self.x), str(self.y)

#class game qui va gérer l'affichage du labyrinthe ainsi que la fin d'un niveau et que le menu
class Game:
    def __init__(self):
        self.levelNum = 0
        self.niv = None
        self.liste_gomme=[]
        self.list_pacgomme=[]


#fonction affichage qui à chaque valeur va afficher l'élément voulu

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

                if block == 7:
                    screen.blit(carImg, (x,y))

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
                    screen.blit(multicoin3, (x,y))

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
                    screen.blit(texte1, (x,y))

                if block == 31:
                    police = pygame.font.Font(None, 30)
                    texte3 = police.render("Jouer" ,True,WHITE)
                    screen.blit(texte3, (x,y))

                if block == 32:
                    police = pygame.font.Font(None, 30)
                    texte4 = police.render("Quitter" ,True,WHITE)
                    screen.blit(texte4, (x,y))


                if block == 33:
                    screen.blit(power, (x,y))

                if block == 35:
                    police = pygame.font.Font(None, 30)
                    texte5 = police.render("Menu principal ?" ,True,WHITE)
                    screen.blit(texte5, (x,y))

                if block == 36:
                    police = pygame.font.Font(None, 30)
                    texte5 = police.render("continuer ?" ,True,WHITE)
                    screen.blit(texte5, (x,y))

                if block == 666:
                    police = pygame.font.Font(None, 15)
                    texte7 = police.render("Made by Louis et Guillaume" ,True,WHITE)
                    screen.blit(texte7, (x,y))

##                if block == 37:
##                    police = pygame.font.Font(None, 25)
##                    texte6 = police.render("" + str( joueur.powered_up),True,WHITE)
##                    screen.blit(texte6, (x,y))

                x += 16
            x=0
            y += 16


    def get_niv(self):
        if self.levelNum ==0 :
            self.niv = niv0

        if self.levelNum == 1:
            self.niv = niv1

        if self.levelNum == -1:
            self.niv = menu

        return self.niv


    #  fonction qui va changer le niveau

    def set_labyrinthe(self,level):
        self.levelNum = level
        self.get_niv()

    def next_level(self):
        self.levelNum+=1


    def creer_listes_gomme(self):
        global compteur
        compteur = 0
        tab = niv.get_niv()
        for x,ligne in enumerate(tab):
            for y,block in enumerate(ligne):
                if block == 33:
                    compteur+=1
                if block == 17 :
                    compteur+=1



    def fin_niveau(self):
        if compteur == 0:
            return True

    def verifier(self,joueur):
        if self.get_niv() == niv0:
            if joueur.position == 1:
                self.levelNum+=1
                self.get_niv()
            if joueur.position == 2 :
                pygame.display.flip()
                pygame.quit()
        if self.get_niv() == menu :
            if joueur.position == 1:
                self.levelNum = 0
                self.get_niv()
            if joueur.position == 2:
                self.levelNum = i
                self.get_niv()




#class pastille et pacgomme

class  Pastille():
   def __init__(self,y=None,x=None):
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
   def __init__(self,y=None,x=None):
        pygame.sprite.Sprite.__init__(self)
        Img =  pygame.image.load('pellet.png')
        Img.convert()
        self.image = Img
        self.rect = Img.get_rect()
        self.x = x
        self.y = y

   def afficher(self, screen):
        screen.blit(self.image, (self.x*16,self.y*16))





#class curseur qui va être que dans le menu qui va permettre de lancer le jeux

class Curseur():
    def __init__(self,x=5,y=6,direction=None,position=1):
        self.x = x
        self.y = y
        self.direction = direction
        self.position= position

    def get_pos(self):
        return self.x,self.y


    def deplacement(self,niv,direction):
        x = 0
        y = 0

        tab = niv.get_niv()
        (x,y) = self.x, self.y

        tab[y][x]=0
        pygame.time.wait(25)
        # tentative chagnement de direction

        if  direction == 'bas': #avancer vers b
            if tab[y+1][x] == 0 :
                y = y+1
                self.position = 2

        elif  direction == 'haut': #avancer vers h
            if tab[y-1][x] == 0 :
                y = y-1
                self.position = 1

        self.x , self.y = x, y


    def afficher(self, screen):
        curseur = pygame.Surface((16,16))
        pygame.draw.polygon(curseur,WHITE,((8,8),(16,16),(16,0)))
        curseur = pygame.transform.rotate(curseur, 180)
        screen.blit(curseur, (self.x*16,self.y*16))










def init_display():
    global screen, porte, tile, mur, mur2, mur3, mur4, manger,power, murfin,murfin2, fantome,fond, fantome2, murfin3,murfin4, murcoin,murcoin2, multicoin, multicoin2, multicoin3, multicoin4, carImg, murcoin3, murcoin4, vie
    screen = pygame.display.set_mode((320, 320))
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
    intro = pygame.mixer.Sound("pacman_beginning.wav")
    global son
    global eatfantôme
    global mort
    son = pygame.mixer.Sound("pacman_chomp.wav")
    eatfantôme = pygame.mixer.Sound("pacman_eatghost.wav")
    mort = pygame.mixer.Sound("pacman_death.wav")



    global niv
    global joueur
    global curseur
    global i
    global compteurson
    niv = Game()
    curseur = Curseur()
    joueur=Player()
    i=1
    compteurson =1

    global ghost
    ghost = Ghost(13,1,"chercher")
    global ghost2
    ghost2 = Ghost(1,12,'random')
    niv.set_labyrinthe(0)
    niv.creer_listes_gomme()


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
                vitesse = -1   #
            if t == 0:
                vitesse = 1

            if keys[pygame.K_UP]:
                direction = 'haut'

            if keys[pygame.K_DOWN]:
                direction = 'bas'

            if keys[pygame.K_LEFT]:
                direction = 'gauche'

            if keys[pygame.K_RIGHT]:
                direction = 'droite'

            if keys[pygame.K_q]:
                niv.verifier(curseur)


            if niv.get_niv() != niv0 and niv.get_niv() != menu :
                joueur.avancer(niv,direction,ghost,ghost2),
                joueur.is_power_up(),
                ghost.tete_chercheuse(niv,joueur),
                ghost2.avancer(niv,joueur),




            if niv.get_niv() == niv0 or  niv.get_niv() == menu:
                if compteurson == 1:
                    intro.play()
                    compteurson-=1
                curseur.deplacement(niv,direction)
                curseur.afficher(screen)

            niv.affichage()



            if niv.get_niv() != niv0:
                joueur.afficher(screen),
                ghost.afficher(screen),
                ghost2.afficher(screen),
                niv.creer_listes_gomme()

            for event in pygame.event.get():

                if event.type == pygame.QUIT :
                    game_over = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    niv.set_labyrinthe(-1)

                if niv.get_niv() != niv0 :
                    if joueur.get_vie() == 0 :
                        game_over = niv.set_labyrinthe(0)
                        compteurson = 1
                if niv.fin_niveau():
                    i=+1
                    niv.set_labyrinthe(i)



            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()



