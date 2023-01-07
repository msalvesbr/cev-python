# Desafios 45
itens = ['Pedra', 'Papel', 'Tesoura']
from random import randint
from time import sleep
computador = randint(0, 2)
from datetime import date
titulo = ' Desafio do JO-KEN-PO '
print('{:=^40}'.format(titulo))
print('''Escolha sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
print('*-'*20)
jogador = int(input('Sua opção:  '))
print('JO')
sleep(.6)
print('KEN')
sleep(.6)
print('PO!!!')
print('*-'*20)
print('Computador jogou {}!'.format(itens[computador]))
print('Você jogou {}!'.format(itens[jogador]))
print('*-'*20)
if computador == 0: #jogou pedra
	if jogador == 0:
		print('EMPATE!!!')
	elif jogador == 1:
		print('Você GANHOU!!!')
	elif jogador == 2:
		print('Computador GANHOU!!!')
	else:
		print('Deixa de ser burro. Sabe jogar não???')
elif computador ==	1: #jogou papel
	if jogador == 0:
		print('Computador GANHOU!!!')
	elif jogador == 1:
		print('EMPATE!!!')
	elif jogador == 2:
		print('Você GANHOU!!!')
	else:
		print('Deixa de ser burro. Sabe jogar não???')
elif computador == 2: #jogou tesoura
	if jogador == 0:
		print('Você GANHOU!!!')
	elif jogador == 1:
		print('Computador GANHOU!!!')
	elif jogador == 2:
		print('EMPATE!!!')
	else:
		print('Deixa de ser burro. Sabe jogar não???')
print('*-'*20)
