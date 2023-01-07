valores = list()
maior = 0
menor = 0
contador = 0
repetido = 0
#continua = ' '
while True:
	continua = ' '
	numero = int(input(f"Digite um número: "))
	if numero not in valores:
		valores.append(numero)
	else:
		print(f'O número {numero} já foi digitado.')
		repetido += 1 
		continua = 's'
	if contador == 0:
		maior = menor = numero
	elif numero > maior:
		maior = numero
	elif numero < menor:
		menor = numero
	if continua == ' ':
		continua = str(input('Continua? [S/N] ')).strip().upper()[0]
	if continua in 'N':
		break
	contador += 1
print('=' * 60)
print(f'Foram digitados {contador} números', end='')
print(f' com {repetido} repetições')
print(f'Os valores foram {valores}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
print('=' * 60)