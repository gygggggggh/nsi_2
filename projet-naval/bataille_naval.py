# NSI 1ère - Projet Bataille navale - Octobre 2020

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
                                                                                                                   
                                                                                                                   
                         
        ╔═══════════════════════════════════════════════════════╗ 
        ║ [Niveau 1]           [Niveau 2]          [HIGH SCORE] ║
        ╚═══════════════════════════════════════════════════════╝   
        
         ▶ ''')
            
    if reponse ==  '1' :
        niveau1()
    if reponse ==  '2' :          
        print('\nWORK IN PROGRESS\n ')
        exit()
    if reponse ==  'HIGH SCORE' :
        pass
                
    else:
        print('tu dois choisir entre 1 ou 2 ou HIGH SCORE ')
        main()
        
main() # <--------------- On exécute le code ici.

