# Créé par lenouvel, le 06/05/2021 en Python 3.7

    '''    # obtenir les coordonnées du pacman
        for x,ligne in enumerate(tab):
                for y,block in enumerate (ligne):
                    try:
                        if block == 7 :
                            print("pacman en", x, y)
                            self.x = x
                            self.y = y
                    except IndexError:
                        pass'''



pacman = pygame.Surface((16,16))
                    pygame.draw.circle(pacman,(255,255,0),(8,8),8)
                    pygame.draw.polygon(pacman,(0,0,0),((8,8),(16,8-t),(16,8+t)))
                    angle= { 'droite' : 0, 'haut' : 90, 'gauche': 180, 'bas':270}
                    pacman = pygame.transform.rotate(pacman, angle[joueur.direction])
                    screen.blit(pacman, (x,y))
