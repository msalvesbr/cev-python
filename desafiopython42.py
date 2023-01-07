# Desafios 42
titulo = ' Desafio dos segmentos que formam um triangulo '
print('{:=^70}'.format(titulo))
a = int(input('Digite o tamanho do primeiro segmento: '))
b = int(input('Digite o tamanho do segundo segmento: '))
c = int(input('Digite o tamanho do terceiro segmento: '))
print('*-'*35)
# a regra determina que a soma de dois segmentos não pode ser maior q o terceiro
if a < b + c and b < a + c and c < a + b:
	if a == b == c:
			print('Os segmentos {}, {} e {} podem formar um triângulo, e será um triângulo EQUILÁTERO!'.format(a, b, c))
	elif a != b != c != a:
			print('Os segmentos {}, {} e {} podem formar um triângulo, e será um triângulo ESCALENO!'.format(a, b, c))
	else:
			print('Os segmentos {}, {} e {} podem formar um triângulo, e será um triângulo ISÓCELES!'.format(a, b, c))
else: 
	print('Os segmentos {}, {} e {} NÃO podem formar um triângulo.'.format(a, b, c))
print('*-'*35)
#** colocar cores no terminal **

