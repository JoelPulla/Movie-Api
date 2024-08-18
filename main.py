from fastapi import FastAPI
from config.db import init_db 
from routes import users

app = FastAPI(
    title= 'MovieAp',
    version= ' 0.0.10',
)

""" Inicializar la base de datos y crear las tablas """
init_db()

""" Rutas """
app.include_router(users.router)



