from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime

meta = MetaData()

# Definición de la tabla EntidadesEducativas
entidades_educativas = Table(
    "EntidadesEducativas", meta,
    Column("entidad_id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(100), nullable=False),
    Column("email", String(100), nullable=False, unique=True),
    Column("contrasena", String(255), nullable=False),
    Column("nombre_representante", String(100), nullable=False),
    Column("telefono_representante", String(15)),
    Column("fecha_registro", DateTime)
)

class EntidadEducativaModel:
    def __init__(self, entidad_id, nombre, email, contrasena, nombre_representante, telefono_representante, fecha_registro):
        self.entidad_id = entidad_id
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena
        self.nombre_representante = nombre_representante
        self.telefono_representante = telefono_representante
        self.fecha_registro = fecha_registro

    def dict(self): 
        return {
            "entidad_id": self.entidad_id,
            "nombre": self.nombre,
            "email": self.email,
            "contrasena": self.contrasena,
            "nombre_representante": self.nombre_representante,
            "telefono_representante": self.telefono_representante,
            "fecha_registro": self.fecha_registro
        }