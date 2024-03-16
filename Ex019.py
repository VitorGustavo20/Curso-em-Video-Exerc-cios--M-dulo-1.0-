'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''

from random import choice

aluno_01 = input('Primeir aluno: ')
aluno_02 = input('Segundo aluno: ')
aluno_03 = input('Terceiro aluno: ')
aluno_04 = input('Quarto aluno: ')
alunos = (aluno_01, aluno_02, aluno_03, aluno_04)
sorteio = choice(alunos)
print(f'O aluno sorteado foi {sorteio}')