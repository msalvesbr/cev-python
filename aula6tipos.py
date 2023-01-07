# Desafio4
# Receber dois numeros e somar
# Brincando com  testes de tipo
dado1 = input('Digite qualquer coisa: ')
print('o valor {} é ? '.format(dado1))
print('= alpha:? {}'.format(dado1.isalpha()))
print('= numeric:? {}'.format(dado1.isnumeric()))
print('= alpha numeric:? {}'.format(dado1.isalnum()))
print('= digit:? {}'.format(dado1.isdigit()))
print('= decimal:? {}'.format(dado1.isdecimal()))
print('= identifier:? {}'.format(dado1.isidentifier()))
print('= minusculo:? {}'.format(dado1.islower()))
print('= maiusculo:? {}'.format(dado1.isupper()))
print('= imprimivel:? {}'.format(dado1.isprintable()))
print('= espaço:? {}'.format(dado1.isspace()))
print('= title:? {}'.format(dado1.istitle()))