# 🧠 PFO 2 – Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto fue desarrollado como parte del Trabajo Práctico Final de la materia **Programación sobre Redes**.  
Consiste en una aplicación cliente-servidor basada en una **API REST creada con Flask**, que permite registrar usuarios, iniciar sesión y visualizar una página de bienvenida.  
Los datos se almacenan de forma segura en una base de datos **SQLite**, utilizando **hashing de contraseñas**.

---

## ⚙️ Requisitos técnicos

Antes de comenzar, asegurate de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Las siguientes librerías:
Ejecutá este comando para instalar las librerías que se utilizan:

pip install flask werkzeug requests

## Archivos principales
servidor.py: archivo que contiene el servidor Flask

cliente.py: cliente en consola para interactuar con la API

usuarios.db: archivo generado automáticamente con la base de datos SQLite

README.md: este archivo con instrucciones

## Cómo ejecutar el proyecto
1. Clonar o descargar el proyecto
git clone https://github.com/tu_usuario/gestion-tareas-api.git
cd gestion-tareas-api

2. Ejecutar el servidor
En una terminal, ejecutá:
python servidor.py

Verás un mensaje como:

 * Running on http://127.0.0.1:5000

 3. Ejecutar el cliente
Abrí otra terminal (en paralelo) y ejecutá: python cliente.py

Aparecerá el menú:
=== CLIENTE API TAREAS ===
1. Registrar usuario
2. Iniciar sesión
3. Ver página de tareas
4. Salir

## Cómo probar el proyecto
Registro de usuario
Elegí la opción 1, ingresá un nombre de usuario y una contraseña.
El cliente enviará un POST /registro al servidor y mostrará la respuesta.

Iniciar sesión
Elegí la opción 2 e ingresá los mismos datos.
Si las credenciales son correctas, verás un mensaje tipo "Bienvenido, jesica".

Ver página de bienvenida
Luego de iniciar sesión, elegí la opción 3.
El sistema te preguntará si querés ver la página en navegador (n) o en consola como texto HTML (c).

Si elegís n, se abrirá la ruta http://127.0.0.1:5000/tareas en tu navegador.

Si elegís c, verás el código HTML en la consola.

finalmente la opcion 4 

