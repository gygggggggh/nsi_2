# sript programme_tets.py
'''with open('mots_francais.txt','r',encoding='utf-8-sig') as f:
    while True:
        mot = f.readline().strip()
        if '' == mot :
            print(dernier)
            break
        for i in range(9999999999999999999999999):
            dernier = mot'''
        

'''with open('tables.txt','w') as f:
    for i in range(2,31):
        f.write(f'table de {str(i)} \n')
        for j in range(1,21):
            f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\n')'''
#11
'''with open ('journal.txt','a',) as f:
    chaine = "nimporte quoi"
    while chaine !=  '':
        chaine = input('>> ')
        f.write(f'{chaine} \n')'''

#12

def isFile(filename):
    try:
        with open (filename,'r') as f:
            return True
    except IOError:
          return False
#

#13

def show_file(filename):
    if isFile(filename):
        with open(filename,'r',encoding='utf-8') as f:
            for ligne in f:
                print(ligne.strip())
    else:
        print('ce fichier est pas dans cette realité')



def copy_file(filename,copy_file):
    if isFile(filename):
        with open(filename,'r') as original , open(copy_file,'w') as copy_file:
            for ligne in original :
                copy_file.write(ligne)
copy_file('/home/dylans/Bureau/porge.txt','porche.txt')