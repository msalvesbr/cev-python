# Aula 8
import math as mt
titulo = 'Aula 8'
print('{:=^70}'.format(titulo))
numero = float(input('Digite un número: '))
print('*-'*35)
print('A porção inteira de {:.4f} é {:.2f}'.format(numero, mt.trunc(numero)))
print('A raiz de {:.2f} é {:.2f}'.format(numero, mt.sqrt(numero)))
print('O arredondamento da raiz de {:.2f} para cima é {:.2f}'.format(numero, mt.ceil(mt.sqrt(numero))))
print('O arredondamento da raiz de {:.2f} para baixo é {:.2f}'.format(numero, mt.floor(mt.sqrt(numero))))



print('*-'*35)

