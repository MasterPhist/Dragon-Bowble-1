import tkinter
from tkinter import *
import random
from classes import *
from constantes import *
from pygame.locals import *


def lancer_jeu():



        pygame.init()

        fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

        pygame.display.set_caption(titre_fenetre)

        pygame.mixer.init()
        pygame.mixer.music.load("song/dbz.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(.25)





        continuer = 1
        while continuer:
                #Chargement et affichage de l'ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©cran d'accueil
                accueil = pygame.image.load(image_accueil).convert()
                fenetre.blit(accueil, (0,0))

                #Rafraichissement
                pygame.display.flip()

                #On remet ces variables ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  1 ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  chaque tour de boucle
                continuer_jeu = 1
                continuer_accueil = 1


                while continuer_accueil:

                        #Limitation de vitesse de la boucle
                        pygame.time.Clock().tick(30)

                        for event in pygame.event.get():

                                #Si l'utilisateur quitte, on met les variables
                                #de boucle ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  0 pour n'en parcourir aucune et fermer
                                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                                        continuer_accueil = 0
                                        continuer_jeu = 0
                                        continuer = 0
                                        #Variable de choix du niveau
                                        choix = 0

                                elif event.type == KEYDOWN:
                                        #Lancement du niveau 1
                                        if event.key == K_F1:

                                                continuer_accueil = 0	#On quitte l'accueil
                                                choix = 'level/n1'   	#On dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©finit le niveau ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  charge

                                        elif event.key == K_F2:
                                                continuer_accueil = 0
                                                choix = 'level/n2'
                                        elif event.key == K_F3:
                                                continuer_accueil = 0
                                                choix = 'level/n3'
                if choix != 0:

                        #Chargement du fond
                        fond = pygame.image.load(image_fond).convert()

                        #GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ration d'un niveau ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  partir d'un fichier
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        goku = Perso("picture/goku1.png","picture/goku.png","picture/goku3.png","picture/goku3.png", niveau)





                while continuer_jeu:

                        #Limitation de vitesse de la boucle
                        pygame.time.Clock().tick(30)

                        for event in pygame.event.get():


                                #Si l'utilisateur quitte, on met la variable qui continue le jeu
                                #ET la variable gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©rale ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  0 pour fermer la fenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âªtre
                                if event.type == QUIT:
                                        continuer_jeu = 0
                                        continuer = 0

                                elif event.type == KEYDOWN:
                                        #Si l'utilisateur presse Echap ici, on revient seulement au menu
                                        if event.key == K_ESCAPE:
        	                                continuer_jeu = 0

                                        #Touches de dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©placement de Donkey Kong
                                        elif event.key == K_RIGHT:
                                        	goku.deplacer('droite')
                                        elif event.key == K_LEFT:
                                        	goku.deplacer('gauche')
                                        elif event.key == K_UP:
                                        	goku.deplacer('haut')
                                        elif event.key == K_DOWN:
                                        	goku.deplacer('bas')




                        fenetre.blit(fond, (0,0))

                        niveau.afficher(fenetre)

                        fenetre.blit(goku.direction, (goku.x, goku.y))

                        pygame.display.flip()

                        if niveau.structure[goku.case_y][goku.case_x] == '1':
                        	continuer_jeu = 0
                        if niveau.structure[goku.case_y][goku.case_x] == '2':
                        	continuer_jeu = 0
                        if niveau.structure[goku.case_y][goku.case_x] == '3':
                        	continuer_jeu = 0
                        if niveau.structure[goku.case_y][goku.case_x] == 'Z':
                        	continuer_jeu = 0
                        	



