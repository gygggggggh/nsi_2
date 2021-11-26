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

coup = 0

from os import write
from random import randint
from time import *
from datetime import datetime
'''NIVEAU 1'''




def generer_bat() :
    # on génère le bateau mystère avec le module randint de random
    xB = randint (1, 10)
    yB = randint (1, 10)
    return (xB, yB)


def tirer():
    #On crée la fonction de tir grace a l'utlisateurs (fonction input) 
    #puis on regarde si il respecte les regles 
    
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

# On compare la fonction tir à la fonction du bateau mystère pour savoir si les données concordent 

def result(bat, t):
    coup = 0
    # On compare la fonction tir à la fonction du bateau mystère pour savoir si les données concordent 
    if bat[0] == t[0] and bat[1] != t[1] :
        print("\nEn vue sur la colone !\n")
        coup +=1
    if bat[1] != t[1] and bat[0] == t[0] :
        print("\nEn vue sur la ligne!\n ")
        coup += 1
    if bat[0] == t[0] and bat[1] == t[1] :
        print('\ncoulé\n')
        fichier(coup)
    else:
        print("\nÀ l’eau\n")
        
    
        
 
 
def niveau1() :
# on crée une fonction pour utilise ce code en boucle 
    bat = generer_bat()
    while True:
        print(bat)
        t = tirer()
        result(bat, t)
        sleep(1)
        
        
def fichier(coup) :
    Coup = coup
    i = 0
    nombre_unite = 1   
    nom = str(input('Choisi un nom : '))  
     
    if nom == '':
        nom = 'inviter'
        
        
    for chr in nom:
        i += 1
    lenth_nom = i
    
    
    if lenth_nom > 9 :
        nombre_unite += 1
        
        
    if lenth_nom > 99:
        print("ce nom est trop grand")
        fichier()
    date= datetime.now()    
    date_2 = date.strftime("%Y-%m-%d %H:%M:%S ")
    with open("score.txt","a",) as obj :
        obj.write(f'\n{nombre_unite} {lenth_nom} {nom} {Coup}{date_2}\n') 
    print(coup)
    exit()
    

    


