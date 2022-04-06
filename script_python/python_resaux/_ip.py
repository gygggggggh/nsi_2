from re import M


def zero_a_droite(n):
    return n & 992 #  = 00000

#print(zero_a_droite(0b111001001))

def zero_a_gauche(n):
    return n & 31 # = 11111

#print(zero_a_gauche(0b111001001))

def convIP_to_int(ipstr):
    liste  = ipstr.split('.')
    s = 0 
    for i in range(4):
        nb = int(liste[i]) <<8 *(3-i)
        s += nb
    return s


#print(convIP_to_int("115.250.207.0"))

def convIP_to_str(ipint):
    chaine = ''
    for i in range(4):
        octet = ipint >> (8*(3-i))
        octet = octet & 255
        chaine += str(octet) + '.'
    chaine  = chaine[:-1]
    return chaine

#print(convIP_to_str(1945816832))

def adresse_reseaux(ipstr,masquestr):
    ip =  convIP_to_int(ipstr)
    masque =  convIP_to_int(masquestr)
    return convIP_to_str(ip & masque)

print(adresse_reseaux( "90.98.100.3 "," 255.255.255.128 " ))


def nb_adresses(masque_str):
    m = convIP_to_int(masque_str)
    nb = 0
    while m & x != 0 :
         nb += 1
         x = x >>1
    nb_ad  = 2 ** (32-nb)

def adresse_broadcast(ipstr,m_str):
    ip =  convIP_to_int(ipstr)
    m = convIP_to_int(m_str)
    ad_res =  ip & m 
    comp = 2**32-1-m
    ad_broadcast = ad_res |comp
    return convIP_to_int(ad_broadcast)