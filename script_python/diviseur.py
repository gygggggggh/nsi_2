#script diviseur.py

n=int(input("choisissez un entier :"))
print("les diviseurs de",n,"sont")
for i in range(1,n+1):
     if n%i == 0 :
        print(i,end=" ")

        