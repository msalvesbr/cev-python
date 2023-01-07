# Desafios 29 
titulo = 'Desafio da Multa de Trânsito'
print('{:=^70}'.format(titulo))
velocidade = float(input('Qual a velocidade? '))
print('*-'*35)
if velocidade > 80:
	multa = 7 * (velocidade - 80)
	print('MULTADO!!!! Pensa que está em Le Mans? . Vais pagar R$ {:.2f} de multa'.format(multa))
else:
	print('Tenha um bom dia! Dirija com segurança')
print('*-'*35)

# Desafios 30 
print('Vamos saber se a velocidade que vc informou é par ou impar: ')
resultado = velocidade % 2
if resultado == 0:
	print('É par!')
else:
	print('É impar!')
