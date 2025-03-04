numero = in(input("ingrese un numero de tres digitos: "))
if 100 < numero < 999:
centenas= (numero // 100)
decenas= (numero % 100) // 10
unidades= (numero % 10)
numero_invertido= unidades * 100 + decenas * 10 + centenas
print("El numero invertido es:", numero_invertido)