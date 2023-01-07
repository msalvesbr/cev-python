# Desafio 47
# Repetições
from time import sleep
titulo = ' Estruturas de repetição = Solução 1 '
print('{:=^70}'.format(titulo))
for c in range(1, 51):
	if c % 2 == 0:
		print(c)
titulo2 =' Estruturas de repetição = Solução 2 '
print('{:=^70}'.format(titulo2))
for c in range(2, 51, 2):
	print(c)

print('BUM! BUM! POW!')