# Desafio 39
# Condições aninhadas
from datetime import date
titulo = ' Desafio Serviço Militar '
print('{:=^70}'.format(titulo))
nascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
if (anoAtual - nascimento == 18):
	print('Apresente-se na Junta de Alistamento para o Serviço Militar')
elif(anoAtual - nascimento > 18):
	print('Se você ainda não se alistou, vc está em dívida com o Serviço Militar obrigatório')
else:
	if(18-(anoAtual - nascimento) == 1):
		print('No ano quem vem, ao completar 18 anos, apresente-se na Junta de Alistamento para o Serviço Militar')
	else:
		print('Em {} anos, ao completar 18 anos, apresente-se na Junta de Alistamento para o Serviço Militar'.format(18-(anoAtual - nascimento)))
print('*-'*50)