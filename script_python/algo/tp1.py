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


def comparer_dico(d1,d2):
    if len(d1) != len(d2):
        return False
    else:
        for cle , val in d1.items():
            if cle not in d2:
                return False
            else:
                if d2[cle] != val :
                    return False
    return True

d1 = {1:2,2:3,4:2}
d2 = {3:2,4:3,5:1}
d3 = {3:3,9:4,1:2}

def compare_table(t1,t2):
    d1 = convert_tab_to_dico(t1)
    d2 = convert_tab_to_dico(t2)
    return comparer_dico(d1,d2)

t1 = [1,2,3,4]
t2 = [2,1,3,4]

