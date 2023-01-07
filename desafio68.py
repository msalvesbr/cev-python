#desafio 68
#Jogo de par ou impar
from random import randint
contador = 1
vitorias = 0
while True:
	numero = int(input('Digite um valor: '))
	computador = randint(0, 10) # numero com a escolha do computador
	tipo = ' '
	total = numero + computador
	while tipo not in 'PpIi':
		tipo = str(input('Par ou Impar? ')).strip().upper()[0]
	print(f'Você jogou {numero} e o computador jogou {computador}.')
	if tipo == 'P':
		if total % 2 == 0:
			print('Você VENCEU!!!')
			vitorias +=1
		else:
			print('Você perdeu. O Computador VENCEU!!')
			break
	elif tipo == 'I':
		if total % 2 == 1:
			print('Você VENCEU!!!')
			vitorias +=1
		else:
			print('Você perdeu. O Computador VENCEU!!')
			break
	print('Vamos jogar novamente...')
	contador += 1
	print('=-'*25)
print(f'Game Over. Vocês jogaram {contador} vezes, você venceu {vitorias} partidas.')