#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from calendar import c
import string


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digie o terceiro número: '))

menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c 
print('O menor número digitado foi {}.'.format(menor))

maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 
print('O menor número digitado foi {}.'.format(maior))


