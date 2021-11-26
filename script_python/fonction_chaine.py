def longueur(ch):
    l=0
    for lettre in ch :
        l += 1
    return l

def position(c,ch) :
    pos = -1
    for lettre in ch :
        pos += 1 
        if lettre == c :
            return pos
        print("pas de",c,"dans la chaine : ",ch)

def espace(ch):
    new_ch = ""
    for lettre in ch :
        new_ch

def inverse(ch):
    new_ch =""
    for lettre in ch :
        new_ch = lettre + new_ch
    return(new_ch)

def palindrome(ch):
    ch_inv = inverse(ch)
    if ch_inv ==ch :
        return True
    else:
        return False

def palindrome2(ch):
    return  inverse (ch)

def voyelle (c):
    ch_voyelles = "aàâeéèêiîuûoôy"
    return c in ch_voyelles

def nb_voyelle(ch):
    compteur = 0
    for lettre in ch :
        if voyelle(lettre):
            compteur += 1
    return compteur

print(inverse('11       12      13      14      15      21      22      23      24      25      31      32      33      34      35      41      42      43      44      45      51      52      53      54      55'))
               