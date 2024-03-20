'''A Confederação Nacional de Natação precisa de um programa que leia o nascimento de um atleta e mostre sua categoria,
de acordo com a idade.

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date
ano = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano

print(f'Você tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')