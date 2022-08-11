#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do caro: '))
multa = (velocidade-80) * 7
if velocidade <= 80:
    print('Você esta dentro do limite de velocidade estipulado.')
else:
    print('Sua velocidade de {}km/h está acimada da permitida, sua multa será de R${:.2f} reais.'.format(velocidade, multa))