#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite a largura da sua parede:'))
alt = float(input('Digite a altura da sua parede:'))

area = larg * alt

print('Sua parede tem a dimensão de {}m x {}m e sua area é de {}m'.format(larg, alt, area))

tinta = area / 2

print('Para pintar sua parede você precisará de {}L de tinta'.format(tinta))
