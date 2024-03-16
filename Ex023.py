'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos
separados.
Ex: Digite um número: 1834
 unidade: 4  dezena: 3 centena:8 milhar:1'''

número = int(input('Digite um número de 0 à 9999: '))

unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10

print(f'Unidade = {unidade}')
print(f'Dezena = {dezena}')
print(f'Centena = {centena}')
print(f'Milhar = {milhar}')
