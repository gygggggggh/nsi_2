from math import *
def inverse():

    while True :
        try:
            nombre = float(input("Entrer un nombre : ").replace(",",'.'))
            inverse = 1/nombre
        except ValueError:
            #ce bloc est execute si une exception de type ValueError est levee dans le bloc try
            print("donne un nombre decimal !")
        except ZeroDivisionError:
            #ce bloc est execute si une exception de type ZeroDivisionError est levee dans le bloc try
            print("Division par zero !")
        else:
            #on arrive ici si aucune exception n’est levee dans le bloc try
            print("L’inverse de", nombre, "est :", inverse)

def racine():
    while True :
        try:
            nombre = float(input("Entrer un nombre : "))
            racine = sqrt(nombre) 
        except ValueError:
            #ce bloc est execute si une exception de type ValueError est levee dans le bloc try
            print("donne un nombre decimal !")
        except ZeroDivisionError:
            #ce bloc est execute si une exception de type ZeroDivisionError est levee dans le bloc try
            print("Division par zero !")
        else:
            #on arrive ici si aucune exception n’est levee dans le bloc try
            print("La racine de ", nombre, "est :", racine)
            
            
racine()