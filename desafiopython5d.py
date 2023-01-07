# Desafios aula 7 - Percentual de desconto
titulo = 'Desafios aula 7 - 5 por cento de desconto:'
print('{:=^70}'.format(titulo))
preco = float(input('Digite o preço do produto em R$'))
comDesconto = preco - (preco * 5 / 100)
print('*-'*35)
print('O produto que custava {:.2f}, na promoção com 5% de desconto vai custar {:.2f}'.format(preco, comDesconto))
print('*-'*35)
