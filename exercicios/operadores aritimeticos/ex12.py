#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$'))
desc = float(input('Digite o valor de desconto:'))

total = preço - (preço * desc / 100)

print('O valor do produto é R${:.2f}, com o desconto aplicado de {:.1f}%, o valor passa a ser de R${:.2f}'.format(preço, desc, total))