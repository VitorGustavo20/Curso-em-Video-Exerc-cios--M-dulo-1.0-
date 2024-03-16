'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milímetros'''

metros = float(input('Digite um valor em metros (m): '))
cm = metros * 100
mm = metros * 1000

print(f'{metros}m corresponde à {cm}cm e {mm}mm')
