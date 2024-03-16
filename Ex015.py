'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.'''

km = float(input('Distância percorrida: '))
dias = int(input('Dias alugado: '))
preço = ( 60 * dias ) + ( 0.15 * km )

print(f'O valor total a pagar pelo aluguel do carro é: R${preço:.2f}')