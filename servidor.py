from flask import Flask, request, jsonify, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DB_NAME = 'usuarios.db'

# Inicializar la base de datos
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL
            )
        ''')
        conn.commit()

# Endpoint: POST /registro
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({'mensaje': 'Usuario y contraseña son obligatorios'}), 400

    contrasena_hash = generate_password_hash(contrasena)

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, contrasena_hash))
            conn.commit()
        return jsonify({'mensaje': f'Usuario {usuario} registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'mensaje': 'El nombre de usuario ya existe'}), 409

# Endpoint: POST /login
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cursor.fetchone()

    if resultado and check_password_hash(resultado[0], contrasena):
        return jsonify({'mensaje': f'Bienvenido, {usuario}'}), 200
    else:
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

# Endpoint: GET /tareas
@app.route('/tareas', methods=['GET'])
def tareas():
    html = """
    <html>
        <head><title>Bienvenida</title></head>
        <body>
            <h1>¡Bienvenido al sistema de tareas!</h1>
            <p>Aquí podrás gestionar tus tareas.</p>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
