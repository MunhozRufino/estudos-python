#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# SEM A UTILIZAÇÃO DO IMPORT
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))''' 

# COM A UTILIZAÇÃO DO IMPORT 
import math # from math import hypot - Obs: Formas de fazer.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) #hi = hypot(co, ca) - Obs: Formas de fazer.
print('A hipotenusa vai medir {:.2f}'.format(hi))

