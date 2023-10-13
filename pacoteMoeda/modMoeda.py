def dobrar (n,show = False):
    if (show == True):
        return 'R${}'.format(n * 2)
    
    else:
        return n * 2

def metade (n,show = False):
    if (show == True):
        return 'R${}'.format(n / 2)
    
    else:
        return n / 2

def aumentar(n, pcnt, show = False):
    pcnt = pcnt * 0.01

    if (show == True):
        return 'R${}'.format(n + n * pcnt)
    
    else:
        return n + n * pcnt

def diminuir(n, pcnt, show = False):
    pcnt = pcnt * 0.01

    if (show == True):
        return 'R${}'.format(n - n * pcnt)
    
    else:
        return n - n * pcnt

def moeda(n):
    return ('R${}'.format(n))
