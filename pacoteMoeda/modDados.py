from pacoteMoeda import modMoeda

def resumo(n,x = 0, y = 0):
    if (x == 0 and y == 0):
        print('-----------------')
        print('Resumo do valor')
        print('-----------------')
        print('Preço analisado: {}'.format(n))
        print('Dobro do preço: {}'.format(modMoeda.dobrar(n)))
        print('Metade do preço: {}'.format(modMoeda.metade(n)))

    elif (x !=0 and y == 0):
        print('-----------------')
        print('Resumo do valor')
        print('-----------------')
        print('Preço analisado: {}'.format(n))
        print('Dobro do preço: {}'.format(modMoeda.dobrar(n)))
        print('Metade do preço: {}'.format(modMoeda.metade(n)))
        print('{}% de aumento: {}'.format(x, modMoeda.aumentar(n,x)))

    elif (x == 0 and y != 0):
        print('-----------------')
        print('Resumo do valor')
        print('-----------------')
        print('Preço analisado: {}'.format(n))
        print('Dobro do preço: {}'.format(modMoeda.dobrar(n)))
        print('Metade do preço: {}'.format(modMoeda.metade(n)))
        print('{}% de redução: {}'.format(y, modMoeda.diminuir(n,y)))

    elif (x !=0 and y != 0):
        print('-----------------')
        print('Resumo do valor')
        print('-----------------')
        print('Preço analisado: {}'.format(n))
        print('Dobro do preço: {}'.format(modMoeda.dobrar(n)))
        print('Metade do preço: {}'.format(modMoeda.metade(n)))
        print('{}% de aumento: {}'.format(x, modMoeda.aumentar(n,x)))
        print('{}% de redução: {}'.format(y, modMoeda.diminuir(n,y)))
    