
import tkinter as tk
import random

f = tk.Tk()
f.title('snake')
f.iconphoto(True, tk.PhotoImage(file='script_python/snake/snake.png'))

hexa= ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]

f.config(background=hexa)



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


if  __name__ == '__main__' :
    f.mainloop()
