'''Crie um programa que faça o computador jogar JOKENPÔ com você.'''

from random import randint
from time import sleep

print('VAMOS JOGAR PEDRA, PAPEL E TESOURA')

print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('Escolha uma opção: '))
computador = randint(1,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if computador == 1:
    if jogador == 1:
        print('Computador = Pedra')
        print('Jogador = Pedra')
        print('EMPATE!')
    elif jogador == 2:
        print('Computador = pedra')
        print('Jogador = Papel')
        print('VOCÊ GANHOU!')
    else:
        print('Computador = Pedra')
        print('Jogador = Tesoura')
        print('VOCÊ PERDEU!')
elif computador == 2:
    if jogador == 1:
        print('Computador = Papel')
        print('Jogador = Pedra')
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('Computador = Papel')
        print('Jogador = Papel')
        print('EMPATE!')
    else:
        print('Computador = Papel')
        print('Jogador = Tesoura')
        print('VOCÊ VENCEU!')
else:
    if jogador == 1:
        print('Computador = Tesoura')
        print('Jogador = Pedra')
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('Computador = Tesoura')
        print('Jogador = Papel')
        print('VOCÊ PERDEU!')
    else:
        print('Computador = Tesoura')
        print('Jogador = Tesoura')
        print('EMPATE!')
print('FIM DE JOGO!')