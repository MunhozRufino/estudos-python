# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from time import sleep
from datetime import date
data = date.today().year
nascimento = int(input('Digite sua data de nascimento: '))
idade = data - nascimento
if idade <= 9:
    print('Com base na sua idade de {} anos, sua catégoria é MIRIM!'.format(idade))
    categoria = 9 - idade
    print('Daqui {} anos você irá para categoria INFANTIL!'.format(categoria))
elif idade > 9 and idade <= 14:
    print('Com base na sua idade de {} anos, sua catégoria é INFANTIL'.format(idade))
    categoria = 14 - idade
    print('Daqui {} você irá para categoria JÚNIOR!'.format(categoria))
elif idade > 14 and idade <= 19:
    print('Com base na sua idade de {} anos, sua categoria é JUNIOR!'.format(idade))
    categoria = 19 - idade
    print('Daqui {} você irá para categoria SÊNIOR!'.format(categoria))
elif idade > 19 and idade <= 25:
    print('Com base na sua idade de {} anos, sua categoria é SÊNIOR!'.format(idade))
    categoria = 25 - idade
    print('Daqui {} você irá para categoria MASTER!'.format(categoria))
elif idade >= 25:
    print('Com base na sua idade de {} anos, sua categoria é MASTER!'.format(idade))
    print('Parabéns você é um exemplo de atleta!')

