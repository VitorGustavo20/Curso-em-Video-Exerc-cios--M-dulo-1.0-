'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 , calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.'''

salário = float(input('Qual é o seu salário? '))

if salário > 1250:
    aumento = salário + ( salário * 0.10 )
    porcentagem = 10
else:
    aumento = salário + ( salário * 0.15 )
    porcentagem = 15
print(f'O seu salário de R${salário:.2f}, recebeu um reajuste de {porcentagem}%, passando a ser de R${aumento:.2f}')