def funcion_Suma(A,num1):
	resultado= A+int(num1)
	return resultado,0

def funcion_Resta(A,num2):
	A=A-int(num1)
	return A	

def funcion_Multiplica(A,num1):
	A=A*int(num1)
	return A

def funcion_Divide(A,num1):
	A=A/int(num1)
	return A

A=0
while True:
	operacion=raw_input("Teclee una operacion +,-,*,/, 0 para salir")
#a,b=funcion_Suma(4,3)
#print a,b
	if operacion == "0":
		break	
	num1=raw_input("Teclee un numero")
	if operacion== "+":
		#resul=funcion_Suma(A,num1)
		#print result
		A=funcion_Suma(A,num1)
		print A
	elif operacion == "-":
		A=funcion_Resta(A,num1)[0]
	elif operacion=="*"	:
		A= funcion_Multiplica(A,num1)[0]
	elif operacion=="/":
		if A==0:
			print("division entre cero , no permitida")
		else:
			print funcion_Divide(A,num1)
	else:
		print ("Operacion erronea")