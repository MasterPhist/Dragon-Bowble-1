import tkinter
from tkinter import *
import random
import time
import classes
from classes import *
from constantes import *
from pygame.locals import *

def lancer_jeu():

        pygame.init()#on initialise pygame
        fenetre = pygame.display.set_mode((cote_fenetre_x, cote_fenetre_y))#on definit la taille de la fenetre

        pygame.display.set_caption(titre_fenetre)# on definit le titre de la fenetre

        frame_rate = 20
        pygame.mixer.init()
        pygame.mixer.music.load("song/dbz.mp3")
        pygame.mixer.music.play(loops=-1) #permet de lancer le son à l'infinis
        pygame.mixer.music.set_volume(.15)


        continuer = 1

        while continuer:
                        #Chargement et affichage de l'ecran d'accueil
                        accueil = pygame.image.load(image_accueil).convert()
                        fenetre.blit(accueil, (0,0))

                        #Rafraichissement
                        pygame.display.flip()

                        #On remet ces variables
                        continuer_accueil = 1
                        while continuer_accueil:

                                #Limitation de vitesse de la boucle
                                pygame.time.Clock().tick(5)

                                for event in pygame.event.get():

                                        #Si l'utilisateur quitte, on ferme la fenetre de pygame
                                        
                                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                                                pygame.quit()
                                                return

                                        elif event.type == KEYDOWN:
                                                #Lancement du niveau 1
                                                if event.key == K_F1:

                                                        continuer_accueil = 0	#On quitte l'accueil
                                                        choix = 'level/n1'   	#On definit le niveau 1

                                                elif event.key == K_F2:
                                                        continuer_accueil = 0 #On quitte l'accueil
                                                        choix = 'level/n2'      #On definit le niveau 2
                                                elif event.key == K_F3:
                                                        continuer_accueil = 0 
                                                        choix = 'level/n3'
                                                elif event.key == K_F4:
                                                        continuer_accueil = 0
                                                        choix = 'level/n4'
                                                elif event.key == K_F5:
                                                        continuer_accueil = 0
                                                        choix = 'level/n5'
                                                elif event.key == K_F6:
                                                        continuer_accueil = 0
                                                        choix = 'level/n6'
                                                elif event.key == K_F7:
                                                        continuer_accueil = 0
                                                        choix = 'level/n7'
                        if choix != 0:

                                #Chargement du fond
                                fond = pygame.image.load(image_fond).convert_alpha()

                                #Génerer un niveau à partir d'un fichier
                                niveau = Niveau(choix)
                                niveau.generer()
                                niveau.afficher(fenetre)
                                goku = Perso("picture/goku3.png","picture/goku2.png","picture/goku.png","picture/goku1.png", niveau)#on définit le perso et ses différentes position à chaque déplacement



                        continuer_jeu = 1
                        frame_count = 0
                        life = 4
                        while continuer_jeu:
                                        


                                #Limitation de vitesse de la boucle

                                for event in pygame.event.get():


                                        #Si l'utilisateur quitte, on met la variable qui continue le jeu=0, donc retour a l'accueil
                                        
                                        if event.type == QUIT:
                                                continuer_jeu = 0

                                        elif event.type == KEYDOWN:
                                                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                                                if event.key == K_ESCAPE:
                                                        continuer_jeu = 0

                                                #Touches de déplacement de Goku
                                                elif event.key == K_RIGHT:
                                                        goku.deplacer('droite')
                                                elif event.key == K_LEFT:
                                                        goku.deplacer('gauche')
                                                elif event.key == K_UP:
                                                        goku.deplacer('haut')
                                                elif event.key == K_DOWN:
                                                        goku.deplacer('bas')



                               
                                fenetre.blit(fond, (0,0)) #On place le fond
                                pygame.time.Clock().tick(20)#Limitation de vitesse de la boucle
                                total_seconds = frame_count // frame_rate # frame_count est egale au nombre de boucle depuis le debut du jeu , frame_rate est egale au nombre de boucle en 1 seconde
                                minutes = total_seconds // 60# On caclule le nombre de minutes
                                seconds = total_seconds % 60# On fait en sorte que seconds ne puisse pas depasser 60
                                el_font = pygame.font.SysFont("monospace", 15)# on définit la police du timer
                                output_string = "Temps: {0:02}:{1:02}".format(minutes, seconds)# on la variable string du timer
                                timer = el_font.render(output_string, 1,(255,255,0))#on ajoute des paramètres à la variable string 'output_string'
                                fenetre.blit(timer, (1, 670))# on definit la position du timer
                                frame_count += 1# frame_count augmente de 1 par boucle

                                        

                                

                                        

                                        

                                if niveau.structure[goku.case_y][goku.case_x] == '1': # si goku arrive à la boule de cristal , retour au menu
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '2':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '3':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '4':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '5':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '6':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == '7':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == 'Z':
                                        continuer_jeu = 0
                                if niveau.structure[goku.case_y][goku.case_x] == 'Q': # si goku arrive a sa pos du départ , on enlève une vie
                                        goku.case_x -= 1 # on deplace la pos de goku de -1 pour x pour pas que le compteur de v arrive directement à 0
                                        life -= 1

                                if life == 0: #on affiche les coeurs en fonction des vies restantes
                                        continuer_jeu =0
                                        coeur1 = pygame.image.load(image_dead).convert_alpha()
                                        coeur2 = pygame.image.load(image_dead).convert_alpha()
                                        coeur3 = pygame.image.load(image_dead).convert_alpha()
                                        
                                if life == 3:
                                        
                                        coeur1 = pygame.image.load(image_life).convert_alpha()
                                        coeur2 = pygame.image.load(image_life).convert_alpha()
                                        coeur3 = pygame.image.load(image_life).convert_alpha()
                                        
                                if life == 2:
                                        
                                        coeur1 = pygame.image.load(image_life).convert_alpha()
                                        coeur2 = pygame.image.load(image_life).convert_alpha()
                                        coeur3 = pygame.image.load(image_dead).convert_alpha()
                                        
                                         
                                        
                                if life == 1:
                                        
                                        coeur1 = pygame.image.load(image_life).convert_alpha()
                                        coeur2 = pygame.image.load(image_dead).convert_alpha()
                                        coeur3 = pygame.image.load(image_dead).convert_alpha()

                                fenetre.blit(coeur1, (525,665)) #placement des coeurs
                                fenetre.blit(coeur2, (575,665))
                                fenetre.blit(coeur3, (625,665))
                                        

                                niveau.afficher(fenetre) 

                                fenetre.blit(goku.direction, (goku.x, goku.y)) #on place goku fonction de sa position ainsi que sa direction (bas, haut...)

                                pygame.display.flip()



                                

                                        




