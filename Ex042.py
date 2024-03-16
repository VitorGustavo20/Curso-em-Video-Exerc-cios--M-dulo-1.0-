'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = float(input('Segmento 01: '))
r2 = float(input('Segmento 02: '))
r3 = float(input('Segmento 03: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo.')
    if r1 == r2 == r3:
        print('Será formado um triângulo EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Será formado um triângulo ISÓSCELES')
    else:
        print('Será formado um triângulo ESCALENO')
else:
    print('Não é possível formar um triângulo.')

