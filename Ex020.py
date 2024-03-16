'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

from random import shuffle

aluno_01 = input('Primeir aluno: ')
aluno_02 = input('Segundo aluno: ')
aluno_03 = input('Terceiro aluno: ')
aluno_04 = input('Quarto aluno: ')
alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
shuffle(alunos)

print(f'A ordem sorteada foi: {alunos}')