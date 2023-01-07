# Desafios Aula 
from random import randint
titulo = 'Desafio das condicionais'
print('{:=^70}'.format(titulo))
#fórmulas do pacote random
numero = randint(0, 5)
print('Pensei num número. Adivvinhe se for capaz!')
palpite = int(input('Digite um número entre a e 5: '))
print('*-'*35)
if numero == palpite:
	print('Parabéns!!!! Vc acertou.')
else:
	print('Mais sorte na próxima!')
print('*-'*35)

