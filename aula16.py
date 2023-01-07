# aula 16
lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
# uma forma de mostrar a lista ordenada - vira uma lista
print(sorted(lanche))
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
# modos de usar o for
# for comida in lanche:
# 	print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
# 	print(cont, end='#')
# 	print(lanche[cont])
# print('Fora do for')

for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')

# Métodos das tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(1))
