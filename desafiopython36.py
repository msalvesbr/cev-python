# Desafio 36
# Condições aninhadas
from datetime import date
titulo = ' Desafio do Empréstimo bancário '
print('{:=^70}'.format(titulo))
montante = float(input('Digite o valor do empréstimo em R$: '))
renda = float(input('Informe sua renda mensal: '))
tempo = int(input('Deseja parcelar em quantos anos? '))
parcela = montante / (tempo*12)
if (parcela > renda * (30/100)):
	print('Seu salário não comporta uma parcela tão alta. Precisamos reduzir o valor ou aumentar o prazo')
else:
	print('Empréstimo aprovado! Você irá pagar em {:.0f} parcelas de R$ {:.2f} durante {} anos'.format((tempo*12), parcela, tempo))
print('*-'*50)