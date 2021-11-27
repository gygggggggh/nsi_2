
# NSI 1ère - Projet Bataille navale - Octobre 2020


# Importation des modules nécessaires au bon fonctionnement du programme.

import math
from random import randint

'''NIVEAU 2'''

# La définition de la liste_p ne sert à rien, cette fonction n'est qu'une liste des multiple possibilités
# de coordonnées du bateau mystère.

# liste_p =[[[1,1][1,2][1,3]][[1,1][2,1][3,1]][[1,2][1,3][1,4]][[1,2][2,2][3,2]][[1,3][1,4][1,5]][[1,3][2,3][3,3]][[1,4][1,3][1,2]][[1,4][2,4][3,4]][[1,5][2,5][3,5]][[1,5][1,4][1,3]][[2,1][2,2][2,3]][[2,1][3,1][4,1]][[2,2][2,3][2,4]][[2,2][3,2][4,2]][[2,3][2,4][2,5]][[2,3][3,3][4,3]][[2,3][2,2][2,1]][[2,4][3,4][4,4]][[2,4][2,3][2,2]][[2,5][3,5][4,5]][[2,5][2,4][2,3]][[3,1][3,2][3,3]][[3,1][4,1][4,2]][[3,2][3,3][3,4]][[3,2][4,2][5,2]][[3,2][2,2][1,2]][[3,3][3,4][3,5]][[3,3][4,3][5,3]][[3,3][3,2][3,1]][[3,3][2,3][1,3]][[3,4][4,4][5,4]][[3,4][3,3][3,2]][[3,4][2,4][1,4]][[3,5][4,5][5,5]][[3,5][3,4][3,3]][[3,5][2,5][1,5]][[4,1][3,1][2,1]][[4,2][4,3][4,4]][[4,2][3,2][2,2]][[4,3][4,2][4,1]][[4,3][3,3][2,3]][[4,3][4,4][4,5]][[4,4][4,3][4,2]][[4,4][3,4][2,4]][[4,5,][4,4][4,3]][[4,5][3,5][2,5]][[5,1][5,2][5,3]][[5,2][5,3][5,4]][[5,3][5,2][5,1]][[5,3][4,3][3,3]][[5,4][5,3][5,2]][[5,4][5,3][5,2]][[5,5][5,4][5,3]][[5,5][4,3][3,3]]]


plat = []

# Fonctions servant à créé le plateau et à l'imprimer dans le terminal.

for x in range(5):
    plat.append(["-"] * 5) 

def print_plat(plat):
    print('  1 2 3 4 5' )
    for col in range(len(plat)): 
        print(str(col+1) + " " + " ".join(plat[col])) 
    print()
    

def tirer():
    
    # On crée la fonction de tir grâce à l'utilisateur (fonction input).
    # Puis le programme vérifie si le joueur respecte les règles : si oui, le programme continue, 
    # si non, le programme se relance.
    
    while True:
        try:
            x = int(input('Choisi une colonne de 1 a 5 : '))
            y = int(input('Choisi une ligne de 1 a 5 : '))
        except ValueError:
                print("\nvous devez entrer un nombre\n")
        else:
            if x  < 1 :
                print("\n un  nombre  est trop petit\n")
                tirer()
            if y  < 1 :
                print("\n un  nombre est trop petit\n")  
                tirer() 
            if x  > 5 : 
                print("\nun nombre  est trop grand\n")
                tirer()
            if y  > 5 : 
                print("\nle nombre de ta ligne est trop grand\n")  
                tirer() 
            else:
                return  x,y 
 


   
# --> Cette partie du programme ne fonctionne pas, on donc mise en commentaire.

# def gen_bateau(liste_p):
    # n = randint(0,57)
    # print(liste_p)


# print(print_plat(plat))
# for i in range (100):
   # print(gen_bateau(liste_p)