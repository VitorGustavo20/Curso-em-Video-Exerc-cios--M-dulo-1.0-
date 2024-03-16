'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Quando foi seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano

print(f'Então você tem {idade} anos.')
if idade < 18:
    print('Ainda não está na hora de se alistar.')
    print(f'Falta {18 - idade} anos para o alistamento.')
elif idade > 18:
    print('Você já passou do prazo de alistamento.')
    print(f'Você está {idade - 18} anos atrasado.')
else:
    print('Já é hora de se alistar.')