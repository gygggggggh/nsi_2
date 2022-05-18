

def money(n,s):
    """_summary_
    la fonction renvoie la solution gloutone sous la forme d'un tableau

    Args:
        n (int): est un montant entier
        s (liste): est un sisteme de monnaie
    """
    tab = []
    n = len(s)
    for p in range(n-1, -1, -1):
        