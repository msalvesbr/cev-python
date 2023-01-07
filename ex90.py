#desafio 90
aluno = dict()
aluno['nome']  = str(input('Aluno: '))
aluno['media'] = float(input(f'Informe a média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
	aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 5:
	aluno['situacao'] = 'Reprovado'
else:
	aluno['situacao'] = 'Em recuperação'
print('=-'*30)
for k,v in aluno.items():
	print(f' - {k} é igual a {v}')