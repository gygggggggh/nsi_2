# NSI 1ere - Projet Bataille navale - octobre 2020

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


from bataille_navale1 import *
from bataille_navale2 import *



def main():
    #cette fonction sert a chosir quelle niveau jouer en demandant a un utilisateur 
    # un chiffre entre 1 et 3
    
    # si le texte est s'affiche mal il faut agrandir la fenetre 
    reponse = input('''

██████╗  █████╗ ████████╗ █████╗  ██╗ ██╗     ██╗     ███████╗    ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗ ██║ ██║     ██║     ██╔════╝    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     
██████╔╝███████║   ██║   ███████║ ██║ ██║     ██║     █████╗      ██╔██╗ ██║███████║██║   ██║███████║██║     
██╔══██╗██╔══██║   ██║   ██╔══██║ ██║ ██║     ██║     ██╔══╝      ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║     
██████╔╝██║  ██║   ██║   ██║  ██║ ██║ ███████╗███████╗███████╗    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝ 
                                                                        
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
        with open ('score.txt', 'r') as f:
            for ligne in f:
                print(ligne)
    else:
        print('tu dois choisir entre 1 ou 2 ou HIGH SCORE ')
        main()
        
main() # <--------------- on execute le code ici

