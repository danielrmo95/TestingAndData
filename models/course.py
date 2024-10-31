from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

meta = MetaData()

# Definición de la tabla Cursos
cursos = Table(
    "Cursos", meta,
    Column("curso_id", Integer, primary_key=True, autoincrement=True),
    Column("nombre_curso", String(100), nullable=False),
    Column("descripcion", String(255), nullable=True),
    Column("instructor", String(100), nullable=False),
    Column("entidad_id", Integer, ForeignKey("EntidadesEducativas.entidad_id"), nullable=False),  # Llave foránea con EntidadesEducativas
)

# Ajuste de la clase CursoModel de acuerdo con la estructura de la tabla
class CursoModel:
    def __init__(self, curso_id, nombre_curso, descripcion, instructor, entidad_id):
        self.curso_id = curso_id
        self.nombre_curso = nombre_curso
        self.descripcion = descripcion
        self.instructor = instructor
        self.entidad_id = entidad_id

    def dict(self):
        return {
            "curso_id": self.curso_id,
            "nombre_curso": self.nombre_curso,
            "descripcion": self.descripcion,
            "instructor": self.instructor,
            "entidad_id": self.entidad_id,
        }