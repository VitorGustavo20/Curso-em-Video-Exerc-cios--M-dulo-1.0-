'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

num = int(input('Digite um número: '))

print('''AS OPÇÕES SÃO:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL 

''')

opção = int(input('ESCOLHA UMA DAS OPÇÕES PARA REALIZAR A CONVERSÃO DO NÚMERO: '))

if opção == 1:
    print(f'O número {num} em binário é: {bin(num) [2:]}')
elif opção == 2:
    print(f'O número {num} em octal é: {oct(num) [2:]}')
elif opção == 3:
    print(f'O número {num} em hexadecimal é: {hex(num) [2:]}')
else:
    print(f'Opção inválida! Tente novamente.')