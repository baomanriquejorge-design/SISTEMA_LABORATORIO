
import pyodbc
import pandas as pd

# 1. Configuración de conexión
try:
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=Laboratorio;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    print("CONEXION EXITOSA CON SQL SERVER")

    # 2. Consultar la tabla
    consulta = """
    SELECT *
    FROM dbo.Cultivos
    ORDER BY ID;
    """

    datos = pd.read_sql_query(consulta, conexion)

    # 3. Mostrar los resultados
    print("\nDATOS DE LA TABLA CULTIVOS:")
    print(datos.to_string(index=False))

    # 4. Mostrar cantidad de registros
    print("\nTOTAL DE REGISTROS:", len(datos))

    # 5. Cerrar conexión
    conexion.close()

    print("\nCONEXION CERRADA CORRECTAMENTE")

except pyodbc.Error as error:
    print("ERROR DE CONEXION:")
    print(error)
