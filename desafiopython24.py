# Aula 9 - Cadeias de caracteres
# Fatiamento
# fatia[inicio:final:passo]
# fatia[:5]   - do inicio até a posição 5 exclusive
# fatia[15:]  - a partir da posição indicada até o final
# fatia[9::3] - a partir da posição até o final em saltos de 3
# comprimento (len(elemento-a-medir-o-comprimento))
# Podemos usar o count para retornar o número de ocorrências numa lista: 
#     frase.count('o') - retorna 3 ocorrências
#     frase.count('caracter buscado', inicio 0, fim 13)
# frase.find('deo') - retorna o início da cadeia dada. Se não encontra, retorna -1
# operador booleano 'in' localiza uma cadeia em uma lista
# upper()/lower() - tudo pra maiusc/minisc
# capitalize() - só o primeiro caractere maiusc.
# title()
# strip()  remove espaços no inicio e no final da string
# split() quebra a frases nos espaços e cria uma lista das palavras
# '#'.join() faz o contrário, junta numa unica string conectada pelo caractere entre aspas no inicio 

titulo = ' Resolvendo desafios da aula 9 '
print('{:=^70}'.format(titulo))
frase = 'Curso em Vídeo Python'
print('A sequência será: {}'.format(frase))

# desafio22
nome = str(input('Digite um nome completo: '))
print('*-'*35)
print('Tudo maiúsculo: {}', format(nome.upper()))
print('Tudo minúsculo: {}', format(nome.lower()))
print('*-'*35)
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('*-'*35)
primeiroNome = nome.split()
print('O primeiro nome tem {} letras'.format(len(primeiroNome[0])))

# desafio23
print('*-'*35)
ano = input('Digite um ano: ')
print('O ano informado é composto por:\n{} unidades\n{} dezenas\n{} centenas e\n{} milhares'.format(ano[3], ano[2], ano[1], ano[0]))