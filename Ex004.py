'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

algo = input('Digite uma palavra qualquer: ')
print('Seu tipo primitivo:', type(algo))
print('É alfabético?', algo.isalpha())
print('É numérico?', algo.isnumeric())
print('É alfanumérico?', algo.isalnum())
print('Tem letras maiúsculas?', algo.isupper())
print('Tem letras minúsculas?', algo.islower())
print('É capitalizada?', algo.istitle())