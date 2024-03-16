'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.'''

real = float(input('Quanto de dinheiro você tem em sua carteira: R$'))
dolar = real / 4.95

print(f'Com R${real:.2f} você pode comprar U${dolar:.2f}')