import random

def juego_adivinar():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (1-100): "))
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

if __name__ == "__main__":
    juego_adivinar()