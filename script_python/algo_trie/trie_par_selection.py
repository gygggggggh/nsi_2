#tp  algo de trie par selection 

def indice_min(t,i):
    
    m = i 
    for j in range(i+1,len(t)):
        if t[j] < t[m]:
            m = j
    return m

def echanger(t,i,j):
    t[i] , t[j] = t[j], t[i]
    

def trie_selection(t):
    '''elle trie le tableux dans l'ordre crossant 
    t est un tableux non vide d'entiers'''
    for i in range(len(t)-1):
        m = indice_min(t,i)
        echanger(t,i,m)
        
t = [10,32,64,128,256 ,128,4,0]

trie_selection(t)
print(t)


