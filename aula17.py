# as listas possuem os métodos append, insert, pop, remove, etc
# podemos organizar os itens usando o método sort. Para usar ordem descrescente, usamos sort(reverse=True)
# o método len() devolve o tamanho da lista
# valores = list()
# for cont in range(0,5):
# 	valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
# 	print(f'Na posição {c} encontrei o valor {v}')
# print('Fim!')

# Quando se coloca uma igualdade entre listas (a = b) o Python cria uma ligação entre elas
a = [1, 2, 3, 4, 5, 6, 7]
b = a # faz uma ligação
b = a[:] # faz uma cópia de todos os elementos de a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
