
from tkinter import *
import random

f = Tk()
f.title('snake')
f.iconphoto(True, PhotoImage(file='script_python/snake/snake.png'))

# variable pour stocker le score 
score = 0

# taille de la fenêtre
hauteur_f = 500
largeur_f = 500

#taille de l'ecran 
largeur_ecran = f.winfo_screenwidth()
hauteur_ecran = f.winfo_screenheight()


cor_x = int((largeur_ecran/2) - (largeur_f/2))
cor_y = int((hauteur_ecran/2) - (hauteur_f/2))

f.geometry("{}x{}+{}+{}".format(largeur_f, hauteur_f, cor_x, cor_y))

f.resizable(0,0)

grille = Canvas(f, width =500, height = 450, bg = "black", )
grille.pack(side="bottom")

score = Canvas(f, width =500, height = 60, bg = "white", relief = 'raised',  bd = '6')
score.create_text(250,20, text = 'score: '+ str(0), font = ('Times', '24', 'bold '))
score.pack(side="top")


nombre_grille = 30

Largeur_Case = (500 / nombre_grille)
Hauteur_Case = (450 / nombre_grille)


def remplir_case (x, y):
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case

    grille.create_rectangle(Origine_snake_X1, Origine_snake_Y1, Origine_snake_X2, Origine_snake_Y2, fill="green")





if  __name__ == '__main__' :
    f.mainloop()
