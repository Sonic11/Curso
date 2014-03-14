def suma(numero1, numero2):
	resultado = int(numero1) + int(numero2)
	return resultado

def resta(numero1, numero2):
	resultado = int(numero1) - int(numero2)
	return resultado

def multiplica(numero1, numero2):
	resultado = int(numero1) * int(numero2)
	return resultado

	operacion = raw_input("Ingresa una Operacion:")
	valor1 = raw_input("Ingresa un Numero:")
	valor2 = raw_input("Ingresa otro Numero:")

	if operacion == 'suma':

		print suma

	suma = suma(valor1, valor2)
	


	



