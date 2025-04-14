from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List

# __________________________ schemas de usuario _____________________________

class Userbase(SQLModel):
    """
    Modelo base para un usuario 
    """
    nombre: str = Field(default=None)
    correo:str = Field(default=None)
    edad: int = Field(default=None)
    telefono: Optional[str] = Field(default="Not contact number")

class UserCreate(Userbase):
    """
    Modelo para crear los usuarios, se usa para mejor entedimiento del proyecto aplicando clean code
    """
    pass

class UserUpdate(SQLModel):
    """
    Modelo para actualizar usuarios 
    """
    nombre:Optional[str]
    correo: Optional[str]
    edad: Optional[int]
    telefono : Optional[str] 
    
class UserRead(Userbase):
    """
    Modelo para mostrar la informacion de un usuario 
    """
    id:int
    transacciones : List["TransactionRead"] = []
    
class User(Userbase, table=True):
    """
    Modelo usado para crear la tabla en base de datos 
    """
    id:int = Field(default=None, primary_key=True)
    transacciones : List["Transaction"] = Relationship(back_populates="user" , cascade_delete=True)

# __________________________ schemas de transacciones _____________________________

class TransactionBase(SQLModel):
    """
    Modelo de una transaccion basica 
    """
    monto : int
    descripcion : str
    
class TransactionCreate(TransactionBase):
    """ 
    Modelo para crear nuevas Transacciones 
    """
    user_id: int

class TransactionRead(TransactionBase):
    """
    Modelo para mostrar la informacion de la transacion 
    """
    id: int

class TransactionUpdate(SQLModel):
    """
    Modelo para actualizar transacciones 
    """
    monto: Optional[int]
    descripcion : Optional[str]
    
class Transaction(TransactionBase,table=True):
    """
    Modelo para la creacion de tablas con relaciones con la tabla usuario 
    """
    id : int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="transacciones")
