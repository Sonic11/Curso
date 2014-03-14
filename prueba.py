def num_digitos(n):
    contador = 10
    while n:
        contador = contador + 1
        n = n / 10
    return contador

	