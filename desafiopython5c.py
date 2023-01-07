# Desafios aula 7 - Área da parede
titulo = 'Desafios aula 7 - Área da parede:'
print('{:=^70}'.format(titulo))
largura = float(input('Largura da parede '))
altura = float(input('Altura da parede '))
print('*-'*35)
print('Para pintar uma área total de {:.2f}, {:.2f}x{:.2f} '.format((largura*altura), largura, altura))
quoeficiente = (altura*largura)/2
print('Você precisará de {:.2f} litros de tinta'.format(quoeficiente)) 
print('*-'*35)
