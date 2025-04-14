from models import *
from db import sesion
from sqlmodel import select
from fastapi import APIRouter,HTTPException,status

# Definimos nuestra apirouter que es parecido a Fastapi pero para definir routers
router = APIRouter(prefix="/transaction",tags=["Transaction"])


# Endpoint para mostrar todas las transacciones de la base de datos
@router.get("/transaction",response_model=List[TransactionRead],description="Este endpoint devuelve todas las transacciones de la base de datos")
async def get_transaction(session:sesion):
    return session.exec(select(Transaction)).all()

# Endpoint para mostrar transacciones por id
@router.get("/transaction/{transaccion_id}",response_model=TransactionRead,description="Este endpoint devuelve una transaccion por su id")  
async def get_transaction(session:sesion, transaccion_id:int):
    transaccion = session.get(Transaction,transaccion_id)
    if not transaccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Transaccion no encontrada")
    return transaccion

# Endpoint para crear transacciones
@router.post("/transaction",response_model=TransactionRead,status_code=status.HTTP_201_CREATED,description="Este endpoint crea una transaccion en la base de datos")
async def Create_transaction(session:sesion,data:TransactionCreate):
    user = session.get(User, data.user_id) # Validamos que el usuario exista
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Transaccion no encontrada")
    
    # Creamos la transaccion
    transaccion = Transaction(**data.model_dump())
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    return transaccion
    
# Endpoint para eliminar transacciones
@router.delete("/transaction/{transaccion_id}",status_code=status.HTTP_200_OK , description="Este endpoint elimina una transaccion por su id")
async def delete_transaction(session:sesion,transaccion_id:int):
    transaction = session.get(Transaction, transaccion_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Transaccion no encontrada")
    session.delete(transaction)
    session.commit()
    return {"Message": f"Transaccion #{transaction.id} eliminada con exito"}

# Endpoint para actualizar transacciones
@router.patch("/transaction/{transaccion_id}",status_code=status.HTTP_202_ACCEPTED, description="Este endpoint actualiza una transaccion por su id")
async def update_transaction(session:sesion,transaccion_id:int,data:TransactionUpdate):
    transaction = session.get(Transaction, transaccion_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Transaccion no encontrada")
    # desempaquetamos los datos
    update_data = data.model_dump(exclude_unset=True)
    transaction.sqlmodel_update(update_data)
    session.commit()
    session.refresh(transaction)
    return transaction
    