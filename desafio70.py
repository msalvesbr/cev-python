#desafio 70
#Lojão
contador = 1
total = altoValor = contaVAlto = menorPreco = 0
while True:
	produto = str(input('Nome do Produto: '))
	preco = float(input('Valor R$: '))
	continua = ' '
	total += preco
	if contador == 1:
		menorPreco = preco
	if preco < menorPreco:
		menorPreco = preco
	if preco >= 1000:
		contaVAlto += 1
	while continua not in 'sSnN':
		continua = str(input('Continua? [S/N] ')).strip().upper()[0]
	if continua == 'N':
			break
	contador += 1
	print('=-'*25)
print('{:=^50}'.format('Fim do Programa'))
print(f'O total gasto foi de R$ {total:.2f}')
print(f'O produto mais barato custou R$ {menorPreco:.2f}')
print(f'A compra contém {contaVAlto} produtos com preço superior a R$ 1000,00 ')
