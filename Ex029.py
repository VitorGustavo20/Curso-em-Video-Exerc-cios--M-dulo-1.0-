'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Velocidade do carro = '))

if velocidade > 80:
    print('VOCÊ FOI MULTADO!')
    multa = ( velocidade - 80 ) * 7
    print(f'A sua multa vai ser de R${multa:.2f}')
else:
    print('Você está na velocidade ideal, ótimo!')
print('TENHA UMA BOA VIAGEM!')