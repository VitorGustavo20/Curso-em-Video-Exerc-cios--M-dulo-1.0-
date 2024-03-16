'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta
uma área de 2m²'''

largura = float(input('Tamanho da largura: '))
altura = float(input('Tamanho da altura: '))
área = largura * altura
tinta = área / 2

print(f'Uma parede que mede uma dimensão de {largura:.2f}x{altura:.2f}, tem uma área total de {área:.2f}m²')
print(f'Será necessário {tinta:.2f}l de tinta para pinta-la totalmente.')