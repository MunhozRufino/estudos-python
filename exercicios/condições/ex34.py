#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário atual: '))
if salario >= 1250: 
    aumento = (salario * 10) / 100 + salario
    print('Seu segundo aumento de salário será de R${:.2f} reais.'.format(aumento))
else:
    aumento = (salario * 15) / 100 + salario
    print('Seu primeiro aumento de salário será de R${:.2f} reais.'.format(aumento))