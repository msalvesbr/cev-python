#Desafio 89
cadastro = list()
while True:
	nome  = str(input('Aluno: '))
	nota1 = float(input('Nota 1: ')) 
	nota2 = float(input('Nota 2: ')) 
	media = float(nota1 + nota2) / 2
	cadastro.append([nome, [nota1, nota2], media])
	continua = str(input('Continua? [S/N] '))
	if continua in "Nn":
		break
print('=' * 60)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('=' * 60)
for numero, aluno in enumerate(cadastro):
	print(f'{numero:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
	print('*-' * 30)
	opcao = int(input("Deseja ver as notas de qual aluno? (999 termina o programa) "))
	if opcao == 999:
		print('*-' * 30)
		print('{:^60}'.format("Fim"))
		print('*-' * 30)
		break
	if opcao <= len(cadastro) - 1:
		print(f'Notas de {cadastro[opcao][0]} são {cadastro[opcao][1]}')