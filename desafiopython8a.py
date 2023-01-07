# Aula 8
import math as mt
titulo = 'Desafio do cateto oposto'
print('{:=^70}'.format(titulo))
co = float(input('Digite o cumprimento do cateto oposto: '))
ca = float(input('Digite o cumprimento do cateto adjacente: '))
#fórmula sem o pacote Math
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
#usando a função do pacote Math
hip = mt.hypot(co, ca)
print('*-'*35)
print('A hipotenusa do triângulo de catetos {:.2f} e {:.2f}, é \n{:.8f} usando o pacote Math\n{:.8f} calculando direto'.format(co, ca, hip, hipotenusa))


print('*-'*35)

