from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)


# Define una ruta para la página principal
@app.route("/")
def Tarea_Python():
    return "¡Proyecto final si el comando CURL funciona!"
	

# Ejecuta la aplicación si este script es el principal
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
    
