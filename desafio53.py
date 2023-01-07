# Desafio 53
# Repetições
titulo = ' Estruturas de repetição = Palindromos '
print('{:=^70}'.format(titulo))
frase = str(input('Digite uma frase: ')).strip().upper()
original = frase.replace(" ",'')
tamanho = len(original)
palindromo = str()
palindromo = original[::-1]
'''for c in range(tamanho -1, -1, -1):
	palindromo += original[c]'''
if original == palindromo:
	print('A frase {} e seu inverso {} é um palindromo!'.format(frase, palindromo))
else:
	print('O inverso {} não é igual à {}, logo, não é palindromo.'.format(palindromo, frase))