# Desafio 50
# Repetições
titulo = ' Estruturas de repetição = Soma dos pares entre os digitados '
print('{:=^70}'.format(titulo))
soma = 0
contador = 0
for c in range(1, 7):
	numero = int(input('Digite um número: '))
	if numero % 2 == 0:
		soma += numero
		contador += 1
print('Você informou {} números pares e sua soma é = {}'.format(contador, soma))
