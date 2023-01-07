# Desafios aula 7
titulo = 'Desafios aula 7:'
print('{:=^70}'.format(titulo))
n1 = int(input('Digite um número: '))
print('O antecessor de {} é {} e o sucessor é {}'.format(n1, (n1-1), (n1+1)))
print('*-'*35)
print('O dobro de {} é {}, \no triplo é {} \ne a raiz quadrada é {}'.format(n1, (n1*2), (n1*3), (n1 ** (1/2))))