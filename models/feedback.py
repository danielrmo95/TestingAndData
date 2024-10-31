from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, ForeignKey

meta = MetaData()

# Definición de la tabla Comentarios
comentarios = Table(
    "Comentarios", meta,
    Column("comentario_id", Integer, primary_key=True, autoincrement=True),
    Column("curso_id", Integer, ForeignKey("Cursos.curso_id"), nullable=False),  # Relación con Cursos
    Column("entidad_id", Integer, ForeignKey("EntidadesEducativas.entidad_id"), nullable=False),  # Relación con EntidadesEducativas
    Column("comentario", String(500), nullable=False),  # Texto del comentario
    Column("fecha_comentario", DateTime, nullable=False),  # Fecha del comentario
)

class ComentarioModel:
    def __init__(self, comentario_id, curso_id, entidad_id, comentario, fecha_comentario):
        self.comentario_id = comentario_id
        self.curso_id = curso_id
        self.entidad_id = entidad_id
        self.comentario = comentario
        self.fecha_comentario = fecha_comentario

    def dict(self):
        return {
            "comentario_id": self.comentario_id,
            "curso_id": self.curso_id,
            "entidad_id": self.entidad_id,
            "texto": self.comentario,
            "fecha_comentario": self.fecha_comentario,
        }
