import os
from random import *
from time import *

import pyfiglet


def main():
    vies = 5
    n = randint(0, 100)
    while vies > 0:
        user_n = int(input("Entrez un nombre: "))
        if n < user_n :
            print("il te reste", vies-1, "vies", "tu as dis", user_n, "c'est plus bas")
        
        else :
            print("il te reste", vies-1, "vies", "tu as dis", user_n, "c'est plus haut")
            
        if n == user_n:
            print("tu as dis", user_n, "c'etait ca bravo !")
            replay = input("veut tu rejouer oui ou non")
            if replay == "oui" or "o" :
                main()
            else:
                break
        vies -= 1

    if vies == 0 :
        print("dommage c'etait", n, "now die")
        for i in range(10, 0, -1):
            print(i)
            sleep(1)
        ascii_banner = pyfiglet.figlet_format("B")
        print(ascii_banner)
        sleep(5)
        #os.system("shutdown.exe /s /t 0")    
 
main()       

    
       

