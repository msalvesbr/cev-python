#ex96
def cabecalho(msg):
	print('*'*70)
	print('{:*^70}'.format(msg))
	print('*'*70)

def area51(largura, comprimento):
	area = largura * comprimento
	print(f'A área de um terreno de {largura}x{comprimento} é de {area} m2.')

#Programa
cabecalho(' - Medição de terrenos - ')
l = float(input('Informe a lagura (m): '))
c = float(input('Informe o comprimento (m): '))
area51(l, c)
