from sqlmodel import create_engine,Session,SQLModel
from fastapi import Depends,FastAPI
from typing import Annotated
# Definimos la direccion de nuestra base de datos
URL = "sqlite:///./mydb.db"

# creamos la base de datos
engine = create_engine(URL)

# Creamos una funcion para obtener la conexion a la base de datos para cada endpoint
def get_session():
    """
    Funcion para obtener la sesion de la base de datos que se usara para cada endpoint  
    """
    with Session(engine) as session:
        yield session 
        
# Funcion para crear todas las tablas
def create_table(app: FastAPI):
    """
    Funcion para crear todas las tablas de la base de datos 
    """
    SQLModel.metadata.create_all(engine)
    yield
        
# Definimos el tipo de sesion para usar en los endpoints 
# Le ponemos depends para automatizar la inyeccion de dependencias sin necesidad e importarlo en el main.py
sesion = Annotated[Session,Depends(get_session)]