'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Digite o nome de sua cidade: ')).strip()

if cidade.upper().split()[0] in 'SANTO':
    print('A cidade começa com "Santo".')
else:
    print('A cidade não começa com "Santo".')