# Desafios aula 7 - Locadore de carros
titulo = 'Desafios aula 7 - Custo de Locação de carro:'
print('{:=^70}'.format(titulo))
dias = int(input('Quantos dias durará a locação? '))
kilometragem = float(input('Quantos km´s rodados? '))
aPagar = (dias * 60) + (kilometragem * 0.15)
print('*-'*35)
print('O total das diárias será R$ {:.2f}'.format(aPagar))
print('*-'*35)

