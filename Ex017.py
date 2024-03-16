'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto Adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa desse triângulo é: {hipotenusa:.2f}')