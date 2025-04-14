from models import *
from db import sesion
from sqlmodel import select
from fastapi import APIRouter,HTTPException,status

router = APIRouter(prefix="/users",tags=["Users"])

# Endpoint para obtener todos los usuarios
@router.get("/users/",response_model=list[UserRead],description="Este endpoint devuelve todos los usuarios de la base de datos")
# Nota: no es necesario usar depends ya que en db.py ya lo definimos en la variable sesion
async def get_users(session:sesion):
    return session.exec(select(User)).all()

# Enpoint para obtener usuarios por id
@router.get("/users/{user_id}",response_model=UserRead,description="Este endpoint devuelve un usuario por su id")
async def get_user(user_id:int, session:sesion):
    #user = session.exec(select(User).where(User.id == user_id)).first()
    user = session.get(User,user_id) # Otra forma de obtener el usuario por su id
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Usuario no encontrado")
    return user

# Endpoint para crear usuarios
@router.post("/users/", response_model=UserRead, status_code=status.HTTP_201_CREATED,description="Este endpoint crea un usuario en la base de datos")
async def create_user(user_data:UserCreate, session:sesion):
    user = User(**user_data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Endpoint para eliminar usuarios
@router.delete("/users/{user_id}",status_code =status.HTTP_200_OK, description="Este endpoint elimina un usuario por su id")
async def delete_user(user_id:int, session:sesion):
    user = session.get(User,user_id) # Validmaos la existencia del usuario
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Usuario no encontrado")
    session.delete(user)
    session.commit()
    return {"Message": f"Usuario {user.nombre} eliminado con exito"}

# Endpoint para actualizar usuarios
@router.patch("/users/{user_id}",status_code=status.HTTP_202_ACCEPTED, description="Este endpoint actualiza un usuario por su id")
def update_user(user_id:int,session:sesion, user_data:UserUpdate):
    user = session.get(User,user_id) # Validamos la existencia del usuario
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Usuario no encontrado")
    # Actualizamos los datos
    datos_actualizados = user_data.model_dump(exclude_unset=True)
    user.sqlmodel_update(datos_actualizados)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
