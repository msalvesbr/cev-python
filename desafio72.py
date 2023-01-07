#desafio72.py
# Trabalhando com tuplas
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete',
	'oito','nove','dez','onze','doze','treze','quatorze','quinze',
	'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
	opcao = int(input('Digite um número entre 0 e 20: '))
	if 0 <= opcao <= 20:
		print(f'Você digitou o número {extenso[opcao]}')
	elif opcao == 999:
		break
	print('Digite 999 para sair. ', end='')
