#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos Km foram percorridos:'))
dia = int(input('Digite quantos dias de aluguel:'))

#carro = 60
#preco = 0.15

#custo = carro * dia
#trajeto = km * preco

pago = (dia * 60) + (km * 0.15)


print('Você alugou o carro por {} dia(s) percorrendo {:.1f}km, o valor total a ser pago será de R${:.2f}'.format(dia, km, pago))