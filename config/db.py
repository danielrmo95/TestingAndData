import os
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Leer configuraciones desde variables de entorno
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "EduFeedback")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION", "no")

# Crear cadena de conexión
if DB_TRUSTED_CONNECTION.lower() == "yes":
    connection_string = (
        f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}&Trusted_Connection=yes"
    )
else:
    connection_string = (
        f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}"
    )

try:
    # Crear motor de conexión con SQLAlchemy
    engine = create_engine(connection_string)
    meta = MetaData()
    print("Conexión exitosa")

except Exception as ex:
    print(f"Error al conectar: {ex}")
