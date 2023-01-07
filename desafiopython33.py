# Desafios 33
titulo = ' Desafio de classificar uma lista de valores '
print('{:=^70}'.format(titulo))
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print('*-'*35)
# para achar o menor
menor = a
if b<a and b<c:
	menor = b
if c<a and c<b:
	menor = c
#para achar o maior
maior = a
if b>a and b>c:
	maior = b
if c>a and c>b:
	maior = c
print('O menor número entre {}, {} e {} é {}'.format(a, b, c, menor))
print('e o maior número é {}'.format(maior))
print('*-'*35)
