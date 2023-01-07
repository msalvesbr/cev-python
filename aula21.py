#aula 21
#docstrings
def contador(i, f, p):
	"""
	A partir do parametros informados, faz uma contagem e mostra na tela.
	:param i: inicio da contagem
	:param f: final da contagem
	:param p: incremento da contagem

	Essa funcao nao tem retorno
	"""
	print('{:=^70}'.format(str(' Contador ')))
	c = i
	while c <= f:
		print(f'{c}', end='..')
		c += p
	print('Pronto!')

contador(2,50,2)
help(contador)
