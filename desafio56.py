# desafio 56
somaIdades = 0
mediaIdades = 0
maisVelho = 0
nomeMaisVelho = ''
mulheresAte20 = 0
plural = ''
for p in range(1, 5):
	print(' ----- {} º Pessoa -----'.format(p))
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo: [M/F]')).strip()
	somaIdades += idade
	if p == 1 and sexo in 'Mm':
		maisVelho = idade
		nomeMaisVelho = nome
	if sexo in 'Mm' and idade > maisVelho:
		maisVelho = idade
		nomeMaisVelho = nome
	if sexo in "Ff" and idade < 20:
		mulheresAte20 += 1
	if mulheresAte20 > 1:
		plural = 'mulheres'
	else:
		plural = 'pessoa'

mediaIdades = somaIdades / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdades))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisVelho, nomeMaisVelho))
print('Ao todo temos {} {} com menos de 20 anos.'.format(mulheresAte20, (plural)))