# Desafio 52
# Repetições
titulo = ' Estruturas de repetição = Números Primos '
print('{:=^70}'.format(titulo))
numero = int(input('Digite um número: '))
divisivel = 0
for c in range(1, numero + 1):
	if numero % c == 0:
		divisivel += 1
	#print('{} '.format(c), end='-> ')
if divisivel == 2:
	print('O número {} só é divisivel por 1 e por ele mesmo e É PRIMO!'.format(numero))
else:
	print('O número {} é divisível por {} números e portanto NÃO É PRIMO!'.format(numero, divisivel))