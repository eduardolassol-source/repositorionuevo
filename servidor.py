from flask import Flask, send_from_directory
import os

# Crear app
app = Flask(__name__, static_folder='.', static_url_path='')

# Ruta principal (abre index.html)
@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# Servir otros archivos (CSS, JS, imágenes, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# Ejecutar servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)