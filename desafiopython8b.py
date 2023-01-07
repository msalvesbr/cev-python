# Aula 8
from math import sin, cos, tan, radians
titulo = 'Desafio das medidas trigonométricas'
print('{:=^70}'.format(titulo))
#fórmulas do pacote Math
angulo = float(input('Digite um ângulo: '))
seno    = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente= tan(radians(angulo))
print('*-'*35)
print('O ângulo de {:.0f}° possui\nseno de {:.2f},\ncosseno de {:.2f}, e\n\
tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))
print('*-'*35)

