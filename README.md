# Practica_Backend_FastAPI

Repositorio para practicar desarrollo backend con FastAPI, enfocado en buenas prácticas, escalabilidad y clean code. Ideal para crear APIs robustas y eficientes.

## Índice

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Creación de Schemas](#creación-de-schemas)
5. [Manejo de Conexiones a la Base de Datos](#manejo-de-conexiones-a-la-base-de-datos)
6. [Configuración de Routers](#configuración-de-routers)
7. [Protección de Rutas](#protección-de-rutas)
8. [Middlewares](#middlewares)
9. [Autenticación con JWT](#autenticación-con-jwt)

## Introducción

El propósito de este proyecto es practicar y aplicar las mejores prácticas en el desarrollo backend de APIs utilizando FastAPI. Aunque el enfoque principal está en FastAPI, muchos de los conceptos y técnicas abordados son transferibles a otros frameworks, lo que lo convierte en una excelente base para construir APIs robustas y eficientes en diversos entornos.

### Diagrama 1

![Apis RESTful](image/Diagrama_Api.jpg)

*Diagrama de funcionamiento basico de una API*


## Requisitos Previos

- Python 3.9+
- FastAPI
- Uvicorn
- SQLModel o SQLAlchemy (para manejo de base de datos)
- Pydantic (para validación de datos)


## Estructura del Proyecto

practica_backend_fastapi/
│
├─ routes/
│  ├─ init.py
│  ├─ transaction_router.py
│  └─ user_routes.py
│
├─ venv/ -> crear entorno virtual
│  ├─ ...
│
├─ .gitignore
├─ db.py
├─ main.py
├─ models.py
├─ mydb.db
├─ README.md
└─ requirements.txt


## Creación de Schemas

[Descripción de cómo crear schemas...]

## Manejo de Conexiones a la Base de Datos

[Descripción del manejo de conexiones...]

## Configuración de Routers

[Descripción de la configuración de routers...]

## Protección de Rutas

[Descripción de la protección de rutas...]

## Middlewares

[Descripción de middlewares...]

## Autenticación con JWT

[Descripción de la autenticación con JWT...]
