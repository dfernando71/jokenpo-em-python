"""
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from os import system
from random import randint
import random
from time import sleep, time

itens = ('Pedra', 'Papel', 'Tesoura')

pc = randint(0, 2)
print('{:=^40}'.format('JOKENPO'))
print('''[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
''')
opcao = int(input('Qual é a sua jogada?'))
system('cls')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('=' * 25)
print('Computador Jogou: {}'.format(itens[pc]))
print('Você Jogou: {}'.format(itens[opcao]))
print('=' * 25)

#computador joga pedra

if pc == 0:
    if opcao == 0:
        print('EMPATE!!')
    elif opcao == 1:
        print('VOCÊ VENCEU!!')
    elif opcao == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')

#computador joga papel

if pc == 1:
    if opcao == 0:
        print('VOCÊ VENCEU!!')
    elif opcao == 1:
        print('EMPATE!!')
    elif opcao == 2:
        print('COMPUTADOR VENCEU!!')
    else:
        print('JOGAVA INVALIDA')

#computador joga tesoura

if pc == 2:
    if opcao == 0:
        print('COMPUTADOR VENCEU!!')
    if opcao == 1:
        print('VOCE VENCEU!!')
    if opcao == 2:
        print('EMPATE!!')
    else:
        print('JOGADA INVALIDA')

