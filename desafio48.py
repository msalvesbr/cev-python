# Desafio 48
# Repetições
from time import sleep
titulo = ' Estruturas de repetição = Soma dos impares até 500 '
print('{:=^70}'.format(titulo))
soma = 0
contador = 0
for c in range(1, 501, 2):
	if c % 3 == 0:
		soma += c
		contador += 1

print('A soma de {} números ímpares múltiplos de 3 entre 0 a 500 é = {}'.format(contador, soma))
