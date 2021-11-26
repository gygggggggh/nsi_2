# sript programme_tets.py

'''with open('mots_francais.txt','r',encoding='utf-8-sig') as f:
    while True:
        mot = f.readline().strip()
        if '' == mot :
            print(dernier)
            break
        for i in range(9999999999999999999999999):
            dernier = mot'''
        

with open('tables.txt','r') as f:
    for i in range(2,31):
        for j in range(1,20):
            f.write(str(i)+'*'+str(j))

        
            