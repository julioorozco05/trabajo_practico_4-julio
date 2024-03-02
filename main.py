def saludo():
    nombre_usuario = input("¿cuál es su nombre?: ")
    print(f"saludos {nombre_usuario}, ¿cómo está?")

def contador_numero():
    numero = int(input("escoga el numero: "))
    contador = 0
    while contador < numero:
        contador += 1
        print(contador)

def calculadora():
    operacion = int(input("escoga la operacion que quiere utilizar: "))
    while operacion > 4:
        print("la operacion no es valida")
        operacion = int(input("escoga la operacion que quiere utilizar: "))

    num_1 = int(input("Elija el valor 1 que quiere utilizar: "))
    num_2 = int(input("Elija el valor 2 que quiere utilizar: "))

    if operacion == 1:
        print("Hará una multplicacion")
        resultado = num_1 * num_2
        print(f"{num_1} x {num_2} = {resultado}")

    if operacion == 2:
        print("Hará una divicion")
        resultado = num_1 / num_2
        print(f"{num_1} / {num_2} = {resultado}")

    if operacion == 3:
        print("Hará una suma")
        resultado = num_1 + num_2
        print(f"{num_1} + {num_2} = {resultado}")

    if operacion == 4:
        print("Hará una resta")
        resultado = num_1 - num_2
        print(f"{num_1} - {num_2} = {resultado}")



if __name__ == "__main__":
    saludo()
    contador_numero()
    calculadora()