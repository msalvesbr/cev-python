# Desafio 49
# Repetições
from time import sleep
titulo = ' Estruturas de repetição = Tabuada '
print('{:=^70}'.format(titulo))
numero = int(input('Digite um número: '))
for c in range(1, 11):
	print('{} X {:2} = {}'.format(numero, c, numero*c))
