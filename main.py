def saludo():
    nombre_usuario = input("¿cuál es su nombre?: ")
    print(f"saludos {nombre_usuario}, ¿cómo está?")

def contador_numero():
    numero = int(input("escoga el numero: "))
    contador = 0
    while contador < numero:
        contador += 1
        print(contador)

if __name__ == "__main__":
    saludo()
    contador_numero()