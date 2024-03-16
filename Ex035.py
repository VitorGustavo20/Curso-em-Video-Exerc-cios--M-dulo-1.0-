'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo.'''

r1 = float(input('Segmento 01: '))
r2 = float(input('Segmento 02: '))
r3 = float(input('Segmento 03: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')