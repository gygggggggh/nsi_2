from tkinter import *
from random import randint 

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


MOUVEMENT = (0, 0)

SCORE = 0

PERDU = 0




cor_x = int((largeur_ecran/2) - (largeur_f/2))
cor_y = int((hauteur_ecran/2) - (hauteur_f/2))

f.geometry("{}x{}+{}+{}".format(largeur_f, hauteur_f, cor_x, cor_y))
f.resizable(1,1)



grille = Canvas(f, width =500, height = 450,bg = 'black')
grille.pack(side="bottom")

score = Canvas(f, width =500, height = 60, bg = "#369BE3", relief = 'raised',  bd = '6')
score.pack(side="top")
score.create_text(250,20, text = "score: " + str(SCORE) , font = ('Times', '24', 'bold '))
score.pack(side="top")


nombre_grille = 15

Largeur_Case = (500 / nombre_grille)
Hauteur_Case = (450 / nombre_grille)


def remplir_case (x, y):
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_rectangle(Origine_snake_X1, Origine_snake_Y1, Origine_snake_X2, Origine_snake_Y2, fill="green")

def case_aleatoire():
    
    Aleatoire_X = randint(0, nombre_grille - 1)
    Aleatoire_Y = randint(0, nombre_grille - 1)

    return (Aleatoire_X, Aleatoire_Y)


def draw_snake(snake):
    for case in snake:
        x, y = case
        remplir_case(x, y)


def etre_dans_snake(case):
    if case in SNAKE :
        EtreDedans = 1
    else:
        EtreDedans = 0

    return EtreDedans

def fruit_aleatoire():

    random_fruit = case_aleatoire()
    while (etre_dans_snake(random_fruit)):
        random_fruit = case_aleatoire

    return random_fruit

def dessine_fruit():
    global FRUIT
    x, y = FRUIT
    
    OrigineCaseX1 = x * Largeur_Case
    OrigineCaseY1 = y * Hauteur_Case
    OrigineCaseX2 = OrigineCaseX1 + Largeur_Case
    OrigineCaseY2 = OrigineCaseY1 + Hauteur_Case
    
    grille.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill = "red")

def q(event):
    global MOUVEMENT
    MOUVEMENT = (-1, 0)
    
f.bind("<q>", q)

def d(event):
    global MOUVEMENT
    MOUVEMENT = (1, 0)
    
f.bind("<d>",d)

def z(event):
    global MOUVEMENT
    MOUVEMENT = (0, -1)
    
f.bind("<z>",z)

def s(event):
    global MOUVEMENT
    MOUVEMENT = (0, 1)
    
f.bind("<s>",s)    

def serpent_mort(NouvelleTete):
    global PERDU
    
    NouvelleTeteX, NouvelleTeteY = NouvelleTete
    
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= nombre_grille or NouvelleTeteY >= nombre_grille:
        PERDU = 1

def score_update():
    
    global SCORE

    SCORE = SCORE + 1
    score.delete(0.0, 3.0)
    score.create_text( "score: " + str(SCORE) + "\n")
    
def mise_a_jour_snake():
    
    global SNAKE, FRUIT

    (AncienneTeteX, AncienneTeteY) = SNAKE[0]
    MouvementX, MouvementY = MOUVEMENT
    NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
    serpent_mort(NouvelleTete)
    SNAKE.insert(0, NouvelleTete)

    if NouvelleTete == FRUIT:
       
        FRUIT = fruit_aleatoire()
        
        score_update()
    else:
        SNAKE.pop()   
 
 
def boucle():
    
    f.update
    f.update_idletasks()
    mise_a_jour_snake()

    grille.delete("all")
    dessine_fruit()

    draw_snake(SNAKE)

    if PERDU:
       
        score.delete(0.0, 3.0)

        score.text(END, "score finale : ")
    else:
        
        f.after(70, boucle)   



SNAKE = [case_aleatoire()]
FRUIT = fruit_aleatoire()
MOUVEMENT = (0, 0)

SCORE = 0

PERDU = 0


f.after(0, boucle())   
f.mainloop()

