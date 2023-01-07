# Desafios 31 
titulo = 'Desafio da Multa de Trânsito'
print('{:=^70}'.format(titulo))
distancia = float(input('Qual o total em kilometros da sua viagem? '))
print('*-'*35)
# Modo extenso
## if distancia <= 200:
## 	preco = distancia * 0.50 
## 	print('O ticket para sua viagem de {} km custará R$ {:.2f}'.format(distancia, preco))
## else:
## 	preco = distancia * 0.45
## 	print('O ticket para sua viagem de {} km custará R$ {:.2f}'.format(distancia, preco))
## print('*-'*35)
# Modo compacto
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O ticket para sua viagem de {} km custará R$ {:.2f}'.format(distancia, preco))