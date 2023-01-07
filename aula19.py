#aula 19
titulo = ' Estudando dicionários '
print('{:=^70}'.format(titulo))
print('*-'*30)
pessoas = {'nome': 'Marcos', 'sexo': 'M', 'idade':48}
titulo = ' Printando pela referência '
print('{:=^70}'.format(titulo))
print(pessoas['nome'], end=' ')
print(pessoas['sexo'], end=' ')
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
titulo = ' Printando em estruturas de repetição '
print('{:=^70}'.format(titulo))
for i in pessoas.keys():
	print(i)
print('*-'*30)
for i in pessoas.values():
	print(i)
print('*-'*30)
for k,v in pessoas.items():
	print(f'{k} >>> {v}')
titulo = ' Alterando valores num dicionário '
print('{:=^70}'.format(titulo))
pessoas['nome'] = 'Soleil'
pessoas['sexo'] = 'F'
# adicionando um elemento no dicionário
pessoas['peso'] = '66'
for k,v in pessoas.items():
	print(f'{k} >>> {v}')
titulo = ' Criando um dicionário dentro de uma lista '
print('{:=^70}'.format(titulo))
estado1 = {'uf': 'Distrito Federal', 'sigla': 'RJ'}
estado2 = {'uf': 'Ceará', 'sigla': 'CE'}
estado3 = {'uf': 'Maranhão', 'sigla': 'MA'}
estado4 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado5 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado6 = {'uf': 'Bahia', 'sigla': 'BA'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
brasil.append(estado4)
brasil.append(estado5)
brasil.append(estado6)
print(estado6)
print(brasil)
# for n in brasil.items():
# 	print(brasil[n])
# 	print("***************")
# 	print(brasil[n]['uf'])

titulo = ' O preenchimento dos dicionários tem segredos '
print('{:=^70}'.format(titulo))
pessoa = dict()
galera = list()
for p in range(0, 3):
	pessoa['nome'] = str(input('Digite o nome: '))
	pessoa['idade'] = int(input('idade: '))
	galera.append(pessoa.copy())	# aqui não se pode usar fatiamento [:] e se não referenciar,
									# armnazena apenas o último elemento informado
print(galera) 
print('*-'*30)
for p in galera:
	for k, v in p.items():
		print(f'O campo {k} tem valor {v}.')

	