#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

tempo = int(input('Digite quantos anos tem o seu carro: '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro e velho!')
print('--FIM--')

#Condição simplificada
'''tempo = int(input('Digite quantos anos tem o seu carro: '))
print('Seu carro é novo' if tempo<=3 else'Seu carro é velho')
print('--FIM--')'''


n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2) /2
print('Sua média no semestre foi {:.1f}'.format(m))
if m <6:
    print('Você não pssou, precisa estudar!')
else:
    print('Parabéns, você passou!')

#Forma simplificada:
#print('Parabens' if m >=6 else 'Você não passou') 