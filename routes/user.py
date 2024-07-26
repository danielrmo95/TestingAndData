from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, HTTPException
from models.user import users,UserModel
from config.db import engine
from schema.user import UserResponse
from sqlalchemy import Row
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_users():
    try:
        db = SessionLocal()
        query = users.select()
        result = db.execute(query).fetchall()
        users_list = [UserModel(*row).dict() for row in result]
        return users_list
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e

    finally:
        db.close()

def get_user_by_id(user_id: int):
    try:
        db = SessionLocal()
        query = users.select().where(users.c.id == user_id)
        result = db.execute(query).fetchone()

        if result:
            # Convierte el objeto Row a un diccionario usando _asdict()
            user_dict = result._asdict()
            user_response = UserModel(**user_dict)
            return user_response
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except HTTPException as e:
        raise e

    except Exception as e:
        print(f"Error en get_user_by_id: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

    finally:
        db.close()

def create_user(new_user: UserModel):
    try:
        db = SessionLocal()
        db.execute(users.insert().values(
            Nombre=new_user.Nombre,
            Edad=new_user.Edad,
            CorreoElectronico=new_user.CorreoElectronico
        ))

        db.commit()

        return {"message": "Usuario creado exitosamente"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e

    finally:
        db.close()
