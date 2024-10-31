from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, HTTPException
from models.feedback import comentarios
from config.db import engine
from schema.feedback import Comentario, ComentarioResponse  # Cambia la importación del esquema
from sqlalchemy import Row

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_comentarios():
    try:
        db = SessionLocal()
        query = comentarios.select()
        result = db.execute(query).fetchall()
        
        comentarios_list = []
        for row in result:
            comentarios_dict = dict (row._mapping)

            if comentarios_dict['fecha_comentario']:
                comentarios_dict['fecha_comentario'] = comentarios_dict['fecha_comentario'].strftime('%Y-%m-%dT%H:%M:%S')
            else:
                comentarios_dict['fecha_comentario'] = None
            comentarios_list.append(ComentarioResponse(**comentarios_dict).dict())

        return comentarios_list
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()

def get_comentarios_by_id(comentario_id: int):
    try:
        db = SessionLocal()
        query = comentarios.select().where(comentarios.c.comentario_id == comentario_id)
        result = db.execute(query).fetchone()

        if result:
            comentarios_dict = dict(result._mapping)

            if comentarios_dict['fecha_comentario']:
                comentarios_dict['fecha_comentario'] = comentarios_dict['fecha_comentario'].strftime('%Y-%m-%dT%H:%M:%S')
            else:
                comentarios_dict['fecha_comentario'] = None
    
            comentarios_response = ComentarioResponse(**comentarios_dict)
            return comentarios_response
        
        else:
            raise HTTPException(status_code=404, detail="No se encuentran comentarios")

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error en get_comentarios_by_id: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        db.close()

def create_comentario(new_comentario: Comentario):
    try:
        db = SessionLocal()
        db.execute(comentarios.insert().values(
            curso_id=new_comentario.curso_id,
            entidad_id=new_comentario.entidad_id,
            comentario=new_comentario.comentario,
            fecha_comentario=new_comentario.fecha_comentario
        ))

        db.commit()

        return {"message": "Comentario creado exitosamente"}

    except Exception as e:
        db.rollback()
        print(f"Error en create_comentario: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()
