#Dessafio 86
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
titulo = ' Desafio 86 Matriz organizada '
print('{:=^70}'.format(titulo))
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = (int(input(f'Digite um número para [{l}, {c}]: ')))
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}] ', end='')
	print()