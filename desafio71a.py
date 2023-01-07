#desafio 71a
#Caixa eletrônico
print('*-' * 40)
print('{:^80}'.format('BANCO MARCÃO'))
print('*-' * 40)

while True:
	valor = int(input("Quantos reais você quer sacar? R$ "))
	total = valor
	cedulas = [50, 20, 10, 5, 1]
	valorrestante = resto = entregue = 0
	for x in range(0, len(cedulas)):
		if (valor % 2) == 0:  #cedulas[x]
			if valor - valorrestante >= cedulas[x]:
				print(f"{(valor - valorrestante) // cedulas[x]} cédulas de {cedulas[x]} reais")
				valorrestante = (valor // cedulas[x]) * cedulas[x]
				print(f'{valorrestante:.2f}')
		else:
			resto = valor % cedulas[x]
			nCed = int((valor - valorrestante) // cedulas[x])
			if valor - valorrestante >= cedulas[x]:
				print(f"{nCed} cédulas de {cedulas[x]} reais*")
				entregue += (nCed * cedulas[x]) 
				print(f'{entregue:.2f}')
				valor = resto
				print(f'Valor: {valor} entregue {entregue} resto {resto}')
				# if (resto % 2) == 0:
				# 	valorrestante = entregue

	if total == 0:
		break

print('*-' * 40)
print('{:^80}'.format('BANCO MARCÃO sempre um prazer atender!'))
print('*-' * 40)
