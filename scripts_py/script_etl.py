# script_etl.py

import pandas as pd
import pyodbc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

def realizar_etl():
    pyodbc_conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-S5RTQ3ET\\SQLEXPRESS;"
        "DATABASE=SQL tutorial;"
        "Trusted_Connection=yes;"
    )

    engine = create_engine("mssql+pyodbc://", creator=lambda: pyodbc.connect(pyodbc_conn_str))
    meta = MetaData(bind=engine)

    table_1 = Table('Table_1', meta, autoload=True)

    query = table_1.select()
    result = engine.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

    df['EdadDuplicada'] = df['Edad'] * 3

    # Identificar correos sin "@" y crear nueva columna
    df['CorreoNuevo'] = df.apply(lambda row: row['CorreoElectronico'] + '@gmail.com' if '@' 
                                not in row['CorreoElectronico'] else row['CorreoElectronico'], axis=1)
    print("DataFrame después de la transformación:")
    print(df)

    table_tr = Table('table_tr', meta,
                    Column('ID', Integer, primary_key=True),
                    Column('Nombre', String(50)),
                    Column('Edad', Integer),
                    Column('CorreoElectronico', String(100)),
                    Column('EdadDuplicada', Integer),
                    )

    table_tr.create(checkfirst=True)

    df.to_sql('table_tr', engine, index=False, if_exists='replace', schema='dbo')

    print("Proceso ETL completado con éxito.")

# Llamar a la función si se ejecuta el script directamente
if __name__ == "__main__":
    realizar_etl()
    