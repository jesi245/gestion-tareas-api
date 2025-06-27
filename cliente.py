import requests
import webbrowser

BASE_URL = "http://127.0.0.1:5000"
logueado = False  

def menu():
    global logueado
    while True:
        print("\n=== CLIENTE API TAREAS ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        if logueado:
            print("3. Ver página de tareas")
        print("4. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            logueado = login_usuario()
        elif opcion == "3" and logueado:
            ver_tareas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

def registrar_usuario():
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    datos = {
        "usuario": usuario,
        "contraseña": contrasena
    }
    respuesta = requests.post(f"{BASE_URL}/registro", json=datos)
    print(f"\nEstado: {respuesta.status_code}")
    print("Respuesta:", respuesta.json().get("mensaje"))

def login_usuario():
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    datos = {
        "usuario": usuario,
        "contraseña": contrasena
    }
    respuesta = requests.post(f"{BASE_URL}/login", json=datos)
    print(f"\nEstado: {respuesta.status_code}")
    print("Respuesta:", respuesta.json().get("mensaje"))
    return respuesta.status_code == 200  # True si login fue exitoso

def ver_tareas():
    opcion = input("¿Ver tareas en navegador (n) o en consola como HTML (c)? ")
    if opcion.lower() == 'n':
        webbrowser.open(f"{BASE_URL}/tareas")
    else:
        respuesta = requests.get(f"{BASE_URL}/tareas")
        print(f"\nEstado: {respuesta.status_code}")
        print("Contenido HTML recibido:")
        print(respuesta.text)

if __name__ == "__main__":
    menu()
