"""Classes du jeu de Labyrinthe Donkey Kong"""
import tkinter
import pygame
import jeu
import time
from pygame.locals import *
from constantes import *


class Niveau:
     
     def el_chron0():
          frame_count = 0
          frame_rate = 60
          start_time = 90
          total_seconds = frame_count // frame_rate
          seconds = total_seconds % 60
          output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
          text = font.render(output_string, True, black)
          screen.blit(text, [250, 280])
          frame_count += 1
          
     
     """Classe permettant de crÃƒÆ’Ã‚Â©er un niveau"""
     def __init__(self, fichier):
          self.fichier = fichier
          self.structure = 0
          
     def generer(self):
          """MÃƒÆ’Ã‚Â©thode permettant de gÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â©rer le niveau en fonction du fichier.
          On crÃƒÆ’Ã‚Â©e une liste gÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â©rale, contenant une liste par ligne ÃƒÆ’Ã‚Â  afficher"""
          #On ouvre le fichier
          with open(self.fichier, "r") as fichier:
               structure_niveau = []
               #On parcourt les lignes du fichier
               for ligne in fichier:
                    ligne_niveau = []
                    #On parcourt les sprites (lettres) contenus dans le fichier
                    for sprite in ligne:
                         #On ignore les "\n" de fin de ligne
                         if sprite != '\n':
                              #On ajoute le sprite ÃƒÆ’Ã‚Â  la liste de la ligne
                              ligne_niveau.append(sprite)
                    #On ajoute la ligne ÃƒÆ’Ã‚Â  la liste du niveau
                    structure_niveau.append(ligne_niveau)
               #On sauvegarde cette structure
               self.structure = structure_niveau


     def afficher(self, fenetre):
          """MÃƒÆ’Ã‚Â©thode permettant d'afficher le niveau en fonction
          de la liste de structure renvoyÃƒÆ’Ã‚Â©e par generer()"""
          #Chargement des images (seule celle d'arrivÃƒÆ’Ã‚Â©e contient de la transparence)
          arrivee1 = pygame.image.load(image_boule1).convert_alpha()
          arrivee2 = pygame.image.load(image_boule2).convert_alpha()
          arrivee3 = pygame.image.load(image_boule3).convert_alpha()
          arrivee4 = pygame.image.load(image_boule4).convert_alpha()
          arrivee5 = pygame.image.load(image_boule5).convert_alpha()
          arrivee6 = pygame.image.load(image_boule6).convert_alpha()
          arrivee7 = pygame.image.load(image_boule7).convert_alpha()
          goku = pygame.image.load(image_goku_haut).convert_alpha()
          goku1 = pygame.image.load(image_goku_bas).convert_alpha()
          goku2 = pygame.image.load(image_goku_gauche).convert_alpha()
          goku3 = pygame.image.load(image_goku_droite).convert_alpha()
          nappa = pygame.image.load(image_Nappa_droite).convert_alpha()
          nappa1 = pygame.image.load(image_Nappa_gauche).convert_alpha()
          nappa2 = pygame.image.load(image_Nappa_haut).convert_alpha()
          nappa3 = pygame.image.load(image_Nappa_bas).convert_alpha()
          contour = pygame.image.load(image_contour).convert_alpha()
          #On parcourt la liste du niveau
          num_ligne = 0
          for ligne in self.structure:
               #On parcourt les listes de lignes
               num_case = 0
               for sprite in ligne:
                    #On calcule la position rÃƒÆ’Ã‚Â©elle en pixels
                    x = num_case * taille_sprite
                    y = num_ligne * taille_sprite
                    if sprite == 'A':
                         fenetre.blit(nappa, (x,y))
                    elif sprite == 'B':
                         fenetre.blit(nappa1, (x,y))
                    elif sprite == 'C':
                         fenetre.blit(nappa2, (x,y))
                    elif sprite == 'D':
                         fenetre.blit(nappa3, (x,y))
                    elif sprite == '1':
                         fenetre.blit(arrivee1, (x,y))
                    elif sprite == '2':
                         fenetre.blit(arrivee2, (x,y))
                    elif sprite == '3':
                         fenetre.blit(arrivee3, (x,y))
                    elif sprite == '4':
                         fenetre.blit(arrivee4, (x,y))
                    elif sprite == '5':
                         fenetre.blit(arrivee5, (x,y))
                    elif sprite == '6':
                         fenetre.blit(arrivee6, (x,y))
                    elif sprite == '7':
                         fenetre.blit(arrivee7, (x,y))
                    elif sprite == 'Z':
                         fenetre.blit(contour, (x,y))
                    num_case += 1
               num_ligne += 1




class Perso:
     """Classe permettant de crÃƒÆ’Ã‚Â©er un personnage"""
     def __init__(self, droite, gauche, haut, bas, niveau):
          #Sprites du personnage
          self.droite = pygame.image.load(droite).convert_alpha()
          self.gauche = pygame.image.load(gauche).convert_alpha()
          self.haut = pygame.image.load(haut).convert_alpha()
          self.bas = pygame.image.load(bas).convert_alpha()
          #Position du personnage en cases et en pixels
          self.case_x = 19
          self.case_y = 2
          self.x = 570
          self.y = 60
          #Direction par dÃƒÆ’Ã‚Â©faut
          self.direction = self.droite
          #Niveau dans lequel le personnage se trouve
          self.niveau = niveau

          
     def ctraileson():
          soundtp = pygame.mixer.Sound('song/songtp.wav')
          soundtp.set_volume(.1)
          soundtp.play()
          


     def deplacer(self, direction):
          pygame.mixer.init()   
          

          """Methode permettant de dÃƒÆ’Ã‚Â©placer le personnage"""

          #DÃƒÆ’Ã‚Â©placement vers la droite
          if direction == 'droite':
               #Pour ne pas dÃƒÆ’Ã‚Â©passer l'ÃƒÆ’Ã‚Â©cran
               if self.case_x < (nombre_sprite_cote - 1):
                       while self.niveau.structure[self.case_y][self.case_x+1] != 'B':
                              
                              self.case_x += 1
                              self.x = self.case_x * taille_sprite
                              if self.niveau.structure[self.case_y][self.case_x] == 'Z':
                                    return
                         
               self.direction = self.droite
               Perso.ctraileson()
               

          #DÃƒÆ’Ã‚Â©placement vers la gauche
          if direction == 'gauche':
               if self.case_x > 0:
                    while self.niveau.structure[self.case_y][self.case_x-1] != 'A':
                            self.case_x -= 1
                            self.x = self.case_x * taille_sprite
                            if self.niveau.structure[self.case_y][self.case_x] == 'Z':
                                    return
                                   
               self.direction = self.gauche
               Perso.ctraileson()
     
               

          #DÃƒÆ’Ã‚Â©placement vers le haut
          if direction == 'haut':
               if self.case_y > 0:
                    while self.niveau.structure[self.case_y-1][self.case_x] != 'D':
                            self.case_y -= 1
                            self.y = self.case_y * taille_sprite
                            
                            if self.niveau.structure[self.case_y][self.case_x] == 'Z':
                                    return
                            
               self.direction = self.haut
               Perso.ctraileson()
               
               

          #DÃƒÆ’Ã‚Â©placement vers le bas
          if direction == 'bas':
               if self.case_y < (nombre_sprite_cote - 1):
                    while self.niveau.structure[self.case_y+1][self.case_x] != 'C':
                            self.case_y += 1
                            self.y = self.case_y * taille_sprite
                            #TODO -> On doit encore arriver à modifier le niveau du son
                            
                            if self.niveau.structure[self.case_y][self.case_x] == 'Z':
                                    return
                                   
               self.direction = self.bas
               Perso.ctraileson()
               

