import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

def realizar_analisis():
    # Cadena de conexión a la base de datos
    pyodbc_conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-S5RTQ3ET\\SQLEXPRESS;"  
        "DATABASE=EduFeedback;"  
        "Trusted_Connection=yes;"
    )


    engine = create_engine("mssql+pyodbc://", creator=lambda: pyodbc.connect(pyodbc_conn_str))

    # Consulta SQL sobre la vista
    query = "SELECT * FROM [dbo].[VistaComentarios];"

    # Ejecutar la consulta y obtener el resultado 
    df = pd.read_sql(query, engine)

    #imprimir información de la data
    df.info()
    
    # Mostrar los primeros 5 registros
    print(df)

    # Limpieza
    df2 = df[(df['entidad_nombre'] != 'string') & (df['calificacion'].notnull())]
    
     # exportar data set
    
    df2.to_csv(r'C:\xampp\htdocs\Edufeedback\graficas\dataset.txt', index=False, sep='\t')

    # Agrupar los datos por curso y calcular la media de las calificaciones
    calificaciones_por_curso = df2.groupby('nombre_curso')['calificacion'].mean()
    # Ordenar los cursos por la calificación media de mayor a menor y seleccionar los 5 mejores
    top_5_cursos = calificaciones_por_curso.sort_values(ascending=False).head(5)

    # Imprimir los 5 cursos mejor valorados con su calificación media
    print("Top 5 Cursos Mejor Valorados:")
    print(top_5_cursos)

    # Ruta para guardar las imágenes
    ruta_guardar = "C:\\xampp\\htdocs\\Edufeedback\\graficas"

    # verificar si la carpeta exista
    os.makedirs(ruta_guardar, exist_ok=True)

    # 1. Distribución de las calificaciones
    plt.figure(figsize=(10,6))
    plt.hist(df2['calificacion'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribución de Calificaciones')
    plt.xlabel('Calificación')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    # Guardar la imagen (si ya existe, se reemplaza)
    plt.savefig(os.path.join(ruta_guardar, 'distribucion_calificaciones.png'), dpi=300)
    plt.close()

    # 2. Comentarios por Curso
    comentarios_por_curso = df2['nombre_curso'].value_counts()
    plt.figure(figsize=(10,6))
    comentarios_por_curso.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Número de Comentarios por Curso')
    plt.xlabel('Curso')
    plt.ylabel('Número de Comentarios')
    plt.xticks(rotation=15, ha='right', fontsize=5)
    plt.grid(True)
    # Guardar la imagen (si ya existe, se reemplaza)
    plt.savefig(os.path.join(ruta_guardar, 'comentarios_por_curso.png'), dpi=300)
    plt.close()

    # 3. Comentarios por Entidad Educativa
    comentarios_por_entidad = df2['entidad_nombre'].value_counts()
    plt.figure(figsize=(10,6))
    comentarios_por_entidad.plot(kind='bar', color='salmon', edgecolor='black')
    plt.title('Número de Comentarios por Entidad Educativa')
    plt.xlabel('Entidad Educativa')
    plt.ylabel('Número de Comentarios')
    plt.xticks(rotation=15, ha='right', fontsize=5)
    plt.grid(True)
    # Guardar la imagen (si ya existe, se reemplaza)
    plt.savefig(os.path.join(ruta_guardar, 'comentarios_por_entidad.png'), dpi=300)
    plt.close()

    # 4. Cursos con mejor media de calificación
    plt.figure(figsize=(10,6))
    top_5_cursos.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Top 5 Cursos Mejor Valorados')
    plt.xlabel('Curso')
    plt.ylabel('Calificación Promedio')
    plt.xticks(rotation=15, ha='right', fontsize=7)
    plt.grid(True)
    # Guardar la imagen (si ya existe, se reemplaza)
    plt.savefig(os.path.join(ruta_guardar, 'top_5_cursos.png'), dpi=300)
    plt.close()

# Ejecutar la función
realizar_analisis()
