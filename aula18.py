#aula18
teste = list()
teste.append('Gustavo')
teste.append(40)
print(f'A lista teste {teste}')
galera = list()
galera.append(teste)
print(f'A lista galera no append {galera}')
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(f'A lista galera com 2 slice {galera}')
galerao = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45], ['Matheus', 24], ['Lidia', 30], ['Lucas', 12]]
print(f'A lista galerao  {galerao}')
print(f'Só um dado de um elemento do galerao {galerao[2][1]}')
titulo = ' Percorrendo o galerao '
print('{:=^70}'.format(titulo))
for p in galerao:
	print(f'{p[0]} tem {p[1]} anos de idade')
titulo1 = ' Agora com novos dados '
print('{:=^70}'.format(titulo1))
muvuca1 = list()
muvuca2 = list()
maiores = menores = 0
for escolhido in galerao:
	muvuca1.append(escolhido)
print(f'Aqui o muvuca 1 com append direto{muvuca1}')
print('*-'*35)
for n, i in enumerate(galerao):
	muvuca2.append(i)
print(f'Aqui o muvuca 2 com enumerate {muvuca2}')
print('*-'*35)
for pessoa in muvuca1:
	if pessoa[1] >= 21:
		print(f'{pessoa[0]} é maior de idade.')
		maiores += 1
	else:
		print(f'{pessoa[0]} é menor de idade.')
		menores += 1
print(f'Temos {maiores} maiores de idade e {menores} menores.')

