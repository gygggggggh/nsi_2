from random import randint


sens = randint(1, 4)


def bateau():
    xB = randint (2, 4)
    yB = randint (2, 4)
    case1 = xB, yB
    if sens == 1 :
        case2 = xB+1, yB
    if sens == 2 :
        case2 = xB-1, yB
    if sens == 3 :
        case2 = xB, yB+1
    if sens == 4 :
        case2 = xB, yB-1
    if sens == 1 :
        case3 = xB+1, yB
    if sens == 2 :
        case3 = xB-1, yB
    if sens == 3 :
        case3 = xB, yB+1
    if sens == 4 :
        case3 = xB, yB-1
    bat = case1 , case2 , case3
    return bat




# ####################################################################
'''LE  CODE  PRINCIPAL  '''
# ####################################################################

for i in range (100):
    bat = bateau()
    print(bat)













