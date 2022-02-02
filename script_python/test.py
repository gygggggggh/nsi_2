def compare_tab(t1, t2):
    if len(t1) != len(t2):
        return False
    t1.sort()
    t2.sort()
    for i in range(len(t1)):
        if t1[i] != t2[i] :
            return False
    return True

 