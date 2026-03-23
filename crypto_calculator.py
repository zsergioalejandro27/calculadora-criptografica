# =========================
# IMPORTS
# =========================
import hashlib
import base64
import random
import math

# =========================
# UTILIDADES
# =========================

def pausar():
    input("\nPresiona ENTER para continuar...")

def limpiar():
    print("\n" * 50)

# =========================
# MENÚ PRINCIPAL
# =========================

def menu_principal():
    while True:
        limpiar()
        print("===== CRYPTO CALCULATOR =====")
        print("1. Matemática modular")
        print("2. Criptografía clásica")
        print("3. Criptografía moderna")
        print("4. Algoritmos hash")
        print("5. Codificación")
        print("6. SALT")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            menu_matematica_modular()
        elif opcion == "2":
            menu_criptografia_clasica()
        elif opcion == "3":
            print("En construcción...")
            pausar()
        elif opcion == "4":
            print("En construcción...")
            pausar()
        elif opcion == "5":
            print("En construcción...")
            pausar()
        elif opcion == "6":
            print("En construcción...")
            pausar()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
            pausar()

# =========================
# MENÚ MATEMÁTICA MODULAR
# =========================

def menu_matematica_modular():
    while True:
        limpiar()
        print("=== MATEMÁTICA MODULAR ===")
        print("1. Calcular a mod n")
        print("2. Inverso aditivo")
        print("3. Inverso XOR")
        print("4. MCD")
        print("5. Inverso multiplicativo (básico)")
        print("6. Inverso multiplicativo (Euclides Extendido)")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            calcular_modulo()
        elif opcion == "2":
            inverso_aditivo()
        elif opcion == "3":
            inverso_xor()
        elif opcion == "4":
            calcular_mcd()
        elif opcion == "5":
            inverso_multiplicativo_basico()
        elif opcion == "6":
            euclides_extendido()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")
            pausar()

# =========================
# MENÚ CRIPTOGRAFÍA CLÁSICA
# =========================

def menu_criptografia_clasica():
    while True:
        limpiar()
        print("=== CRIPTOGRAFÍA CLÁSICA ===")
        print("1. Cifrado Módulo 27")
        print("2. Cifrado César")
        print("3. Cifrado Vernam (XOR)")
        print("4. Cifrado ATBASH")
        print("5. Transposición columnar simple")
        print("6. Cifrado Afín")
        print("7. Sustitución simple")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cifrado_mod27()
        elif opcion == "2":
            cifrado_cesar()
        elif opcion == "3":
            cifrado_vernam()
        elif opcion == "4":
            cifrado_atbash()
        elif opcion == "5":
            transposicion_columnar()
        elif opcion == "6":
            cifrado_afin()
        elif opcion == "7":
            sustitucion_simple()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")
            pausar()

# =============================
# FUNCIONES MATEMÁTICA MODULAR
# =============================

def calcular_modulo():
    try:
        a = int(input("Ingrese el número a: "))
        n = int(input("Ingrese el módulo n: "))

        resultado = a % n

        print(f"\nResultado: {a} mod {n} = {resultado}")

    except:
        print("Error: entrada inválida")

    pausar()


def inverso_aditivo():
    try:
        a = int(input("Ingrese el número a: "))
        n = int(input("Ingrese el módulo n: "))

        inverso = (-a) % n

        print(f"\nEl inverso aditivo de {a} mod {n} es: {inverso}")

    except:
        print("Error: entrada inválida")

    pausar()


def inverso_xor():
    try:
        a = int(input("Ingrese el valor original: "))
        clave = int(input("Ingrese la clave XOR: "))

        cifrado = a ^ clave
        descifrado = cifrado ^ clave

        print(f"\nValor cifrado: {cifrado}")
        print(f"Valor recuperado (inverso XOR): {descifrado}")

    except:
        print("Error: entrada inválida")

    pausar()


def calcular_mcd():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        original_a = a
        original_b = b

        while b != 0:
            a, b = b, a % b

        print(f"\nEl MCD de {original_a} y {original_b} es: {a}")

        if a == 1:
            print("Sí existe inverso multiplicativo (son coprimos)")
        else:
            print("No existe inverso multiplicativo")

    except:
        print("Error: entrada inválida")

    pausar()


def inverso_multiplicativo_basico():
    try:
        a = int(input("Ingrese el número a: "))
        n = int(input("Ingrese el módulo n: "))

        inverso = None

        for x in range(1, n):
            if (a * x) % n == 1:
                inverso = x
                break

        if inverso is not None:
            print(f"\nEl inverso multiplicativo de {a} mod {n} es: {inverso}")
        else:
            print("\nNo existe inverso multiplicativo")

    except:
        print("Error: entrada inválida")

    pausar()

def euclides_extendido():
    try:
        a = int(input("Ingrese el número a: "))
        n = int(input("Ingrese el módulo n: "))

        r1, r2 = n, a
        t1, t2 = 0, 1

        print("\nTabla del algoritmo:")
        print("r1\tr2\tq\tt1\tt2")

        rondas = 0

        while r2 != 0:
            q = r1 // r2

            print(f"{r1}\t{r2}\t{q}\t{t1}\t{t2}")

            r1, r2 = r2, r1 - q * r2
            t1, t2 = t2, t1 - q * t2

            rondas += 1

        print(f"\nTotal de rondas: {rondas}")

        if r1 == 1:
            inverso = t1 % n
            print(f"Inverso multiplicativo: {inverso}")
        else:
            print("No existe inverso multiplicativo")

    except:
        print("Error: entrada inválida")

    pausar()

# ===============================
# FUNCIONES CRIPTOGRAFÍA CLÁSICA
# ===============================

def cifrado_mod27():
    texto = input("Ingrese el texto: ").lower()

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            valor = ord(letra) - 97
            cifrado = (valor % 27)
            resultado += chr(cifrado + 97)
        else:
            resultado += letra

    print(f"\nResultado: {resultado}")
    pausar()

def cifrado_cesar():
    texto = input("Ingrese el texto: ").lower()
    desplazamiento = int(input("Ingrese el desplazamiento: "))

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            valor = ord(letra) - 97
            cifrado = (valor + desplazamiento) % 26
            resultado += chr(cifrado + 97)
        else:
            resultado += letra

    print(f"\nTexto cifrado: {resultado}")
    pausar()

def cifrado_vernam():
    texto = input("Ingrese el texto: ")
    clave = input("Ingrese la clave: ")

    resultado = ""

    for i in range(len(texto)):
        t = ord(texto[i])
        k = ord(clave[i % len(clave)])
        resultado += chr(t ^ k)

    print(f"\nTexto cifrado: {resultado}")
    pausar()

def cifrado_atbash():
    texto = input("Ingrese el texto: ").lower()

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            resultado += chr(122 - (ord(letra) - 97))
        else:
            resultado += letra

    print(f"\nResultado: {resultado}")
    pausar()

def transposicion_columnar():
    texto = input("Ingrese el texto: ").replace(" ", "")
    columnas = int(input("Número de columnas: "))

    filas = (len(texto) + columnas - 1) // columnas

    matriz = []

    for i in range(filas):
        fila = texto[i*columnas:(i+1)*columnas]
        matriz.append(fila)

    resultado = ""

    for col in range(columnas):
        for fila in matriz:
            if col < len(fila):
                resultado += fila[col]

    print(f"\nTexto cifrado: {resultado}")
    pausar()

def cifrado_afin():
    texto = input("Ingrese el texto: ").lower()
    a = int(input("Ingrese valor de a: "))
    b = int(input("Ingrese valor de b: "))

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            x = ord(letra) - 97
            cifrado = (a * x + b) % 26
            resultado += chr(cifrado + 97)
        else:
            resultado += letra

    print(f"\nTexto cifrado: {resultado}")
    pausar()

def sustitucion_simple():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    clave = input("Ingrese alfabeto de sustitución (26 letras): ").lower()

    texto = input("Ingrese el texto: ").lower()

    resultado = ""

    for letra in texto:
        if letra.isalpha():
            indice = alfabeto.index(letra)
            resultado += clave[indice]
        else:
            resultado += letra

    print(f"\nTexto cifrado: {resultado}")
    pausar()


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    menu_principal()