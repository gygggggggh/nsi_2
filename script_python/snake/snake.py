from tkinter import *
import random

f = Tk()
f.title('snake')
f.iconphoto(True, PhotoImage(file='script_python/snake/snake.png'))


# on choisis une couleur aleatoir en hexadecimal 
hexa= ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]





# taille de la fenêtre
hauteur_f = 500
largeur_f = 500

#taille de l'ecran 
largeur_ecran = f.winfo_screenwidth()
hauteur_ecran = f.winfo_screenheight()

cor_x = int((largeur_ecran/2) - (largeur_f/2))
cor_y = int((hauteur_ecran/2) - (hauteur_f/2))

f.geometry("{}x{}+{}+{}".format(largeur_f, hauteur_f, cor_x, cor_y))
f.resizable(1,1)

grille = Canvas(width=30, height=30, bg = hexa)
grille.create_rectangle(100,100,100,100, outline='red',)
grille.grid(row=0, column=0,)


if  __name__ == '__main__' :
    f.mainloop()