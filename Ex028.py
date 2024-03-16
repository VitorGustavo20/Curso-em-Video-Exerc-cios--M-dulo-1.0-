'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 à 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
deverá escrever na tela se o usário venceu ou perdeu.'''

from random import randint

print('VAMOS JOGAR UM JOGO!')
computador = randint(0,5)
jogador = int(input('Em que número eu pensei? (de 0 à 5) '))

from time import sleep
print('LOADING...')
sleep(3)

print(f'Computador: Eu pensei no número {computador}')
if jogador == computador:
    print('PARABÉNS! Você venceu!')
else:
    print('Que pena, você perdeu!')
    print('GAMER OVER')