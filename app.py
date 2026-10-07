from flask import Flask
app = Flask (__name__)
@app.route("/")
def home():
  return "hola este es mi prueba Castillo Campos Mario ALfredo"
