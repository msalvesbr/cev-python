# Desafios aula 7 - Conversao de moeda
titulo = 'Desafios aula 7 - Conversão em dólar:'
print('{:=^70}'.format(titulo))
real = float(input('Qual o valor rm R$ a converter? '))
print('*-'*35)
print('Com R${:.2f} você pode comprar US${:.2f} dólares'.format(real, (real/4.8)))
print('*-'*35)
