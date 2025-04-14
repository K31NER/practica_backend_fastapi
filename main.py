from routes import user_routes, transaction_routes
from fastapi import FastAPI
from db import create_table

# Iniciamos la aplicacion
app = FastAPI(title="Curso backend con FastAPI", 
            version="1.0",
            lifespan=create_table) # Lifespan es un evento que se ejecuta al iniciar la aplicacion y al cerrarla

# Importamos las rutas de nuestros servicios
app.include_router(user_routes.router) # Rutas de usuarios
app.include_router(transaction_routes.router) # Rutas de transacciones
