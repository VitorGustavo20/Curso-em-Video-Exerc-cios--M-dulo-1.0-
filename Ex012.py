'''Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preço = float(input('Qual é o preço do produto? R$'))
desconto = preço - ( preço * 0.05 )

print(f'Um produto que custa R${preço:.2f}, após um desconto de 5%, passa a custar R${desconto:.2f}')