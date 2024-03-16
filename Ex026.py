'''Faça um programa que leia uma frase pelo teclado e mostre:

A) Quantas vezes aparece a letra "A".
B) Em que posição ela aparece a primeira vez.
C) Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()


print(f'A letra "A" aparece {frase.count('A')} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find('A') + 1}°')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind('A') + 1}')