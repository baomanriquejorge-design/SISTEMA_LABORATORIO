
import streamlit as st
import pyodbc

st.title("Sistema de Microbiología")
st.subheader("Registro de cultivos")

with st.form("registro_cultivo"):
    codigo = st.text_input("Código")
    paciente = st.text_input("Paciente")

    tipo = st.selectbox(
        "Tipo de cultivo",
        ["Urocultivo", "Hemocultivo", "Cultivo de secreción"]
    )

    resultado = st.selectbox(
        "Resultado",
        ["Positivo", "Negativo", "Contaminado", "Pendiente"]
    )

    fecha = st.date_input("Fecha")

    guardar = st.form_submit_button("Guardar registro")

if guardar:
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=Laboratorio;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO dbo.Cultivos
            (Codigo, Paciente, TipoCultivo, Resultado, Fecha)
            VALUES (?, ?, ?, ?, ?)
        """, codigo, paciente, tipo, resultado, fecha)

        conexion.commit()
        conexion.close()

        st.success("¡Registro guardado correctamente!")

    except Exception as error:
        st.error(f"Error: {error}")
