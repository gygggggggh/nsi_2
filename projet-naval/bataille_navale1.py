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



# Importation des modules nécessaires au bon fonctionnement du programme.

from os import  write
from random import expovariate, randint
from datetime import datetime
from time import *

'''NIVEAU 1'''


coup = 0

def generer_bat() :

    ''' génère le bateau mystère dans un emplacement compris entre 1 et 
        10 avec le module randint de random.'''
    
    xB = randint (1, 10)
    yB = randint (1, 10)
    return (xB, yB)


def tirer():

    ''' crée la fonction de tir grâce à la fonction input
      puis le programme vérifie si le joueur respecte les règles : si oui, le programme continue, 
      si non, le programme se relance.'''
    try:
        x = int(input('Choisi une colonne de 1 a 10 : '))
        y = int(input('Choisi une ligne de 1 a 10 : '))
    except ValueError:
            print("\nVous devez entrer un nombre\n")
    else:
        if x  < 1 :
            print("\n un nombre  est trop petit\n")
            tirer()
        if y  < 1 :
            print("\n un  nombre est trop petit\n")  
            tirer() 
        if x  > 10 : 
            print("\n un nombre  est trop grand\n")
            tirer()
        if y  > 10 : 
            print("\n un nombre  est trop grand\n")  
            tirer() 
        else:
            return  x,y 
 
def result(bat, t):

    """ compare la fonction tir à la fonction du bateau mystère pour savoir si les coordonnées 
    concordent et dit si le bateau est coule ou pas."""
    try :
        if bat[0] == t[0] and bat[1] != t[1]:
            print("\nEn vue sur la ligne ?\n")

        if bat[0] != t[0] and  bat[1] == t[1] :
            print("\nEn vue sur la colonne? \n ")

        if bat[0] == t[0] and bat[1] == t[1] :
            print('\nCoulé !\n')
            fichier()
            exit()
            
        if bat[0] != t[0] and bat[1] != t[1] :
            print("\nÀ l’eau\n")
    except TypeError :
                      print("il faut entrée un nombre \n")
                      
                      
        
 
 
def niveau1() :
    """crée une boucle pour utiliser ce code en jusqu'a que l'utilisateur ait trouvé le bateaux"""
    bat = generer_bat()
    while True:
        t = tirer()
        result(bat, t,)
        


def fichier():
    '''demande et enregistre le nom des utilisateurs, leur score, et 
      la date à laquelle ils ont joué. ''' 

    
    nom = str(input('Choisis un nom : ')) 
    if nom == '':
       nom = 'inviter'
    ERROR404 = randint(2,999)
    date= datetime.now()    
    date_2 = date.strftime("%Y-%m-%d %H:%M:%S ")
    with open("score.txt","a",) as obj :
       obj.write(f'\nLe  score de {nom} a {date_2} est de {ERROR404} coups \n ') 
