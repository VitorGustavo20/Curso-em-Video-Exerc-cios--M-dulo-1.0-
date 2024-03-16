'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

distância = float(input('Distância percorrida = '))

if distância <= 200:
    passagem = 0.50 * distância
else:
    passagem = 0.45 * distância

print(f'A viagem custou R${passagem:.2f}')