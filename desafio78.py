valores = list()
maior = 0
menor = 0
for cont in range(0,5):
	valores.append(int(input('Digite um valor: ')))
	if cont == 0:
		maior = menor = valores[cont]
	elif valores[cont] > maior:
		maior = valores[cont]
	elif valores[cont] < menor:
		menor - valores[cont]
print('=' * 60)
print(f'Foram digitados os valores {valores}')
#print(f'O maior número digitado foi {max(valores)} na posição {valores.index(max(valores))}')
#print(f'O menor número digitado foi {min(valores)} na posição {valores.index(min(valores))}')
print('=' * 60)
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
for c, v in enumerate(valores):
	print(f'Na posição {c} encontrei o valor {v}')
print('Fim!')