#desafio 67
while True:
	numero = int(input('Digite um número para ver sua tabuada: '))
	if(numero < 0):
		break
	print('=-'*25)
	for c in range(1,11):
		print(f'{numero} x {c} = {numero * c}')
	print('=-'*25)
