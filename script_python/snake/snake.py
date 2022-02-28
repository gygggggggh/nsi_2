<<<<<<< HEAD
from tkinter import *
import pygame
from random import randint
from time import sleep

pygame.init()

'''
musique = pygame.mixer.Sound("musique.wav")
empty_channel4 = pygame.mixer.find_channel()
empty_channel4.play(musique , loops = -1)
'''

turn = pygame.mixer.Sound("_turn_.ogg")

f = Tk()
f.title('snake')
f.iconphoto(True, PhotoImage(file='snake.png'))


# taille de la fenêtre
hauteur_f = 500
largeur_f = 500

#taille de l'ecran 
largeur_ecran = f.winfo_screenwidth()
hauteur_ecran = f.winfo_screenheight()


MOUVEMENT = (0, 0)

SCORE = 0

PERDU = 0

with open('score.txt','r') as obj :
         HIGHSCORE = obj.readline()
        

cor_x = int((largeur_ecran/2) - (largeur_f/2))
cor_y = int((hauteur_ecran/2) - (hauteur_f/2))

f.geometry("{}x{}+{}+{}".format(largeur_f, hauteur_f, cor_x, cor_y))
f.resizable(0,0)



grille = Canvas(f, width =500, height = 450,bg = '#752B2B' ,)
grille.pack(side="bottom")

score = Canvas(f, width =500, height = 60, bg = "#369BE3", relief = 'raised',  bd = '6')
score.pack(side="top")
texte =  score.create_text(80,20, text = "score: " + str(SCORE) , font = ('Times', '15', 'bold '))
score.itemcget(texte, 'text')
score.pack(side="top")

score.create_text(320,20, text = "high score: " + HIGHSCORE , font = ('Times', '15', 'bold ') , anchor= 'w')
score.pack(side="top")


nombre_grille = 16

Largeur_Case = (500 / nombre_grille)
Hauteur_Case = (450 / nombre_grille)


def remplir_case (x, y):
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_rectangle(Origine_snake_X1, Origine_snake_Y1, Origine_snake_X2, Origine_snake_Y2, fill="green" ,outline = 'white' )
   
def case_aleatoire():
    
    Aleatoire_X = randint(0, nombre_grille - 1)
    Aleatoire_Y = randint(0, nombre_grille - 1)
    return Aleatoire_X, Aleatoire_Y


def draw_snake(snake):
    for case in snake:
        (x, y) = case
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

    return (random_fruit)

def dessine_fruit():
    global FRUIT
    try:
        x, y = FRUIT
    except TypeError:
        FRUIT = fruit_aleatoire()
        try:
            x, y = FRUIT
        except TypeError:
            FRUIT = fruit_aleatoire()
            try:
                x, y = FRUIT
            except TypeError:
                x, y = 0,0
        
        
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_oval( Origine_snake_X1, Origine_snake_Y1,  Origine_snake_X2, Origine_snake_Y2 , fill = "red",outline='white')
    
def gauche(event):
    global MOUVEMENT
    if  MOUVEMENT == (1, 0) or MOUVEMENT == (-1, 0) :
        pass
    else:
        MOUVEMENT = (-1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def droite(event):
    global MOUVEMENT
    if  MOUVEMENT == (-1, 0) or MOUVEMENT == (1, 0):
        pass
    else:
        MOUVEMENT = (1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def haut(event):
    global MOUVEMENT
    if  MOUVEMENT == (0, 1) or MOUVEMENT == (0, -1):
        pass
    else:
        MOUVEMENT = (0, -1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def bas(event):
    global MOUVEMENT
    if  MOUVEMENT == (0, -1) or MOUVEMENT == (0, 1):
        pass
    else:
        MOUVEMENT = (0, 1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
f.bind("<Left>", gauche)
f.bind("<Right>", droite)
f.bind("<Up>", haut)
f.bind("<Down>", bas)
f.bind("<q>", gauche)
f.bind("<d>", droite)
f.bind("<z>", haut)
f.bind("<s>", bas)

def serpent_mort(NouvelleTete):
    pass
    global PERDU
    
    NouvelleTeteX, NouvelleTeteY = NouvelleTete
    
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= nombre_grille or NouvelleTeteY >= nombre_grille:
        PERDU = 1
        empty_channel4.stop()
        game_over = pygame.mixer.Sound("mixkit-retro-game-over-1947.wav")
        empty_channel2 = pygame.mixer.find_channel()
        empty_channel2.play(game_over)
        sleep(2.5)
        f.quit()
def score_update():
    
    global SCORE

    SCORE += 100
    score.itemconfigure(texte,text = "score: " + str(SCORE) , font = ('Times', '15', 'bold '))
    score.pack(side="top")
    
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
            eat = pygame.mixer.Sound("_eat_.wav")
            empty_channel = pygame.mixer.find_channel()
            empty_channel.play(eat)
    else:
        SNAKE.pop()   
 
 
def boucle():
    
    global HIGHSCORE , SCORE
    
    f.update
    f.update_idletasks()
    mise_a_jour_snake()

    grille.delete("all")
    dessine_fruit()
    
    draw_snake(SNAKE)

    if PERDU:
        score.itemconfigure(texte,text = "score : " + str(SCORE) , font = ('Times', '15', 'bold '))
        if SCORE > int(HIGHSCORE) :
            HIGHSCORE = SCORE
            with open("score.txt","w",) as obj :
                obj.write(str(HIGHSCORE))

    else:
        
        f.after(80, boucle)   

SCORE = 0

PERDU = 0

SNAKE = [case_aleatoire()]
FRUIT = fruit_aleatoire()
f.after(0, boucle()) 

  
f.mainloop()


=======
from tkinter import *
import pygame
from random import randint
from time import sleep

pygame.init()
pygame.mixer.music.load("musique.wav")
pygame.mixer.music.play(loops=-1)

turn = pygame.mixer.Sound("_turn_.ogg")

f = Tk()
f.title('snake')
f.iconphoto(True, PhotoImage(file='snake.png'))


# taille de la fenêtre
hauteur_f = 500
largeur_f = 500

#taille de l'ecran 
largeur_ecran = f.winfo_screenwidth()
hauteur_ecran = f.winfo_screenheight()


MOUVEMENT = (0, 0)

SCORE = 0

PERDU = 0

with open('score.txt','r') as obj :
         HIGHSCORE = obj.readline()
        

cor_x = int((largeur_ecran/2) - (largeur_f/2))
cor_y = int((hauteur_ecran/2) - (hauteur_f/2))

f.geometry("{}x{}+{}+{}".format(largeur_f, hauteur_f, cor_x, cor_y))
f.resizable(0,0)



grille = Canvas(f, width =500, height = 450,bg = 'black')
grille.pack(side="bottom")

score = Canvas(f, width =500, height = 60, bg = "#369BE3", relief = 'raised',  bd = '6')
score.pack(side="top")
texte =  score.create_text(80,20, text = "score: " + str(SCORE) , font = ('Times', '15', 'bold '))
score.itemcget(texte, 'text')
score.pack(side="top")

score.create_text(320,20, text = "high score: " + HIGHSCORE , font = ('Times', '15', 'bold ') , anchor= 'w')
score.pack(side="top")


nombre_grille = 16

Largeur_Case = (500 / nombre_grille)
Hauteur_Case = (450 / nombre_grille)


def remplir_case (x, y):
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_rectangle(Origine_snake_X1, Origine_snake_Y1, Origine_snake_X2, Origine_snake_Y2, fill="green" )
   
def case_aleatoire():
    
    Aleatoire_X = randint(0, nombre_grille - 1)
    Aleatoire_Y = randint(0, nombre_grille - 1)
    return Aleatoire_X, Aleatoire_Y


def draw_snake(snake):
    for case in snake:
        (x, y) = case
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

    return (random_fruit)

def dessine_fruit():
    global FRUIT
    try:
        x, y = FRUIT
    except TypeError:
        FRUIT = fruit_aleatoire()
        try:
            x, y = FRUIT
        except TypeError:
            FRUIT = fruit_aleatoire()
            try:
                x, y = FRUIT
            except TypeError:
                x, y = 0,0
        
        
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_oval( Origine_snake_X1, Origine_snake_Y1,  Origine_snake_X2, Origine_snake_Y2 , fill = "red",outline='orange')
    
    
    
def gauche(event):
    global MOUVEMENT
    if  MOUVEMENT == (1, 0) or MOUVEMENT == (-1, 0) :
        pass
    else:
        MOUVEMENT = (-1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def droite(event):
    global MOUVEMENT
    if  MOUVEMENT == (-1, 0) or MOUVEMENT == (1, 0):
        pass
    else:
        MOUVEMENT = (1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def haut(event):
    global MOUVEMENT
    if  MOUVEMENT == (0, 1) or MOUVEMENT == (0, -1):
        pass
    else:
        MOUVEMENT = (0, -1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def bas(event):
    global MOUVEMENT
    if  MOUVEMENT == (0, -1) or MOUVEMENT == (0, 1):
        pass
    else:
        MOUVEMENT = (0, 1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
f.bind("<Left>", gauche)
f.bind("<Right>", droite)
f.bind("<Up>", haut)
f.bind("<Down>", bas)
f.bind("<q>", gauche)
f.bind("<d>", droite)
f.bind("<z>", haut)
f.bind("<s>", bas)

def serpent_mort(NouvelleTete):
    pass
    global PERDU
    
    NouvelleTeteX, NouvelleTeteY = NouvelleTete
    
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= nombre_grille or NouvelleTeteY >= nombre_grille:
        PERDU = 1
        pygame.mixer.music.stop()
        game_over = pygame.mixer.Sound("mixkit-retro-game-over-1947.wav")
        empty_channel2 = pygame.mixer.find_channel()
        empty_channel2.play(game_over)
        sleep(2.5)
        f.quit()
def score_update():
    
    global SCORE

    SCORE += 100
    score.itemconfigure(texte,text = "score: " + str(SCORE) , font = ('Times', '15', 'bold '))
    score.pack(side="top")
    
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
            eat = pygame.mixer.Sound("_eat_.wav")
            empty_channel = pygame.mixer.find_channel()
            empty_channel.play(eat)
    else:
        SNAKE.pop()   
 
 
def boucle():
    
    global HIGHSCORE , SCORE
    
    f.update
    f.update_idletasks()
    mise_a_jour_snake()

    grille.delete("all")
    dessine_fruit()
    
    draw_snake(SNAKE)

    if PERDU:
        score.itemconfigure(texte,text = "score : " + str(SCORE) , font = ('Times', '15', 'bold '))
        if SCORE > int(HIGHSCORE) :
            HIGHSCORE = SCORE
            with open("score.txt","w",) as obj :
                obj.write(str(HIGHSCORE))

    else:
        
        f.after(80, boucle)   

SCORE = 0

PERDU = 0

SNAKE = [case_aleatoire()]
FRUIT = fruit_aleatoire()
f.after(0, boucle()) 

  
f.mainloop()


>>>>>>> 2986f2d85dbf52b4e92900f640481219fa3635cc
