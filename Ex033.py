'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
maior = 0
menor = 0
#maior número
if n1 > n2  and n1 > n2:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
