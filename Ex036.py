'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o seu salário? R$'))
anos = int(input('Quantos anos será dividida a prestação? '))
mensal = anos * 12
prestação = casa / mensal

if prestação < 0.30 * salário:
    print(f'PARABÉNS! O seu empréstimo foi aprovado. Você pode realizar a compra da sua casa de R${casa:.2f}, pagando uma'
          f'prestação mensal de R${casa / mensal:.2f}, durante {mensal} meses')
else:
    print(f'Sinto muito! Mas seu empréstimo foi reprovado.')
print('FIM DO PROGRAMA')