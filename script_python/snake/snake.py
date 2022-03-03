from tkinter import *
import pygame
from random import randint
from time import sleep

pygame.init()

# la musique est desactiver par defaut 
'''musique = pygame.mixer.Sound("script_python/snake/musique.wav")
empty_channel4 = pygame.mixer.find_channel()
empty_channel4.play(musique , loops = -1)'''


turn = pygame.mixer.Sound("script_python/snake/_turn_.ogg")

f = Tk()
f.title('snake')
f.iconphoto(True, PhotoImage(file='script_python/snake/snake.png'))


# taille de la fenêtre
hauteur_f = 500
largeur_f = 500

#taille de l'ecran 
largeur_ecran = f.winfo_screenwidth()
hauteur_ecran = f.winfo_screenheight()


MOUVEMENT = (0, 0)

SCORE = 0

PERDU = 0

with open('script_python/snake/score.txt','r') as obj :
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
    '''cette fonction  prend pour parametre x et y , deux entiers , puis crée un caré qui 
    fabrique le  serpent'''
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_rectangle(Origine_snake_X1, Origine_snake_Y1, Origine_snake_X2, Origine_snake_Y2, fill="green" ,outline = 'white' )
   
def case_aleatoire():
    ''' cette fontion renvoie deux entier aleatoires en fonction de nombre_grille'''
    Aleatoire_X = randint(0, nombre_grille - 1)
    Aleatoire_Y = randint(0, nombre_grille - 1)
    return Aleatoire_X, Aleatoire_Y


def draw_snake(snake):
    '''pour chaque case dans snake récupère les coordonées et les rempli avec la fonction remplir_case'''
    for case in snake:
        x, y = case
        remplir_case(x, y)


def etre_dans_snake(case):
    ''' retourne une valeur 1 ou 0 en fonction de si la case est dans snake'''
    if case in SNAKE :
        EtreDedans = 1
    else:
        EtreDedans = 0

    return EtreDedans

def fruit_aleatoire():
    '''envoie un fruit aleatoires grace a la fonction case aleatoires et verifie que
        ce fruit n'est pas dans le serpent'''
    fruit_random = case_aleatoire()
    
    while (etre_dans_snake(fruit_random)):
        fruit_random = case_aleatoire

    return (fruit_random)

def dessine_fruit():
    '''crée un oval representant le fruit comme pour la fonction case '''
    global FRUIT
    while True : 
        try:
            x, y = FRUIT
            break
        except TypeError:
            FRUIT = fruit_aleatoire()
    
        
    Origine_snake_X1 = x * Largeur_Case
    Origine_snake_Y1 = y * Hauteur_Case
    Origine_snake_X2 = Origine_snake_X1 + Largeur_Case
    Origine_snake_Y2 = Origine_snake_Y1 + Hauteur_Case
    
    grille.create_oval( Origine_snake_X1, Origine_snake_Y1,  Origine_snake_X2, Origine_snake_Y2 , fill = "red",outline='white')
    
def gauche(event):
    '''definit un etat de gauche'''
    global MOUVEMENT
    if  MOUVEMENT == (1, 0) or MOUVEMENT == (-1, 0) :
        pass
    else:
        MOUVEMENT = (-1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def droite(event):
    '''definit un etat de droit'''
    global MOUVEMENT
    if  MOUVEMENT == (-1, 0) or MOUVEMENT == (1, 0): 
        pass
    else:
        MOUVEMENT = (1, 0)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def haut(event):
    '''definit un etat de haut'''
    global MOUVEMENT
    if  MOUVEMENT == (0, 1) or MOUVEMENT == (0, -1):
        pass
    else:
        MOUVEMENT = (0, -1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
def bas(event):
    '''definit un etat de bas'''
    global MOUVEMENT
    if  MOUVEMENT == (0, -1) or MOUVEMENT == (0, 1):
        pass
    else:
        MOUVEMENT = (0, 1)
        empty_channel3 = pygame.mixer.find_channel()
        empty_channel3.play(turn)
  
# lie les fonction de mouvement a des touche de clavier        
f.bind("<Left>", gauche)
f.bind("<Right>", droite)
f.bind("<Up>", haut)
f.bind("<Down>", bas)
f.bind("<q>", gauche)
f.bind("<d>", droite)
f.bind("<z>", haut)
f.bind("<s>", bas)

def serpent_mort(NouvelleTete):
    ''' verifie si le serpent est mort si oui PERDU = 1 sinon rien ne change'''
    global PERDU
    
    NouvelleTeteX, NouvelleTeteY = NouvelleTete
    
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= nombre_grille or NouvelleTeteY >= nombre_grille:
        PERDU = 1

def score_update():
    '''change le score affiché '''
    global SCORE

    SCORE += 100
    score.itemconfigure(texte,text = "score: " + str(SCORE) , font = ('Times', '15', 'bold '))
    
def mise_a_jour_snake():
    ''' mets a jour le serpent en prenant l'ancienneTete , le mouvement  et verfie si le serpent est mort 
    de plus si le serpent mange recrée un fruit et agrandit le serpent '''
    global SNAKE, FRUIT

    (AncienneTeteX, AncienneTeteY) = SNAKE[0]
    MouvementX, MouvementY = MOUVEMENT
    NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
    serpent_mort(NouvelleTete)
    SNAKE.insert(0, NouvelleTete)

    if NouvelleTete == FRUIT:
        
            FRUIT = fruit_aleatoire()
            score_update()
            eat = pygame.mixer.Sound("script_python/snake/_eat_.wav")
            empty_channel = pygame.mixer.find_channel()
            eat.set_volume(0.5)
            empty_channel.play(eat)
    else:
        SNAKE.pop()   
 
 
def boucle():
    '''mets a jours l'affichage et les event clavier , mets a jour le serpent , 
    si PERDU affiche le score finale et si le score finale est supérieur aux HIGHSCORE , 
    l'enregistre dans score.txt sinon le jeu continue''' 
    
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
         # cette fonction eteint la musqiue pour le game over
         #empty_channel4.stop()
        game_over = pygame.mixer.Sound("script_python/snake/mixkit-retro-game-over-1947.wav")
        empty_channel2 = pygame.mixer.find_channel()
        empty_channel2.play(game_over)
        sleep(2.5)
        f.quit()
    else:
        
        f.after(100, boucle)   

SCORE = 0

PERDU = 0

SNAKE = [case_aleatoire()]
FRUIT = fruit_aleatoire()

f.after(0, boucle()) 

  
f.mainloop()


