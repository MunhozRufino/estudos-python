# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-='*20)
print('Analisador de triângulos')
print('-='*20)

r1 = float(input('Digite o primeiro comprimento da linha: '))
r2 = float(input('Digite o segundo comprimento da linha: '))
r3 = float(input('Digite o terceiro comprimento da linha: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIÂNGULO!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')