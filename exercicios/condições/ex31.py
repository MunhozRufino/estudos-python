#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep

viagem = float(input('Digite a distância da viagem: '))
print('Você esta prestes a começar sua viagem...')
sleep(2)
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('O custo da sua passagem será de R${:.2f}'.format(preço))

#Forma simplificada
#preço = distância * 0.50 if distância <= 200 else distância * 0.45