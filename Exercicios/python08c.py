import random

aluno1 = str (input ('Insira o nome do primeiro aluno'))
aluno2 = str (input ('Insira o nome do segundo aluno'))
aluno3 = str (input ('Insira o nome do terceiro aluno'))
aluno4 = str (input ('Insira o nome do quarto aluno'))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.sample(lista, k =4)
print('A ordem é = {}'.format(sorteado))



