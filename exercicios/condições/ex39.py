#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento: '))
idade = atual - ano
print('O governo federal esta acessando seus dados...')
sleep(2)
print('\033[1;33mA sua idade atual é de {} anos!\033[m'.format(idade))
sleep(2)

if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('\033[1;33mVocê não esta no período de alistamento militar\033[m')
    print('\033[1;33mVocê deve se alistar daqui {} anos!\033[m'.format(saldo))
    print('\033[1;32mSeu alistamento será no ano de {}!\033[m'.format(ano))
elif idade == 18:
    print('\033[1;32mVocê deve comparecer a junta militar mais próxima!\033[m')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('\033[1;31mDeve comparecer com urgência à junta militar mais próxima!\033[m')
    print('\033[1;31mVocê deveria ter se alistado à {} anos atrás.\033[m'.format(saldo))
    print('\033[1;33mSeu alistamento ocorreu em {}!\033[m'.format(ano))


