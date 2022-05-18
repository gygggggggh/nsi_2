# tri par selection 

def position(t,i):
    for k in range(i,0,-1):
        if t[k-1]<t[i]:
            return k
    return 0

def insert(t,k,i):
    v = t[i]
    for j in range(i,k,-1):
        t[j] = t[j-1]
    t[k]=v

def tri_insert(t):
    ''' tri le tableau  t dans l'ordre croissant 
        t est un tanbleu d'entier non vide '''
    for i in range(len(t)):
        #invariant de boucle : t[:1] est tiré 
        k = position(t,i)
        insert(t,k,i)
        
t = [6,9,1,0]
print(t)
tri_insert(t)
print(t)


def inserer_val (t , i ) :
    v = t[i]
    j = i
while j > 0 and t [j -1] > v :
    t[j] = t[j-1]
    j = j - 1
    t[j] = v
def tri_insertion2 ( t ) :
    for i in range (1 , len ( t ) ) :
        inserer_val (t , i )
        print(v)