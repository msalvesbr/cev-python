#Dessafio 87
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
titulo = ' Desafio 86 Matriz organizada '
somaPares = somaColuna = maior = 0
print('{:=^70}'.format(titulo))
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = (int(input(f'Digite um número para [{l}, {c}]: ')))
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}] ', end='')
		if matriz[l][c] % 2 == 0:
			somaPares += matriz[l][c]
		if matriz[l][c] > maior:
			maior = matriz[l][c]
	print()
for l in range(0, 3):
	somaColuna += matriz[l][2]
print(f'Soma dos valores pares: {somaPares}')
print(f'O maior valor digitado foi {maior}.')
print(f'a soma dos elementos da 3a coluna é {somaColuna}')