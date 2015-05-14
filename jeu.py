import tkinter
from tkinter import *
import random
import time
import classes
from classes import *
from constantes import *
from pygame.locals import *

def lancer_jeu():

        pygame.init()
        fenetre = pygame.display.set_mode((cote_fenetre_x, cote_fenetre_y))

        pygame.display.set_caption(titre_fenetre)

        pygame.mixer.init()
        pygame.mixer.music.load("song/dbz.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(.15)
        frame_rate = 20
        start_time = 90


        done = False

        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop


                continuer = 1
                while continuer:
                        #Chargement et affichage de l'ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cran d'accueil
                        accueil = pygame.image.load(image_accueil).convert()
                        fenetre.blit(accueil, (0,0))

                        #Rafraichissement
                        pygame.display.flip()

                        #On remet ces variables ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  1 ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  chaque tour de boucle
                        continuer_jeu = 1
                        continuer_accueil = 1


                        while continuer_accueil:

                                #Limitation de vitesse de la boucle
                                pygame.time.Clock().tick(20)

                                for event in pygame.event.get():

                                        #Si l'utilisateur quitte, on met les variables
                                        #de boucle ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  0 pour n'en parcourir aucune et fermer
                                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                                                continuer_accueil = 0
                                                continuer_jeu = 0
                                                continuer = 0
                                                #Variable de choix du niveau
                                                choix = 0

                                        elif event.type == KEYDOWN:
                                                #Lancement du niveau 1
                                                if event.key == K_F1:

                                                        continuer_accueil = 0	#On quitte l'accueil
                                                        choix = 'level/n1'   	#On dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©finit le niveau ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  charge

                                                elif event.key == K_F2:
                                                        continuer_accueil = 0
                                                        choix = 'level/n2'
                                                elif event.key == K_F3:
                                                        continuer_accueil = 0
                                                        choix = 'level/n3'
                        if choix != 0:

                                #Chargement du fond
                                fond = pygame.image.load(image_fond).convert()

                                #GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©ration d'un niveau ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  partir d'un fichier
                                niveau = Niveau(choix)
                                niveau.generer()
                                niveau.afficher(fenetre)
                                goku = Perso("picture/goku1.png","picture/goku.png","picture/goku3.png","picture/goku3.png", niveau)




                        frame_count = 0
                        while continuer_jeu:
                                


                                #Limitation de vitesse de la boucle

                                for event in pygame.event.get():


                                        #Si l'utilisateur quitte, on met la variable qui continue le jeu
                                        #ET la variable gÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rale ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  0 pour fermer la fenÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªtre
                                        if event.type == QUIT:
                                                continuer_jeu = 0
                                                continuer = 0

                                        elif event.type == KEYDOWN:
                                                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                                                if event.key == K_ESCAPE:
                                                        continuer_jeu = 0

                                                #Touches de dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©placement de Donkey Kong
                                                elif event.key == K_RIGHT:
                                                        goku.deplacer('droite')
                                                elif event.key == K_LEFT:
                                                        goku.deplacer('gauche')
                                                elif event.key == K_UP:
                                                        goku.deplacer('haut')
                                                elif event.key == K_DOWN:
                                                        goku.deplacer('bas')

                                fenetre.blit(fond, (0,0))
                                el_chrono = pygame.font.SysFont("monospace", 15)
                                timer = el_chrono.render('', 1,(255,255,0))
                                pygame.time.Clock().tick(30)
                                fg = 250, 240, 230
                                bg = 5, 5, 5
                                font = pygame.font.Font(None, 80)
                                total_seconds = frame_count // frame_rate
                                minutes = total_seconds // 60
                                seconds = total_seconds % 60
                                output_string = "Temps: {0:02}:{1:02}".format(minutes, seconds)
                                timer = el_chrono.render(output_string, 1,(255,255,0))
                                fenetre.blit(timer, (1, 500))
                                frame_count += 1

                                

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

                                

                        #fichier = open("test.txt", "w")        #Créer le fichier s'il n'existe pas
                        #fichier.write(output_string)        #Écrit la valeur de la variable a dans le fichier
                       # fichier.close()




