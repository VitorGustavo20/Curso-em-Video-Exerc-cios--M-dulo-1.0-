'''Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
média = ( primeira + segunda ) / 2

print(f'As notas do alunos são respectivamente {primeira:.1f} e {segunda:.1f}, tendo uma média de {média:.1f}')