# Desafios aula 7 - Celsius pra Fahrenheith
titulo = 'Desafios aula 7 - Celsius pra Fahrenheith:'
print('{:=^70}'.format(titulo))
temp = float(input('Digite uma temperatura em °Célsius: '))
tf = 9 * temp / 5 + 32
print('*-'*35)
print('A temperatura de {:.2f}°C, corresponde a  {:.2f}°Fahrenheith'.format(temp, tf))
print('*-'*35)

