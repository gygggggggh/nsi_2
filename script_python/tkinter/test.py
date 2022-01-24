# coding: utf8
from tkinter import *
import os
import tkinter.messagebox
from tkinter import filedialog

f = Tk()
f.title("Liste de tâches")
label1 = Label(f, text="Nouvelle tâche :")
# Ajout d'une image pour égayer l'ensemble. Le fichier image doit être
# présent dans le répertoire courant de l'application (dans cet exemple).
# Pour gérer du JPEG cf. https://www.nemoquiz.com/python/images-in-tkinter/
# Avantage du PNG : pas de perte (format non destructeur) et gestion
# de la transparence.
# Inconvénient du PNG : fichiers plus volumineux que du JPEG.
icone = PhotoImage(file="notes.png")
label2 = Label(f, image=icone)
# Une boîte de saisie, cf. http://tkinter.fdex.eu/doc/entw.html#Entry
# (on validera une saisie en appuyant sur Entrée du clavier, cf. plus bas).
# Attention : cette touche N'est PAS celle du pavé numérique !
saisie_tache = Entry(f)
# Une liste simple, cf. http://tkinter.fdex.eu/doc/lbw.html#Listbox.
liste_taches = Listbox(f, height=6)
b = Button(f, text="Effacer la liste de tâches")
label1.grid(row=0, column=0, pady=3)
saisie_tache.grid(row=0, column=1)
label2.grid(row=1, column=0, pady=3)
liste_taches.grid(row=1, column=1)
b.grid(row=2, column=0, columnspan=2, pady=3)

def ajouter_tache(event=None): # définition du gestionnaire
    tache = saisie_tache.get()
    liste_taches.insert("end", tache)
    saisie_tache.delete(0, "end")

saisie_tache.bind("<Return>", ajouter_tache) # liaison

# Vider la liste des taches
# Fonction lambda : fonction dépourvue de nom, comprenant une seule et unique
# instruction, retournant une « valeur ».
b["command"] = lambda : liste_taches.delete(0, "end")
# Supprimer une tâche, en appuyant sur la doute "Suppr." (à droite de la
# touche Entrée).
liste_taches.bind("<Delete>", lambda event=None: liste_taches.delete(liste_taches.curselection()))

# Cette variable Tkinter sert à connaître l'index de la tâche sélectionnée.
# On pourrait aussi utiliser une variable normale et la déclarer « globale »
# dans chaque fonction où on a besoin de la modifier...
index = IntVar()

def clic_sur_item(event): # Ce qu'on fait lorsqu'on clique sur un item
    # On stocke dans la variable entière "index" le numéro de la tâche
    # la plus proche de l'emplacement où l'on a cliqué (on se base sur
    # l'ordonnée du point cliqué pour le déterminer).
    index.set(liste_taches.nearest(event.y))

def relacher_sur_item(event): # Ce qu'on fait lorsqu'on relache le clic sur un
    # autre item. On récupère l'item sur lequel on a initié le clic, puis
    # l'index et l'item sur lequel on a relaché le clic et on échange si
    # nécessaire les items.
    item1 = liste_taches.get(index.get())
    # index2 est une variable « standard » !
    index2 = liste_taches.nearest(event.y)
    if index2 != index.get():
        item2 = liste_taches.get(index2)
        liste_taches.delete(index.get()) # On supprime le premier item ...
        liste_taches.insert(index.get(), item2) # ...qu'on remplace par le second
        liste_taches.delete(index2) # Et vice versa !
        liste_taches.insert(index2, item1)

# Cf. https://docs.python.org/3/library/tkinter.html#bindings-and-events pour
# comprendre le add="+". Cet article donne une illustration de l'intérêt
# du add='+' : https://www.pythontutorial.net/tkinter/tkinter-event-binding/
liste_taches.bind("<Button-1>", clic_sur_item, add="+")
liste_taches.bind("<ButtonRelease-1>", relacher_sur_item)

def charger():
    # Exercice : à vous de coder le contenu de cette fonction !
    tkinter.messagebox.showinfo("Oups !", "Vous devrez coder cette fonction !")

def enregistrer():
    # Cf. http://tkinter.unpythonic.net/wiki/tkFileDialog
    # Il peut être utile de connaître le répertoire courant (option initialdir).
    # Pour cela, mettre import os en tête de fichier, puis utiliser os.getcwd().
    fichier =  filedialog.asksaveasfilename(initialdir = os.getcwd(),
        title = "Choisir un fichier",
        filetypes = (("Fichier de tâches (texte)","*.todo"),))
    if fichier:
        with open(fichier, "w") as f:
            for ligne in liste_taches.get(0,END):
                f.write(ligne+"\n") # +"\n" pour ajouter un saut de ligne à chaque entrée

def a_propos():
    tkinter.messagebox.showinfo("À propos de ce logiciel",
"""Ce logiciel est disponible sous la licence GNU/GPL
(cf. https://www.gnu.org/licenses/gpl-3.0.fr.html).

Saisir une tâche dans la zone
de saisie et valider la saisie
en pressant la touche Entrée
(pas celle du pavé numérique).

Les tâches peuvent être 
réorganisées par simple
glisser-déposer.

Pour supprimer une tâche,
la sélectionner puis presser
la touche Suppr.
""")

# Créer une barre de menu principale
barre_de_menus = Menu(f)
# Créer une barre de menu secondaire
menu_actions = Menu(barre_de_menus, tearoff=1) # tearoff=0 permet d'avoir un menu « non détachable »
menu_actions.add_command(label="Charger", command=charger)
menu_actions.add_command(label="Enregistrer", command=enregistrer)
menu_actions.add_separator()
menu_actions.add_command(label="Quitter", command=f.quit)
# Ajouter la barre de menu secondaire à la barre de menu principale
barre_de_menus.add_cascade(label="Actions", menu=menu_actions)
# Ajouter une commande à la barre de menu principale
barre_de_menus.add_command(label="À propos", command=a_propos)

# Ajouter la barre de menu principale à la fenêtre
f.config(menu=barre_de_menus)

f.mainloop()
