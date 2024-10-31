from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, HTTPException
from models.course import cursos
from config.db import engine
from schema.course import Curso, CursoResponse  # Cambiar a Curso y CursoResponse
from sqlalchemy import Row


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_cursos():
    try:
        db = SessionLocal()
        query = cursos.select()  # Usar la tabla de cursos
        result = db.execute(query).mappings().all()
        cursos_list = [CursoResponse(**row) for row in result]
        
        return cursos_list
    except Exception as e:
        print(f"Error en get_curso: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()

def get_curso_by_id(curso_id: int):
    try:
        db = SessionLocal()
        query = cursos.select().where(cursos.c.curso_id == curso_id)  # Usar curso_id en lugar de entidad_id
        result = db.execute(query).fetchone()

        if result:
            # Convierte el objeto Row a un diccionario usando _asdict()
            curso_dict = result._asdict()
            curso_response = CursoResponse(**curso_dict)
            return curso_response
        else:
            raise HTTPException(status_code=404, detail="Curso no encontrado")

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error en get_curso_by_id: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        db.close()

def create_curso(new_curso: Curso):
    try:
        db = SessionLocal()
        db.execute(cursos.insert().values(  # Usar la tabla de cursos
            nombre_curso=new_curso.nombre_curso,
            descripcion=new_curso.descripcion,
            instructor=new_curso.instructor,
            entidad_id=new_curso.entidad_id  # Suponiendo que hay una relación con entidades educativas
        ))

        db.commit()

        return {"message": "Curso creado exitosamente"}

    except Exception as e:
        db.rollback()
        print(f"Curso: {str(e)}") 
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    finally:
        db.close()
