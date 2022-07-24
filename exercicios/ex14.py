#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura atual em °C:'))
f = ((9*c) / 5) + 32
#devido a ordem de precedência o calculo acima poderia ser feito assim: f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))