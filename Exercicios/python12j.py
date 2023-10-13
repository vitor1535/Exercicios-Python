import random
import math

num = int (input ('Escolha uma opção! 1 - Pedra / 2 - Papel / 3 - Tesoura'))
if (num == 1):
    escolhaHumano = 'pedra'
elif (num == 2):
    escolhaHumano = 'papel'
elif (num == 3):
    escolhaHumano = 'tesoura'

escolhaMaquina = random.choice(['pedra','papel','tesoura'])

if (escolhaHumano == 'pedra'):
    if (escolhaMaquina == 'pedra'):
        print('Empate! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'papel'):
        print('Derrota! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'tesoura'):
        print('Vitória! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))

elif (escolhaHumano == 'papel'):
    if (escolhaMaquina == 'pedra'):
        print('Vitória! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'papel'):
        print('Empate! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'tesoura'):
        print('Derrota! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))

elif (escolhaHumano == 'tesoura'):
    if (escolhaMaquina == 'pedra'):
        print('Derrota! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'papel'):
        print('Vitória! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))
    elif (escolhaMaquina == 'tesoura'):
        print('Empate! Humano - {} x {} - Máquina'.format(escolhaHumano, escolhaMaquina))