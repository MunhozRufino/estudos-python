#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('\033[1;32mDigite o primeiro numero: \033[m'))
n2 = int(input('\033[1;32mDigite o segundo número: \033[m'))

if n1 > n2:
    print('O primeiro número é o maior!')
elif n2 > n1:
    print('O segundo número é o maior!')
else:
    print('\033[1;4;31mOs dois números são iguais!\033[m')