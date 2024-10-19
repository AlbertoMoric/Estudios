import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Programa Analizador de Datos")

st.title("Análisis de Factores de Rendimiento Estudiantil")

# Cargar el archivo CSV usando Streamlit
uploaded_file = st.file_uploader("Sube el archivo CSV", type="csv")

# Verificar si se ha subido un archivo
if uploaded_file is not None:
    # Cargar el archivo CSV en un DataFrame
    data = pd.read_csv(uploaded_file)
    
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
else:
    st.write("Por favor, sube un archivo CSV para continuar.")
