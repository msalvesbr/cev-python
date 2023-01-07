# Desafios aula 7 - Aumento de salário
titulo = 'Desafios aula 7 - 15 por cento de aumento:'
print('{:=^70}'.format(titulo))
salario = float(input('Digite o valor do salário em R$ '))
comAumento = salario + (salario * 15 / 100)
print('*-'*35)
print('Após o reajuste de 15%, seu salário de {:.2f}, passará para  {:.2f}'.format(salario, comAumento))
print('*-'*35)
