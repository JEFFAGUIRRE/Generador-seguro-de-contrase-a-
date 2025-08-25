import string
import secrets

# Diccionario con tipos de caracteres
tipos_caracteres = {
    "minusculas": string.ascii_lowercase,
    "mayusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos": string.punctuation
}

# Lista para almacenar las contraseñas generadas
historial_contrasenas = []

def generar_contrasena(longitud, usar_simbolos=True):
    # Verificación de longitud mínima
    if longitud < 8:
        print("⚠ La longitud mínima recomendada es de 8 caracteres.")
        return None

    # Construir conjunto de caracteres
    caracteres = tipos_caracteres["minusculas"] + tipos_caracteres["mayusculas"] + tipos_caracteres["numeros"]
    if usar_simbolos:
        caracteres += tipos_caracteres["simbolos"]

    # Garantizar al menos un carácter de cada tipo
    contrasena = [
        secrets.choice(tipos_caracteres["minusculas"]),
        secrets.choice(tipos_caracteres["mayusculas"]),
        secrets.choice(tipos_caracteres["numeros"])
    ]
    if usar_simbolos:
        contrasena.append(secrets.choice(tipos_caracteres["simbolos"]))

    # Completar la contraseña con caracteres aleatorios
    while len(contrasena) < longitud:
        contrasena.append(secrets.choice(caracteres))

    # Mezclar los caracteres de forma segura
    secrets.SystemRandom().shuffle(contrasena)
    contrasena_final = ''.join(contrasena)

    # Guardar en historial
    historial_contrasenas.append(contrasena_final)

    return contrasena_final


def main():
    print("=== GENERADOR DE CONTRASEÑAS SEGURAS ===")

    # Mostrar el diccionario de caracteres
    print("\nDiccionario de tipos de caracteres:")
    for clave, valor in tipos_caracteres.items():
        print(f"{clave}: {valor}")

    try:
        longitud = int(input("\nIngrese la longitud de la contraseña: "))
    except ValueError:
        print("⚠ Error: Por favor, ingrese un número válido.")
        return

    if longitud < 8:
        print("⚠ La longitud mínima recomendada es de 8 caracteres.")
        return

    usar_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

    resultado = generar_contrasena(longitud, usar_simbolos)
    if resultado:
        print(f"\n✅ Contraseña generada: {resultado}")
        print(f"📜 Historial de contraseñas: {historial_contrasenas}")


if __name__ == "__main__":
    # Permite generar varias contraseñas en una sola ejecución
    while True:
        main()
        continuar = input("\n¿Desea generar otra contraseña? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nPrograma finalizado. 👋")
            break

