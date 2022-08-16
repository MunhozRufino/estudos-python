#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
casa = float(input('Qual o valor do imóvel: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você quer pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa no valor de \033[1;33mR${:.2f}\033[m em \033[1;33m{}\033[m anos'.format(casa, anos), end='')
print(' a prestação será de \033[4;32mR${:.2f}\033[m.'.format(prestacao))
if prestacao <= minimo:
    print('Com base no seu salário \033[1;33mR${}\033[m o limite máximo para parcela será de \033[1;33mR${}\033[m.'.format(salario, minimo))
    sleep(2)
    print('\033[1;34mEmprestimo concedido!\033[m')
else:
    print('Com base no seu salário \033[1;33mR${}\033[m o limite máximo para parcela será de \033[1;33mR${}\033[m.'.format(salario, minimo))
    sleep(2)
    print('\033[1;31mEmprestimo negado!\033[m')