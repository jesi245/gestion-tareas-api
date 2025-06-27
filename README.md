# PFO 2 – Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto consiste en una aplicación cliente-servidor basada en una **API REST creada con Flask**, que permite registrar usuarios, iniciar sesión y visualizar una página de bienvenida.  
Los datos se almacenan de forma segura en una base de datos **SQLite**, utilizando **hashing de contraseñas**.

## Requisitos técnicos

Antes de comenzar, es necesario asegurase de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Ejecutar este comando para instalar las librerías que se utilizan:

         pip install flask werkzeug requests

## Archivos principales
- servidor.py: archivo que contiene el servidor Flask
-cliente.py: cliente en consola para interactuar con la API
- usuarios.db: archivo generado automáticamente con la base de datos SQLite
- README.md: archivo con instrucciones

## Cómo ejecutar el proyecto
Para ejecutar este proyecto seguir estos pasos:

1. Clonar o descargar el proyecto
git clone https://github.com/jesi245/gestion-tareas-api.git
cd gestion-tareas-api

2. Ejecutar el servidor
En una terminal, ejecutar este comando:
      python servidor.py

Se va a ver un mensaje como:  * Running on http://127.0.0.1:5000

 3. Ejecutar el cliente
Abrir otra terminal (en paralelo) y ejecutar este comando: 
      python cliente.py

Se aparecerá el menú:
=== CLIENTE API TAREAS ===
1. Registrar usuario
2. Iniciar sesión
3. Ver página de tareas
4. Salir

## Cómo probar el proyecto
Para probar el funcionamiento dle proyecto se pueden probar las diferentes opciones del menú inicial:

1. Registro de usuario
Elegí la opción 1, ingresá un nombre de usuario y una contraseña.
El cliente enviará un POST /registro al servidor y mostrará la respuesta.

2. Iniciar sesión
Elegí la opción 2 e ingresá los mismos datos.
Si las credenciales son correctas, verás un mensaje tipo "Bienvenido".

3. Ver página de bienvenida
Luego de iniciar sesión, elegí la opción 3.
El sistema te preguntará si querés ver la página en navegador (n) o en consola como texto HTML (c).

Si elegís n, se abrirá la ruta http://127.0.0.1:5000/tareas en el navegador.

Si elegís c, verás el código HTML en la consola.

4. finalmente la opcion 4 permite salir de la app


