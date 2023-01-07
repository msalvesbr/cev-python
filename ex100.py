#desafio 100
from time import sleep
from random import randint
def sorteia(lista):
	contador = 0
	print('{:=^70}'.format(str(' Sorteando... ')))
	sleep(0.3)
	while contador < 5:
		escolhido = randint(1, 10) 
		if escolhido not in lista:
			lista.append(escolhido)
			contador +=1


def somaPares(lista):
	soma = 0
	for valor in lista:
		if valor % 2 == 0:
			soma += valor
	print(f'A soma dos números pares da lista é {soma}')

numeros = list()
sorteia(numeros)
print(numeros)
print('{:=^70}'.format(str(' Somando os pares da lista... ')))
somaPares(numeros)