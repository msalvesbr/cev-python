#desafio 71
#Caixa eletrônico
print('*-' * 40)
print('{:^80}'.format('BANCO MARCÃO'))
print('*-' * 40)
valor = int(input('Digite o valor desejado R$ '))
total = valor
cedula = 50
totcedula = 0
##

##
# cassete50 = cassete20 = cassete10 = cassete5  = cassete1  = 50
# valorNumerarioDisponivel = ((cassete50 * 50) + (cassete20 * 20) + 
# 	(cassete10 * 10) + (cassete5 * 5))
# totalCedulasDisponivel = (cassete50 + cassete20 + cassete10 + cassete5 + cassete1)
while True:
	if total >= cedula:
		total -= cedula
		totcedula += 1
	else:
		if totcedula > 0:
			print(f'Total de {totcedula} cédulas de R$ {cedula}')
		if cedula == 50:
			cedula = 20
		elif cedula == 20:
			cedula = 10
		elif cedula ==10:
			cedula = 5
		elif cedula == 5:
			cedula = 1
		totcedula = 0
		if total == 0:
			break
print('*-' * 40)
print('{:^80}'.format('BANCO MARCÃO sempre um prazer atender!'))
print('*-' * 40)
