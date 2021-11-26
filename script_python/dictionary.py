dico = {}
for i in range(26):
    dico[chr(i+65)] = i
    
table_codage = {}
for lettre in dico:
    nombre = (dico[lettre]+7)%26
    lettre_codee = ''
    for cle in dico :
        if dico[cle] == nombre:
             lettre_codee = cle
table_codage[lettre] = lettre_codee
    
    



