# Desafio 44
# Condições aninhadas
titulo = ' Lojas Alves '
print('{:=^70}'.format(titulo))
valor = float(input('Valor das compras R$: '))
print('''Escolha uma forma de pagamento:
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual sua opção:  '))
if (opcao == 1):
	print('O valor com desconto de pagamento em dinheiro/cheque será de R$ {:.2f}. Obrigado e volte sempre!'.format(valor*(1-(10/100))))
elif (opcao == 2):
	print('O valor com desconto de pagamento à vista no cartão será de R$ {:.2f}. Obrigado e volte sempre!'.format(valor*(1-(5/100))))
elif (opcao == 3):
	print('O valor no cartão em até 2x será de R$ {:.2f}. Obrigado e volte sempre!'.format(valor))
elif (opcao == 4):
	total = valor + (valor*(20/100))
	parcelas = float(input('Informe o númerop de parcelas: '))
	print('Em {:.0f} vezes no cartão vai ficar R$ {:.2f} em {:.0f} parcelas de R$ {:.2f}'.format(parcelas, total, parcelas, (total/parcelas)))
else:
	print('Opção inválida!')
print('*-'*50)