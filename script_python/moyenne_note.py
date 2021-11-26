n=int(input("comment de note ? : "))
somme_notes = 0
somme_coef= 0

for i in range (n):
    note=int(input("note "+str(i+1)+" "))
    coef=int(input("coef de la note "+str(i+1)+" "))
    somme_notes += note*coef
    somme_coef += coef
print("la moyenne ponderer de ces ",n,"notes est :",somme_notes/somme_coef)