from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()

users = Table(
    "Table_1", meta,
    Column("id", Integer, primary_key=True),
    Column("Nombre", String(50)),
    Column("Edad", Integer),
    Column("CorreoElectronico", String(100))
)

class UserModel:
    def __init__(self, id, Nombre, Edad, CorreoElectronico):
        self.id = id
        self.Nombre = Nombre
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico

    def dict(self): 
        return {
            "id": self.id,
            "Nombre": self.Nombre,
            "Edad": self.Edad,
            "CorreoElectronico": self.CorreoElectronico
        }
    


