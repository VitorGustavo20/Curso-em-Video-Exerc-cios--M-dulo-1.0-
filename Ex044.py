'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print(f'{'=' * 20} LOJA DE COMPRAS {'=' * 20}')

preço = float(input('Qual é o valor do produto que você escolheu? R$'))

print('''AS OPÇÕES DE PAGAMENTO SÃO:

[ 1 ] À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO
[ 2 ] Á VISTA NO CARTÃO: 5% DE DESCONTO
[ 3 ] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
[ 4 ] 3X OU MAIS NO CARTÃO: 20% DE JUROS''')

opção = int(input('Escolha a sua opção de pagamento: '))

if opção == 1:
    total = preço - ( preço * 0.1 )
    print(f'A sua compra custou R${total:.2f}')
elif opção == 2:
    total = preço - ( preço * 0.05 )
    print(f'A sua compra custou R${total:.2f}')
elif opção == 3:
    parcela = preço / 2
    print(f'A sua compra foi dividida em 2x sem juros. Você pagará duas parcelas de R${parcela:.2f}.')
    print(f'No total, a sua compra será de R${preço:.2f}.')
elif opção == 4:
    parcelas = int(input('Em quantas parcelas deseja dividir? '))
    total = preço + (preço * 0.2)
    parcela = total / parcelas
    print(f'A sua compra foi dividida em {parcelas}x com juros de 20%. Você pagará {parcelas} de R${parcela:.2f}.')
    print(f'No total, a compra custou R${total:.2f}')
else:
    print('Opção inválida. Tente novamente!')