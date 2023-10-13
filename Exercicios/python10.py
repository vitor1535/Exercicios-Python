import random

numeroAleatorio = random.randrange(6)

chute = (int (input ('Chute um numero entre 0 e 5')))

if (chute == numeroAleatorio):
    print('Voce acertou! O numero era {}'.format(numeroAleatorio))
else:
    print('Voce errou! O numero era {}'.format(numeroAleatorio))






