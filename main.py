from fastapi import FastAPI
from routes.user import get_entidades, create_entidad, get_entidad_by_id  # Cambia las importaciones
from schema.user import EntidadEducativa, EntidadEducativaResponse  # Cambia la importación del esquema
from routes.course import get_cursos, create_curso, get_curso_by_id  # Cambia las importaciones para los cursos
from schema.course import Curso, CursoResponse  # Cambia la importación del esquema a curso
from routes.feedback import get_comentarios, create_comentario, get_comentarios_by_id  # Importaciones para los comentarios
from schema.feedback import Comentario,ComentarioResponse  # Importación del esquema de comentarios


app = FastAPI()
## Entidades
@app.get("/getentidades")
def read_entidades():
    return get_entidades()

@app.get("/entidades/{entidad_id}", response_model=EntidadEducativaResponse)  # Cambia el ID a entidad_id
def read_entidad(entidad_id: int):
    return get_entidad_by_id(entidad_id)    

@app.post("/postentidades", response_model=dict)  # Cambia la ruta y el nombre
def create_entidad_route(new_entidad: EntidadEducativa):
    return create_entidad(new_entidad)
## Cursos
@app.get("/getcursos")
def read_cursos():
    return get_cursos()

@app.get("/cursos/{curso_id}", response_model=CursoResponse)  # Cambia el ID a curso_id
def read_curso(curso_id: int):
    return get_curso_by_id(curso_id)

@app.post("/postcursos", response_model=dict)  # Cambia la ruta y el nombre
def create_curso_route(new_curso: Curso):
    return create_curso(new_curso)

##Comentarios

@app.get("/getcomentarios")  # Ruta para obtener comentarios
def read_comentarios():
    return get_comentarios()

@app.get("/comentarios/{comentario_id}", response_model=ComentarioResponse)  # Cambia el ID a comentario_id
def read_comentario(comentario_id: int):
    return get_comentarios_by_id(comentario_id)

@app.post("/postcomentarios", response_model=dict)  # Cambia la ruta y el nombre
def create_comentario_route(new_comentario: Comentario):
    return create_comentario(new_comentario)


