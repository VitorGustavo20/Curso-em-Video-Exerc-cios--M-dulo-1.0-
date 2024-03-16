'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite seu nome completo: ')).strip()

if 'SILVA' in nome.upper():
    print('Você tem "Silva" no nome.')
else:
    print('Você não tem "Silva" no nome.')