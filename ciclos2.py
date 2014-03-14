def variable1(rango, variable):

	while True:

		print variable

		if variable == rango:
			break

		variable = variable + 1

	return rango, variable 

def variable2(rango, variable):

	while True:

		print variable

		if variable == 0:
			break

		variable = variable - 1

rango = int(raw_input('ingresa un numero'))

variable = 0

rango, variable = variable1(rango, variable)

variable2(rango, variable) 

	
