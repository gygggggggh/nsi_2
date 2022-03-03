
from random import randint, shuffle
from time import *
import matplotlib.pyplot as plt


# création des tableaux
taille = 1000
donnees_random = []
donnees_triees = []
donnees_inversees = []
axis = []

for i in range(8):
    tab_random = []
    tab_trie = []
    tab_inverse = []
    for j in range(taille*2*(i+1)):
        tab_trie.append(j)
        tab_random.append(j) 
        tab_inverse.append(taille*2*(i+1)-1-j)
    shuffle(tab_random) 
    donnees_random.append(tab_random)
    donnees_triees.append(tab_trie)
    donnees_inversees.append(tab_inverse)
    axis.append(taille*2*(i+1))


def executer_fonction(fonction,color,nom):
    plot_random = []
    plot_triees = []
    plot_inversees = []
    for i in range(len(donnees_random)):
        debut = perf_counter()
        fonction(donnees_random[i])
        fin = perf_counter()
        duree = fin-debut
        plot_random.append(duree)
        print('taille : '+str(taille*2*(i+1))+' => temps : '+str(duree))

        debut = perf_counter()
        fonction(donnees_triees[i])
        fin = perf_counter()
        duree = fin-debut
        plot_triees.append(duree)

        debut = perf_counter()
        fonction(donnees_inversees[i])
        fin = perf_counter()
        duree = fin-debut
        plot_inversees.append(duree)
        
    plt.plot(axis,plot_random,'-'+color,label=nom+' (random)')
    plt.plot(axis,plot_triees,'--'+color,label=nom+' (triées)')
    plt.plot(axis,plot_inversees,':'+color,label=nom+' (inversées)')


# ========================================================================================
# Recherche du minimum
def element_min(tab) :
    m = tab[0]
    for i in range(1,len(tab)):
        if tab[i] < m :
            m = tab[i]
    return m

#cexecuter_fonction(element_min,'r','Recherche du min')

# ===================================
# tri_selection

def tri_selection (tab) :
    for i in range(0,len(tab)-1) :    # de 0 à n-2
        indmin = i
        for j in range(i+1,len(tab)) : # de i+1 à n-1, recherche du min
            if tab[j] < tab[indmin] : indmin = j
        tab[indmin],tab[i]=tab[i],tab[indmin]  # echange de valeurs entre indmin et i

#executer_fonction(tri_selection,'g','Tri par sélection')



# ========================================================================================
# Tri par insertion
def tri_insertion(tab) :
    for j in range(1,len(tab)) :
        elt_a_placer = tab[j]
        i = j-1
        while i >= 0 and tab[i] > elt_a_placer :
            tab[i+1] = tab[i]
            i = i-1
        tab[i+1] = elt_a_placer

#executer_fonction(tri_insertion,'b','Tri par insertion')


# ===================================
# Tri bulle
def tri_bulle (tab):
    i = len(tab)-1
    while i >= 1:
        for j in range(i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
        i = i-1

#executer_fonction(tri_bulle,'r','Tri bulle')


# ========================================================================================

# Tri fusion (fonction récursive ... programme terminale)
def fusion(gauche, droite):
    igauche, idroite = 0,0
    result = []
    while igauche < len(gauche) and idroite < len(droite):
        if gauche[igauche] < droite[idroite]:
            result.append(gauche[igauche])
            igauche += 1
        else:
            result.append(droite[idroite])
            idroite += 1
    result += gauche[igauche:]
    result += droite[idroite:]
    return result

def triFusion (tab):
    if len(tab) <= 1 :
        return tab
    milieu = len(tab) // 2
    gauche = triFusion(tab[:milieu])
    droite = triFusion(tab[milieu:])
    return fusion(gauche,droite)

#executer_fonction(triFusion,'k','Tri fusion')


# ========================================================================================
#plt.yscale('log')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()








    
