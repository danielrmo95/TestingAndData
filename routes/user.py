from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, HTTPException
from models.user import entidades_educativas
from config.db import engine
from schema.user import EntidadEducativa, EntidadEducativaResponse
from sqlalchemy.exc import IntegrityError


router = APIRouter()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
def get_entidades():
    try:
        db = SessionLocal()
        query = entidades_educativas.select()
        result = db.execute(query).fetchall()

        # Crear una lista de entidades usando EntidadEducativaResponse
        entidades_list = []
        for row in result:
            entidad_dict = dict(row._mapping)

            if entidad_dict['fecha_registro']:
                entidad_dict['fecha_registro'] = entidad_dict['fecha_registro'].strftime('%Y-%m-%dT%H:%M:%S')
            else:
                entidad_dict['fecha_registro'] = None
                
            entidades_list.append(EntidadEducativaResponse(**entidad_dict).dict())

        return entidades_list
    except Exception as e:
        print(f"Error en get_entidad: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()

def get_entidad_by_id(entidad_id: int):
    try:
        db = SessionLocal()
        query = entidades_educativas.select().where(entidades_educativas.c.entidad_id == entidad_id)
        result = db.execute(query).fetchone()

        if result:
            entidad_dict = dict(result._mapping)

            if entidad_dict['fecha_registro']:
                entidad_dict['fecha_registro'] = entidad_dict['fecha_registro'].strftime('%Y-%m-%dT%H:%M:%S')
            else:
                entidad_dict['fecha_registro'] = None
    
            entidad_response = EntidadEducativaResponse(**entidad_dict)
            return entidad_response
        
        else:
            raise HTTPException(status_code=404, detail="Entidad no encontrada")

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error en get_entidad_by_id: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        db.close()

def create_entidad(new_entidad: EntidadEducativa):
    try:
        db = SessionLocal()
        db.execute(entidades_educativas.insert().values(
            nombre=new_entidad.nombre,
            email=new_entidad.email,
            contrasena=new_entidad.contrasena,
            nombre_representante=new_entidad.nombre_representante,
            telefono_representante=new_entidad.telefono_representante,
            fecha_registro=new_entidad.fecha_registro
        ))

        db.commit()

        return {"message": "Entidad creada exitosamente"}
    
    except IntegrityError as e:
        db.rollback()
        if "UQ__Entidade__AB6E616430625533" in str(e.orig):  # Asegúrate de que esto coincide con el nombre real de tu restricción
            raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso.")

    except Exception as e:
        db.rollback()
        print(f"Exception: {str(e)}")  # Imprimir el error original para depuración
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()
