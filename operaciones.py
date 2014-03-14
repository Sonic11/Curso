def suma(operacion, sumar):

	numero1 = int(raw_input('Primer Numero:'))
	numero2 = int(raw_input('Segundo Numero:'))

	print "Escoje una Operacion"

	operacion = raw_input('Elige una Operacion:')

	if operacion == 'Suma':

		sumar = numero1 + numero2

		print 'El Resultado es:', sumar

	operacion, sumar = suma(operacion, sumar)