import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Programa Analizador de Datos")

st.title("Análisis de Factores de Rendimiento Estudiantil")

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)

# Intentar cargar el archivo CSV
try:
    data = pd.read_csv(file_path)
    
    # Limpiar el DataFrame eliminando valores nulos
    df_limpio = data.dropna()
    
    # Mostrar el DataFrame limpio en la aplicación
    st.subheader("DataFrame limpio")
    st.write(df_limpio)
    
    # Mostrar un resumen estadístico de los datos
    st.subheader("Resumen estadístico de los datos")
    resumen = df_limpio.describe()
    st.write(resumen)
    
    # Seleccionar la columna para graficar
    st.subheader("Selecciona una columna para graficar")
    columnas_numericas = df_limpio.select_dtypes(include='number').columns.tolist()
    
    if columnas_numericas:
        columna_seleccionada = st.selectbox("Elige una columna:", columnas_numericas)
        
        # Visualización de la columna seleccionada
        st.subheader(f"Gráfico de la columna: {columna_seleccionada}")
        
        fig, ax = plt.subplots()
        sns.histplot(df_limpio[columna_seleccionada], ax=ax, kde=True)  # Gráfico de histograma con KDE
        st.pyplot(fig)
    else:
        st.write("No hay columnas numéricas para graficar.")
        
except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta especificada: {file_path}")
