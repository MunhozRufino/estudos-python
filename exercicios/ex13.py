#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$'))
desc = float(input('Digite o valor de desconto:'))

total = salario + (salario * desc / 100)

print('O valor do salário é R${:.2f}, com o desconto aplicado de {:.1f}%, o valor passa a ser de R${:.2f} reais'.format(salario, desc, total))