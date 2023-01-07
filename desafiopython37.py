# Desafio 37
# Condições aninhadas
titulo = ' Desafio Conversão de ase matemática '
print('{:=^70}'.format(titulo))
numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:  '))
if (opcao == 1):
	print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif (opcao == 2):
	print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif (opcao == 3):
	print('{} convertido para OCTAL é igual a {}'.format(numero, hex(numero)))
else:
	print('Opção inválida!')
print('*-'*50)