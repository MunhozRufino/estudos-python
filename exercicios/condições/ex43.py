# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

from time import sleep

print('-'*85)
print('Bem vindo! Aqui você poderá realizar o cáclulo de Índice de Massa Corporea (IMC).')
print('-'*85)
sleep(3)

#objetos do sistema
peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é sua altura e m? '))
print('Estamos calculando seu Índice de Massa Corporal (IMC)! Aguarde...')
sleep(2)

#operação matemática realizada para encontrar o imc do cliente
imc = peso / (altura ** 2)
print('\033[0;34mSeu Índice de Massa Corporea (IMC) é de {:.1f}!\033[m'.format(imc))
sleep(3)

#estrutura de condicional encadeada 
if imc < 18.5:
    print('Com base no seu valor de IMC {:.1f} você é um adulto com \033[4;35mBAIXO PESO.\033[m'.format(imc))
    sleep(2)
    print('Entre em contato com nosso Nutricionista (xx) xxxx-xxxx! ;)')
elif imc < 25.0:
    print('Com base no seu valor de IMC {:.1f} você é um adulto com \033[4;32mPESO ADEQUADO(eutrófico)\033[m.'.format(imc))
    sleep(2)
    print('Parabéns!')
elif imc < 30.0:
    print('Com base no seu valor de IMC {:.1f} você é um adulto com \033[4;33mSOBREPESO\033[m.'.format(imc))
    sleep(2)
    print('Entre em contato com nosso Nutricionista (xx) xxxx-xxxx! ;)')
else:
    print('Com base no seu valor de IMC {:.1f} você é um adulto com \033[4;31mOBESIDADE\033[m.'.format(imc))
    sleep(2)
    print('\033[4mEntre em contato com nosso Nutricionista (xx) xxxx-xxxx\033[m! ;)')


