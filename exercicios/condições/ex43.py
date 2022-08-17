# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
from time import sleep

peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é sua altura? '))
print ('''Qual a sua faixa de idade?
[1] Adolescente
[2] Adulto
[3] Idoso
[4] Gestante''')
opcao = int(input('Sua opção: '))
imc = peso / (altura ** 2)
print('Seu índice de massa corporea é {:.1f}'.format(imc))

if opcao == 1:
    print('\033[1;31mPara crianças e adolescentes (de 6 a 15 anos) os dados são calculados com base em uma tabela específica. Digite sua idade:\033[m')
    sleep(4)
    idade = int(input('Qual a sua idade? '))
    
    if idade == 6:
        if imc >= 14.5 and imc < 16.6:
            print('Você é um adolescente com peso NORMAL!')
        elif imc > 16.6:
            print('Você é um adolescente com SOBREPESO!')



elif opcao == 2:
    if imc < 18.5:
        print('Você é um adulto abaixo do peso!')

elif opcao == 3:
    if imc < 18.5:
        print('Você é um adulto abaixo do peso!')

elif opcao == 3:
    if imc < 18.5:
        print('Você é um adulto abaixo do peso!')