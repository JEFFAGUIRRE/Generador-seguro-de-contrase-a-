import string
import secrets

def generar_contrasena(longitud):
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    todos_caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos

    if longitud < 8:
        print("⚠ La longitud mínima recomendada es de 8 caracteres.")
        return None

    contrasena = ''.join(secrets.choice(todos_caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("=== GENERADOR DE CONTRASEÑAS SEGURAS ===")
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
    except ValueError:
        print("⚠ Por favor, ingrese un número válido.")
        return

    resultado = generar_contrasena(longitud)
    if resultado:
        print(f"✅ Contraseña generada: {resultado}")

if __name__ == "__main__":
    main()

