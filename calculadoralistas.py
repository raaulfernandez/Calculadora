def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: debes introducir un número.")

def guardar_historial(funcion):

    def nueva_funcion(a, b):
        resultado = funcion(a, b)
        return resultado

    return nueva_funcion

while True:
    try:
        eleccion = int(input("""Bienvenido a la calculadora, elija una opción (del 1 al 5):
Opción 1: Suma
Opción 2: Resta
Opción 3: Multiplicar
Opción 4: División
Opción 5: Volver Atras
Opción 6: Salir
Elige qué operación realizar: """))

        break

    except ValueError:
        print("Error: debes introducir un número.")


resultado = None
operacion = ""
historial = []


while eleccion != 6:

    if eleccion == 1:
        print("Has elegido la opción Sumar")

        if resultado is None:
            num1 = pedir_numero("Dime el primer número: ")
            operacion = str(num1)
        else:
            num1 = resultado

        num2 = pedir_numero("Dime el segundo número: ")
        historial.append((resultado,operacion))
        
        resultado = suma(num1, num2)
        operacion = "(" + operacion + " + " + str(num2) + ")"

        print(operacion, "=", resultado)

    elif eleccion == 2:
        print("Has elegido la opción Restar")

        if resultado is None:
            num1 = pedir_numero("Dime el primer número: ")
            operacion = str(num1)
        else:
            num1 = resultado

        num2 = pedir_numero("Dime el segundo número: ")
        historial.append((resultado,operacion))

        resultado = resta(num1, num2)
        operacion = "(" + operacion + " - " + str(num2) + ")"

        print(operacion, "=", resultado)

    elif eleccion == 3:
        print("Has elegido la opción de Multiplicar")

        if resultado is None:
            num1 = pedir_numero("Dime el primer número: ")
            operacion = str(num1)
        else:
            num1 = resultado

        num2 = pedir_numero("Dime el segundo número: ")
        historial.append((resultado,operacion))

        resultado = multiplicar(num1, num2)
        operacion = "(" + operacion + " * " + str(num2) + ")"

        print(operacion, "=", resultado)

    elif eleccion == 4:
        print("Has elegido la opción de Dividir")

        if resultado is None:
            num1 = pedir_numero("Dime el primer número: ")
            operacion = str(num1)
        else:
            num1 = resultado

        num2 = pedir_numero("Dime el segundo número: ")
        historial.append((resultado,operacion))

        try:
            resultado = dividir(num1, num2)
            operacion = "(" + operacion + " / " + str(num2) + ")"

            print(operacion, "=", resultado)

        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
    
    elif eleccion == 5:
        if len(historial) > 0:
            resultado, operacion = historial.pop()
            print(operacion, "=", resultado)
            
        else:
            print("No hay ninguna operación anterior.")


    else:
        print("Opción no válida")

    while True:
        try:
            eleccion = int(input("""
Elija otra opción:
1 - Suma
2 - Resta
3 - Multiplicar
4 - División
5 - Volver Atras
6 - Salir
Opción: """))

            break

        except ValueError:
            print("Error: debes introducir un número.")


print("Gracias por usar la calculadora")
