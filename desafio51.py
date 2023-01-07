# Desafio 51
# Repetições
titulo = ' Estruturas de repetição = Soma dos 10 primeiros termos de uma PA '
print('{:=^70}'.format(titulo))
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimoTermo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimoTermo + razao, razao):
	print('{} '.format(c), end='-> ')
print(' Fim!')