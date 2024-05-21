

"""
CONTADOR DE PALABRAS: PEDIR AL USUARIO UNA FRASE Y CONTAR CUANTAS PALABRAS CONTIENE ESTA 

"""

# CODE :
	
frase = input("Ingrese frase: ")

frase_nueva = frase.strip().split(" ")	

print("Tu frase tiene {} palabras".format(len(frase_nueva)))	