def div_euclidienne(a, b):
    '''revoie le reste et le quotien par rapport aux deux entree entier positif '''
    q = 0
    r = a
    while r >= b:
        #invariant : r >= 0
        #invarient : a = b*q*r
        q += 1
        r  -= b
    return q,r

print(div_euclidienne(73,27))

#n = help(div_euclidienne)

#print(n)