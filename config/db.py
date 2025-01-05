import pyodbc
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

# Cargar variables de entorno desde .env
load_dotenv()

# Leer configuraciones desde variables de entorno
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "EduFeedback")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION", "no")

# Crear cadena de conexión en el formato requerido con comillas dobles adicionales
if DB_TRUSTED_CONNECTION.lower() == "yes":
    connection_string = (
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"Trusted_Connection=yes;"
    )
else:
    connection_string = (
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
    )

try:
        pyodbc_conn = pyodbc.connect(connection_string)
        engine = create_engine("mssql+pyodbc://", creator=lambda: pyodbc_conn)
        meta = MetaData()
        print("Conexión exitosa")
        
except Exception as ex:
        print(ex)


