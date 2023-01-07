# Aula 8 - exercicio 19
titulo = 'Desafio do sorteio de Nomes'
print('{:=^70}'.format(titulo))
from random import choice, shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
#choice seleciona uma entre os elementos da lista
sorteado = choice(lista)
print('O premiado com a viagem foi: {}'.format(sorteado))
print('*-'*35)
#shuffle reordena, embaralha a lista
shuffle(lista)
print('A sequência de apresentação será: {}'.format(lista))