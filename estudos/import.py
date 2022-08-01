
import emoji
print(emoji.emojize('Olá Mundo! 🌍')) #aplicação com o proprio emoji
print(emoji.emojize('Olá Mundo! :globo_mostrando_as_américas:', language='pt')) #aplicação sem emoji com tradução.

#print(emoji.demojize("Python é 🌍", language='pt')) função demojize utilizada para identificar o nome do emoji
#import global funciona desta forma: import math

import math # Forma 1: importação total - Forma 2: from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))