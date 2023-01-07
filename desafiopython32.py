# Desafios 31
from datetime import date
titulo = ' Desafio do ano bissexto '
print('{:=^70}'.format(titulo))
ano = int(input('Digite um ano, ou 0 para analisar o ano atual: '))
print('*-'*35)
if ano == 0:
	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} é bissexto!'.format(ano))
else:
	print('O ano {} NÃO é bissexto!'.format(ano))
print('*-'*35)
