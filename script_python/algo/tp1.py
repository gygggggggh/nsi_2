from random import randint

def gen_tab (n,a,b,):
    t = []
    for i in range(n):
        t.append(randint(a,b))
    return t    
t = gen_tab(5,1,100)
print(t)

def min_tab (t):
    mini = t[0]
    for i in t[1:]:
        if mini > i :
           mini = i
    return mini
        
print(min_tab(t))



def indice_min_tab(t):
    '''renvoie un indice du miniuim du tableau t 
    t est un tableu non vide d'entiers '''
    imin = 0
    for i in range(1,len(t)):
        # imin est un miniuim de 
        if t[i] < t[imin] :
           imin = i
    return imin


print(indice_min_tab(t))


