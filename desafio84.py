#Dessafio 84
tmp = []
principal = []
maior = menor = 0
titulo = ' Desafio 84 Peso Pesado '
print('{:=^70}'.format(titulo))
while True:
	tmp.append(str(input('Digite o nome: ')))
	tmp.append(float(input('Qual o peso? ')))
	if len(principal) == 0:
		manior = menor = tmp[1]
	elif tmp[1] > maior:
		maior = tmp[1]
	elif tmp[1] < menor:
		menor = tmp[1]

	principal.append(tmp[:])
	tmp.clear()
	continua = str(input('Continua? [S/N]'))
	if continua in 'Nn':
		break
result = " Resultado "
print('{:=^70}'.format(result))
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso informado foi de {maior} Kg. Esse é o peso de ', end='' )
for pessoa in principal:
	if pessoa[1] == maior:
		print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso informado foi de {menor} Kg. Esse é o peso de ', end='' )
for pessoa in principal:
	if pessoa[1] == menor:
		print(f'[{pessoa[0]}] ', end='')
print()