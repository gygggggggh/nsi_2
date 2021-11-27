# NSI 1ere - Projet Bataille navale - octobre 2020




'''                                        |_
                                       ---/ |
                                       ___\_|__
                                      /| o  o |
                       ___           / |______|\          ___
                  ====/___\  ,------,--|------|--.       /___\====
    _________________,|- -|,/---------------------\.____,|- -|,______________
    \                       \. . . . . . . . . . . ./                       /     , 
 ,  \   o           o           o           o           o           o     /    ,   )',    ,     ,(
=)'===\___________________________________________________________________/==="('=='""=='"(=='-'  ',

                                Bataille  navale 
               <------------------------------------------------->
'''                      



# Importation des modules nécessaires au bon fonctionnement du programme.

from os import  write
from random import randint
from datetime import datetime
'''NIVEAU 1'''




def generer_bat() :

    # On génère le bateau mystère dans un emplacement aléatoire avec le module randint de random.
    
    xB = randint (1, 10)
    yB = randint (1, 10)
    return (xB, yB)


def tirer():

    # On crée la fonction de tir grâce à l'utilisateur (fonction input).
    # Puis le programme vérifie si le joueur respecte les règles : si oui, le programme continue, 
    # si non, le programme se relance.
    
    while True:
        try:
            x = int(input('Choisi une colonne de 1 a 10 : '))
            y = int(input('Choisi une ligne de 1 a 10 : '))
        except ValueError:
                print("\nvous devez entrer un nombre\n")
        else:
            if x  < 1 :
                print("\n un  nombre  est trop petit\n")
                tirer()
            if y  < 1 :
                print("\n un  nombre est trop petit\n")  
                tirer() 
            if x  > 10 : 
                print("\nun nombre  est trop grand\n")
                tirer()
            if y  > 10 : 
                print("\nle nombre de ta ligne est trop grand\n")  
                tirer() 
            else:
                return  x,y 
 
def result(bat, t):

    # On compare la fonction tir à la fonction du bateau mystère pour savoir si les coordonnées concordent.
    # Si les

    coup  = 0
    if bat[0] == t[0] and bat[1] != t[1] :
        print("\nEn vue sur la colone !\n")
        coup += 1
    if bat[1] != t[1] and bat[0] == t[0] :
        print("\nEn vue sur la ligne !\n ")
        coup += 1
    if bat[0] == t[0] and bat[1] == t[1] :
        print('\nCoulé !\n')
        fichier()
        exit()
        
    else:
        print("\nÀ l’eau\n")
        
    
        
 
 
def niveau1() :
    
# On crée une fonction pour utiliser ce code en boucle.

    bat = generer_bat()
    while True:
        print(bat)
        t = tirer()
        result(bat, t)
        
        
# Création de la fonction qui enregistre le nom des utilisateurs et la date à laquelle ils ont joué.

def fichier():
    lenth_nom  = 0
    nombre_unite = 1   
    nom = str(input('Choisis un nom : '))  
    if nom == '':
        nom = 'invité'    
    for chr in nom:
       lenth_nom  += 1
    if lenth_nom > 9 :
        nombre_unite += 1    
    if lenth_nom > 99:
        print("ce nom est trop grand")
    date= datetime.now()    
    date_2 = date.strftime("%Y-%m-%d %H:%M:%S ")
    with open("score.txt","a",) as obj :
        obj.write(f'\n{nombre_unite} {lenth_nom} {nom} {date_2}') 
    return nombre_unite , lenth_nom 