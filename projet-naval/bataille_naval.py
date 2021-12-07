# NSI 1ère - Projet Bataille navale - Octobre 2021

# Par Schertzer Dylan, Guilleux-Riff Liam et Gobert Mathys.

'''                                        |_
                                       ---/ |
                                       ___\_|__
                                      /| o  o |
                       ___           / |______|\          ___
                  ====/___\  ,------,--|------|--.       /___\====
    _________________,|- -|,/---------------------\.____,|- -|,______________
    \                       \. . . . . . . . . . . ./                       /     , 
 ,   \   o           o           o           o           o           o     /    ,   )',    ,     ,(
=)'===\___________________________________________________________________/==="('=='""=='"(=='-'  ',

                                Bataille  navale 
               <------------------------------------------------->
'''                      

# Importation des fichiers contenant les fonctions nécessaire au bon fonctionnement du programme.

from bataille_navale1 import *
from bataille_navale2 import *



def main():

    # Cette fonction donne la possibilité au joueur de choisir le niveau auquel il veut jouer. 
    # Pour choisir le niveau, le joueur devra entrer un chaine entre 1, 2 ou HIGH SCORE.    
    # Si le texte s'affiche mal, il faut agrandir la fenêtre. 

    reponse = input('''

██████╗  █████╗ ████████╗ █████╗ ██╗██╗     ██╗     ███████╗    ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║██║     ██║     ██╔════╝    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     ██╔════╝
██████╔╝███████║   ██║   ███████║██║██║     ██║     █████╗      ██╔██╗ ██║███████║██║   ██║███████║██║     █████╗  
██╔══██╗██╔══██║   ██║   ██╔══██║██║██║     ██║     ██╔══╝      ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║     ██╔══╝  
██████╔╝██║  ██║   ██║   ██║  ██║██║███████╗███████╗███████╗    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                   
                                                                                                                   
                         
        ╔═════════════════════════════════════════╗ 
        ║ [1]           [2]          [HIGH_SCORE] ║
        ╚═════════════════════════════════════════╝   
        
         ▶ ''').capitalize()
            
    
    
    # Selon la réponse du joueur, le programme lancera le niveau correspondant.
    
    if reponse ==  '1' :
        niveau1()
    if reponse ==  '2' :          
        print('\nWORK IN PROGRESS\n ')
        exit()
    if reponse ==  'HIGH_SCORE'  :
        with open('score.txt','r') as f :
            ligne = f.readline()
            print('\n'+ligne)
    else:
        print('Tu dois choisir entre 1, 2 ou HIGH SCORE ')
        main()
        
main() # <--------------- On exécute le code ici.

