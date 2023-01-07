# Desafio 41
# Condições aninhadas
from datetime import date
titulo = ' Desafio dos Nadadores '
print('{:=^70}'.format(titulo))
nascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
if (idade <= 9):
	print('Você tem {} anos. Bem vindo à categoria Mirim do Clube de Nadadores'.format(idade))
elif(idade > 9 and idade <=14):
	print('Você tem {} anos. Bem vindo à categoria Infantil do Clube de Nadadores'.format(idade))
elif(idade > 14 and idade <=19):
	print('Você tem {} anos. Bem vindo à categoria Júnior do Clube de Nadadores'.format(idade))
elif(idade  > 19 and idade <=20):
	print('Você tem {} anos. Bem vindo à categoria Sênior do Clube de Nadadores'.format(idade))
else:
	print('Você tem {} anos. Bem vindo à categoria Master do Clube de Nadadores'.format(idade))
print('*-'*50)