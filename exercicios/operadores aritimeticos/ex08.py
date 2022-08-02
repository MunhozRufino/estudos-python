#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros:'))

c = n * 100
m = n * 1000

print('{}m equivale a {:.0f}cm e {:.0f}mm.'.format(n, c, m))