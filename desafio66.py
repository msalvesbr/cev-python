#desafio66.py
# Trabalhando com tuplas
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete',
	'oito','nove','dez','onze','doze','treze','quatorze','quinze',
	'dezesseis','dezessete','dezoito','dezenove','vinte')
soma = contador = 0
while True:
	opcao = int(input('Digite um número entre 0 e 20: '))
	if 0 <= opcao <= 20:
		print(f'Você digitou o número {extenso[opcao]}')
		soma = soma+opcao
	elif opcao == 999:
		break
	contador += 1
	print('Digite 999 para sair. ', end='')
print(f'Você digitou {contador} número e a soma deles é {soma}.')