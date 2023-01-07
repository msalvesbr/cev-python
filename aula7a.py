# Aula 7 - Operadoress
# Precedência de operadores:
# 1 () - mesmo para encadear sequência de operações aritméticas, use somente parentesis
# 2 ** - potenciação
# 3 * multiplcação, / divisão real, // divisão inteira, % resto da divisão
# 4 + soma e - subtração
titulo = 'Brincando com os operadores:'
print('{:=^70}'.format(titulo))
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('a divisão inteira é {} e a potência é {}'. format(di, e))