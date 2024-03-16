'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida.

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

primeira = float(input('Primeira nota = '))
segunda = float(input('Segunda nota = '))
média = ( primeira + segunda ) / 2

print(f'A sua média é de {média:.1f}.')
if média < 5.0:
    print('Você foi REPROVADO! Estude mais.')
elif 5.0 < média < 7.0:
    print('Você está em RECUPERAÇÃO. Você está quase lá.')
else:
    print('PARABÉNS! Você foi APROVADO.')
print('Bons estudos!!!')