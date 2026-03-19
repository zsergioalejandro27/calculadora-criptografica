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
            print("En construcción...")
            pausar()
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
            print("En construcción...")
            pausar()
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
            break
        else:
            print("Opción inválida")
            pausar()

# =========================
# FUNCIONES MATEMÁTICAS
# =========================

def calcular_modulo():
    try:
        a = int(input("Ingrese el número a: "))
        n = int(input("Ingrese el módulo n: "))

        resultado = a % n

        print(f"\nResultado: {a} mod {n} = {resultado}")

    except:
        print("Error: entrada inválida")

    pausar()

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    menu_principal()