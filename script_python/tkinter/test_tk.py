# coding: utf8
from tkinter import *
from math import *

def evaluer(event):
    r.set(str(eval(saisie.get())))

f = Tk()
f.geometry("400x300+400+200")
# Il faut absolument créer une fenêtre principale AVANT de créer une variable
# Tkinter ! Sinon vous obtiendrez une erreur : « RuntimeError: Too early to
#create variable: no default root window »
r = StringVar()
saisie = Entry(f)
saisie.bind("<Return>", evaluer)
saisie.pack()
Label(f, text="Résultat :").pack() # Pas besoin de se souvenir de ce widget !
resultat = Label(f, textvariable=r)
resultat.pack()

f.mainloop()
