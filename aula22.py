#aula 22
#módulos
def fatorial(valor):
	f = 1
	for c in range(1, valor+1):
		f *= c
		print(f)
	return f

numero = int(input('Digite um valor: '))
fator = fatorial(numero)
print(f'O fatorial de {numero} é {fator}.')