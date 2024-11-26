from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routes.user import get_entidades, create_entidad, get_entidad_by_id  
from schema.user import EntidadEducativa, EntidadEducativaResponse  
from routes.course import get_cursos, create_curso, get_curso_by_id  
from schema.course import Curso, CursoResponse 
from routes.feedback import get_comentarios, create_comentario, get_comentarios_by_id 
from schema.feedback import Comentario, ComentarioResponse 

app = FastAPI()

# Servir archivos estáticos desde la carpeta "static" (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Ruta para servir el archivo index.html en la raíz
@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("app/static/index.html", "r") as f:
        return f.read()

## Entidades
@app.get("/getentidades")
def read_entidades():
    return get_entidades()

@app.get("/entidades/{entidad_id}", response_model=EntidadEducativaResponse)  
def read_entidad(entidad_id: int):
    return get_entidad_by_id(entidad_id)    

@app.post("/postentidades", response_model=dict)  
def create_entidad_route(new_entidad: EntidadEducativa):
    return create_entidad(new_entidad)

## Cursos
@app.get("/getcursos")
def read_cursos():
    return get_cursos()

@app.get("/cursos/{curso_id}", response_model=CursoResponse)  
def read_curso(curso_id: int):
    return get_curso_by_id(curso_id)

@app.post("/postcursos", response_model=dict)  
def create_curso_route(new_curso: Curso):
    return create_curso(new_curso)

## Comentarios
@app.get("/getcomentarios")  
def read_comentarios():
    return get_comentarios()

@app.get("/comentarios/{comentario_id}", response_model=ComentarioResponse)  
def read_comentario(comentario_id: int):
    return get_comentarios_by_id(comentario_id)

@app.post("/postcomentarios", response_model=dict)  
def create_comentario_route(new_comentario: Comentario):
    return create_comentario(new_comentario)
