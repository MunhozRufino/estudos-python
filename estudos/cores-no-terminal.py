#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

print('\033[1;33mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os número são \033[1;34m{}\033[m e \033[4;32m{}\033[m!!!'.format(a, b))

nome = 'Munhoz'
print('Olá, tudo bem {}{}{}!!!!'.format('\033[1;36m', nome,'\033[m'))

n = 19//2
c = 19 % 2
print('{}{}'.format(n, c))