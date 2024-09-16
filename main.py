from fastapi import FastAPI #Importa la clase FastAPI de la biblioteca fastapi

app = FastAPI() #Crea una instancia de la clase FastAPI
app.title = 'Mi primera aplicacion de peliculas y analisis de datos'
app.version = '0.0.1'

@app.get('/', tags=['home']) #Define una ruta para la API
def message(): #Define una función de la ruta
    return 'Hello World' #Devuelve un diccionario

