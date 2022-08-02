numero = int(input('Digite um número:'))
n = numero * 2
s = numero * 3 
p = numero ** (1/2)

#print('O dobro do número é {},\n o tripulo do número é {},\n e a raiz quadrada do número é {}'.format(n, s, p))

print('O dobro de {} é {}.'.format(numero, (numero*2)))
print('O tripulo de {} é {}.'.format(numero, (numero*3)))
print('A raiz quadrada de {} é {:.2f}.'.format(numero, (numero**(1/2))))