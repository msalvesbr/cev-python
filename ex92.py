#desafio 92
from datetime import datetime
print('{:=^70}'.format(str(' Ministério do Trabalho ')))
rh = list()
bd_pessoas = dict()
contador = idade = ano_nascimento = 0
continua = ' '
while True:
	bd_pessoas.clear()
	bd_pessoas['nome'] = str(input('Nome: '))
	ano_nascimento = int(input('Ano de nascimento: '))
	bd_pessoas['idade'] = datetime.now().year - ano_nascimento
	bd_pessoas['ctps'] = int(input('Carteira de trabalho (digite 0 se não tiver CTPS): '))
	if bd_pessoas['ctps'] != 0:
		bd_pessoas['ano_contrato'] = int(input('Começou a trabalhar em: '))
		bd_pessoas['aposentaCom'] = bd_pessoas['idade'] + ((bd_pessoas['ano_contrato'] + 35) - datetime.now().year)
		bd_pessoas['salario'] = float(input('Salário em R$: '))
	rh.append(bd_pessoas.copy())
	print(bd_pessoas)

	continua = str(input('Continua? [S/N] ')).strip().upper()[0]
	if continua == 'N':
			break
print(f'Nossa empresa tem {len(rh)} funcionários')
print(rh)