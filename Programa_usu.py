import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Programa Analizador de Datos")

st.title("Análisis de Factores de Rendimiento Estudiantil")

# Ruta del archivo CSV (asegúrate de que esté disponible en tu sistema)
file_path = '/content/drive/MyDrive/Colab Notebooks/Examen/StudentPerformanceFactors.csv'

# Intentar cargar el archivo CSV
try:
    data = pd.read_csv(file_path)
    
    # Limpiar el DataFrame eliminando valores nulos
    df_limpio = data.dropna()
    
    # Mostrar el DataFrame limpio en la aplicación
    st.subheader("DataFrame limpio")
    st.write(df_limpio)
    
    # Visualización básica con Seaborn y Matplotlib
    st.subheader("Visualización de datos")
    
    # Verificar si hay alguna columna numérica para graficar
    if not df_limpio.select_dtypes(include='number').empty:
        fig, ax = plt.subplots()
        sns.histplot(df_limpio.select_dtypes(include='number').iloc[:, 0], ax=ax)
        st.pyplot(fig)
    else:
        st.write("No hay columnas numéricas para graficar.")
except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta especificada: {file_path}")
