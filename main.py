from fastapi import FastAPI #Importa la clase FastAPI de la biblioteca fastapi
from fastapi.responses import HTMLResponse #Importa la clase HTMLResponse de la biblioteca fastapi.responses
from movies_lis import movies_list

app = FastAPI() #Crea una instancia de la clase FastAPI
app.title = 'Mi primera aplicacion de peliculas y analisis de datos'
app.version = '0.0.1'

@app.get('/', tags=['home']) #Define una ruta para la API
def message(): #Define una función de la ruta
    return HTMLResponse('<h1>Hola mundo</h1>') #Retorna una respuesta HTML

@app.get('/movies', tags=['Movies']) #Definiendo una ruta de la clase FastAPI
def movies():
    return movies_list

@app.get('/movies/{id}', tags=['Movies']) #Definiendo una ruta de la clase FastAPI
def get_movie(id:int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return {}