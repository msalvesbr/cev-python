#Desafio 88
from random import randint
from time   import sleep
apostas = list()
jogos = list()
total = 1
titulo = ' Desafio 88 Sorteando jogos da Mega-sena '
print('{:=^70}'.format(titulo))
quantas = int(input(f'Digite o número de apostas: '))
while total <= quantas:
	contaDezenas = 0
	while True:
		dezena = randint(1, 60)
		if dezena not in jogos:
			jogos.append(dezena)
			contaDezenas += 1
		if contaDezenas >= 7:
			break
	jogos.sort()
	apostas.append(jogos[:])
	jogos.clear()
	total += 1	
titulo1 = ' Sorteando {quantas} jogos '
print('{:=^70}'.format(titulo))
for n, l in enumerate(apostas):
	print(f'Jogo {n+1}: {l}')

