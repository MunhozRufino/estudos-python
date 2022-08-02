#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

m = float(input('Digite sua primeira nota:'))
p = float(input('Digite sua segunda nota:'))

#s = m + p 
#x = s / 2 

#print('Sua média é {:.1f}'.format(x))

s = (m + p) / 2

print('A sua media entre as notas {:.1f} e {:.1f} é {:.1f}'.format(m, p, s))