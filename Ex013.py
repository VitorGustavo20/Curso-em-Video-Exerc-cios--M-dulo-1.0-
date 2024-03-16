'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.'''

salário = float(input('Quanto é o seu salário? R$'))
aumento = salário + ( salário * 0.15 )

print(f'O seu salário de R${salário:.2f}, após um aumento de 15%, passou a ser R${aumento:.2f}')