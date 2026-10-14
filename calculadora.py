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


historial = ""
resultado = None
operacion = ""


def guardar_historial(funcion):
    def nueva_funcion(a, b):
        global historial, resultado, operacion

        nuevo_resultado = funcion(a, b)

        historial += str(resultado) + "~" + operacion + "|"

        if funcion.__name__ == "suma":
            simbolo = "+"
        elif funcion.__name__ == "resta":
            simbolo = "-"
        elif funcion.__name__ == "multiplicar":
            simbolo = "*"
        else:
            simbolo = "/"

        operacion = "(" + operacion + " " + simbolo + " " + str(b) + ")"
        resultado = nuevo_resultado

        return resultado

    return nueva_funcion


suma = guardar_historial(suma)
resta = guardar_historial(resta)
multiplicar = guardar_historial(multiplicar)
dividir = guardar_historial(dividir)


def volver_atras():
    global historial, resultado, operacion

    if historial == "":
        print("No hay ninguna operación anterior.")
        return

    historial = historial[:-1]

    posicion = historial.rfind("|")

    if posicion == -1:
        paso = historial
        historial = ""
    else:
        paso = historial[posicion + 1:]
        historial = historial[:posicion + 1]

    separador = paso.find("~")

    resultado = float(paso[:separador])
    operacion = paso[separador + 1:]

    print("Has vuelto al paso anterior.")
    print(operacion, "=", resultado)


def pedir_eleccion():
    while True:
        try:
            eleccion = int(input("""
Bienvenido a la calculadora.

Opción 1: Suma
Opción 2: Resta
Opción 3: Multiplicar
Opción 4: División
Opción 5: Volver atrás
Opción 6: Salir

Elige qué operación realizar: """))

            if 1 <= eleccion <= 6:
                return eleccion

            print("Error: elige una opción del 1 al 6.")

        except ValueError:
            print("Error: debes introducir un número.")


eleccion = pedir_eleccion()

while eleccion != 6:

    if eleccion in (1, 2, 3, 4):

        if resultado is None:
            resultado = pedir_numero("Dime el primer número: ")
            operacion = str(resultado)

        num1 = resultado
        num2 = pedir_numero("Dime el segundo número: ")

        try:
            if eleccion == 1:
                resultado = suma(num1, num2)

            elif eleccion == 2:
                resultado = resta(num1, num2)

            elif eleccion == 3:
                resultado = multiplicar(num1, num2)

            elif eleccion == 4:
                resultado = dividir(num1, num2)

            print(operacion, "=", resultado)

        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")

    elif eleccion == 5:
        volver_atras()

    eleccion = pedir_eleccion()


print("Gracias por usar la calculadora.")

