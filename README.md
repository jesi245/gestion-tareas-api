## PFO 2 – Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto consiste en una aplicación cliente-servidor basada en una API REST creada con Flask, que permite registrar usuarios, iniciar sesión y visualizar una página de bienvenida.
Los datos se almacenan de forma segura en una base de datos SQLite, utilizando hashing para proteger las contraseñas, con la librería Werkzeug, que incluye utilidades para hashing de contraseñas (generate_password_hash y check_password_hash).

## Requisitos técnicos
Es necesario tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
Luego, hay que instalar las librerías necesarias con el siguiente comando:
```bash
pip install flask werkzeug requests
```
## Archivos principales
- servidor.py: contiene el servidor Flask.
- cliente.py: cliente en consola para interactuar con la API.
- usuarios.db: base de datos SQLite, se genera automáticamente.
- README.md: instrucciones del proyecto.

## Cómo ejecutar el proyecto

Para ejecutar este proyecto hay que seguir estos pasos:

1. Clonar o descargar el repositorio:
```bash
git clone https://github.com/jesi245/gestion-tareas-api.git
cd gestion-tareas-api
```
2. Ejecutar el servidor (en una terminal):
```bash
python servidor.py
```
Se va a ver un mensaje similar a:
* Running on http://127.0.0.1:5000

3. Ejecutar el cliente (abrir otra terminal paralela):
```bash
python cliente.py
```
Aparecerá el siguiente menú:
=== CLIENTE API TAREAS ===
1. Registrar usuario
2. Iniciar sesión
3. Ver página de tareas
4. Salir

## Cómo probar el proyecto

Se pueden probar las opciones del menú para verificar el funcionamiento:

1. Registrar usuario
La opción 1 permite ingresar un nombre de usuario y una contraseña. El cliente envía una solicitud POST /registro al servidor y muestra la respuesta.

2. Iniciar sesión
La opción 2 solicita las mismas credenciales. Si son correctas, se muestra un mensaje de bienvenida junto al nombre del usuario.

3. Gestión de tareas
La opción 3 permite elegir entre abrir la página de tareas en el navegador (n) o mostrar el código HTML en consola (c).

- En caso de elegir n, se abre la URL http://127.0.0.1:5000/tareas en el navegador.
- En caso de elegir c, se muestra el código HTML directamente en la consola.
Ambas opciones muestran el mismo mensaje "¡Bienvenido al sistema de tareas! Aquí podrás gestionar tus tareas"

4. Salir
La opción 4 finaliza la ejecución del cliente.

