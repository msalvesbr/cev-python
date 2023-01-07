# Desafios 43
titulo = ' Desafio dos Gordinhos '
print('{:=^70}'.format(titulo))
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
print('*-'*35)
#  a/formula do IMC é peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
	print('Você está com baixo peso. É preciso ter atenção!')
elif 18.5 <= imc < 25:
	print('Você está no peso ideal. Parabéns!')
elif 25 <= imc < 30:
	print('Você está com sobrepeso. É preciso atividade física!')
elif 30 <= imc < 40:
	print('Você entrou na obseidade. Todo cuidado é pouco!')
else: 
	print('Se mata doido!')
print('*-'*35)
#** colocar cores no terminal **

