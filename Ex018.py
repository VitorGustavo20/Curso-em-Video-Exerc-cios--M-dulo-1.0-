'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.'''

from math import radians, tan, cos, sin

ângulo = float(input('Digite um ângulo: '))
ang = radians(ângulo)
seno = sin(ang)
tangente = tan(ang)
cosseno = cos(ang)

print(f'seno = {seno:.2f}')
print(f'cosseno = {cosseno:.2f}')
print(f'tangente = {tangente:.2f}')