#desafio 91
from random import randint
from time import sleep
# para sortear o dicionário é necessário importar itemgetter de operator
from operator import itemgetter

jogador = dict()
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('{:=^70}'.format(str(' Casino - Valores sorteados ')))
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
	print(f' - {v[0]} tirou {v[1]}')
	sleep(.16)
