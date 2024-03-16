'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
a sua porção inteira.'''

#num = float(input('Digite um número: '))
#print(f'A porção inteira do número {num} é: {int(num)}')

from math import trunc

num = float(input('Digite um número: '))

print(f'O número {num} possui como sua porção inteira: {trunc(num)}')