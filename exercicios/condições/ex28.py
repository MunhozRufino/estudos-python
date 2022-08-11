#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input('Digite um número que esta pensando: '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('Você Ganhou! Estava pensando nisso!')
else:
    print('Eu ganhei! Você pensou no número {} e eu pensei no número {}'.format(jogador, computador))