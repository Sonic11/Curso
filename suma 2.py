def funcion_suma (numero1, numero2):
	 resultado = int(numero1) + int(numero2)
	 return resultado

def funcion_resta (numero1, numero2):
	 resultado = int(numero1) - int(numero2)
	 return resultado

valor1 = raw_input("escribe un numero: ")
valor2 = raw_input("escribe otro numero: ")

resultado = funcion_suma(valor1,valor2)

print resultado

valor1 = raw_input("escribe un numero: ")
valor2 = raw_input("escribe otro numero: ")

variable = funcion_resta(valor1,valor2)
print variable