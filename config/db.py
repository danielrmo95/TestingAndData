import pyodbc
from sqlalchemy import create_engine, MetaData

try:
        pyodbc_conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-S5RTQ3ET\\SQLEXPRESS;"
        "DATABASE=SQL tutorial;"
        "Trusted_Connection=yes;"
    )
        pyodbc_conn = pyodbc.connect(pyodbc_conn_str)

        engine = create_engine("mssql+pyodbc://", creator=lambda: pyodbc_conn)
        meta = MetaData()
        print("Conexión exitosa")
        
except Exception as ex:
        print(ex)

