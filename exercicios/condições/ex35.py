#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de triângulos')
print('-='*20)

r1 = float(input('Digite o primeiro comprimento da linha: '))
r2 = float(input('Digite o segundo comprimento da linha: '))
r3 = float(input('Digite o terceiro comprimento da linha: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')