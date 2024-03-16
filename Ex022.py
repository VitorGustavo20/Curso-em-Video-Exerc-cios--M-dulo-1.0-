'''Crie um programa que leia o nome completo de uma pessoa e mostre:

 A) O nome com todas as letras maiúsculas e minúsculas.
 B) Quantas letras ao todo (sem considerar espaços).
 C) Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()

print(f'A) Maiúsculas = {nome.upper()} \nMinúsculas = {nome.lower()}')
print(f'B) O seu nome possui {len(nome) - nome.count(' ')} letras no total')
print(f'C) O seu primeiro nome tem {len(nome.split()[0])} letras')