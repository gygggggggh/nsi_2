from random import randint
from time import *

def gen_tab_alea(n, a, b):
    t = []
    for i in range(n):
        t.append(randint(a, b))
    t.sort()
    return t


def recherche_dichotomique(t,v):
    g = 0
    d = len(t)-1
    i = 0
    while g <= d :
        i +=1
        m = (d+g)//2
        if t[m] > v:
            d=m-1
        elif t[m] < v:
            g=m+1
        else:
            return m,i

    return None,i

            

t = gen_tab_alea(100, 0, 1)
g = [0]*1000000

for i in range(10**10c):
    print(recherche_dichotomique(g,1))