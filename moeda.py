#módulo de funções 
#moeda.py

def aumentar(preco, taxa):
	resultado = preco + (preco * taxa/100)
	return resultado

def diminuir(preco, taxa):
	resultado = preco - (preco * taxa/100)
	return resultado

def dobro(valor):
	resultado = valor * 2
	return resultado

def metade(valor):
	resultado = valor / 2
	return resultado
