import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium  # Asegúrate de instalar esta biblioteca

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)
df2 = pd.read_csv('datos_universidades.csv')
df_limpio = data.dropna()

# Crear el mapa
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Añadir el HeatMap
heat_data = [[row['Latitud'], row['Longitud']] for index, row in df2.iterrows()]
HeatMap(heat_data).add_to(m)

# Mostrar el mapa en Streamlit
st.title("Mapa de Calor de Universidades")
st_folium(m, width=700, height=500)

# Agregar la columna 'Id'
df_limpio['Id'] = range(1, len(df_limpio) + 1)

# Cargar nombres de hombres y mujeres desde archivos de texto
nombres_hombres_df = pd.read_csv('names/male.txt', header=None)
nombres_mujeres_df = pd.read_csv('names/female.txt', header=None)

# Agregar una columna 'Id' a ambos DataFrames
nombres_hombres_df['Id'] = range(1, len(nombres_hombres_df) + 1)
nombres_mujeres_df['Id'] = range(1, len(nombres_mujeres_df) + 1)

# Renombrar la columna 0 a 'Nombre' en ambos DataFrames
nombres_hombres_df.rename(columns={0: 'Nombre'}, inplace=True)
nombres_mujeres_df.rename(columns={0: 'Nombre'}, inplace=True)

# Crear una columna 'Nombre' vacía en df_limpio
df_limpio['Nombre'] = ''

# Realizar la fusión de df_limpio con nombres_hombres_df
df_limpio = pd.merge(df_limpio, nombres_hombres_df[['Id', 'Nombre']], on='Id', how='left', suffixes=('', '_hombre'))

# Realizar la fusión de df_limpio con nombres_mujeres_df
df_limpio = pd.merge(df_limpio, nombres_mujeres_df[['Id', 'Nombre']], on='Id', how='left', suffixes=('', '_mujer'))

df_limpio.loc[df_limpio['Gender'] == 'Male', 'Nombre'] = df_limpio['Nombre_hombre']
df_limpio.loc[df_limpio['Gender'] == 'Female', 'Nombre'] = df_limpio['Nombre_mujer']

df_limpio.drop(columns=['Nombre_hombre', 'Nombre_mujer'], inplace=True)

def buscar_universidades():
    st.title("Sistema de Búsqueda de Universidades")
    st.write("--------------------------------------------------")
    
    # Obtener el nombre del alumnado a través de un input
    alumno = st.text_input("Inserte el nombre del alumnado:")
    
    if alumno:
        if alumno not in df_limpio['Nombre'].values:
            st.warning("El alumno no se encuentra en la base de datos")
            return

        nota_alumno = df_limpio['Exam_Score'][df_limpio['Nombre'] == alumno].values[0]
        st.write(f"El alumno {alumno} tiene una nota de {nota_alumno}")

        buscar_unis = []
        for index, row in df2.iterrows():
            if row['Nota_corte'] <= nota_alumno:
                buscar_unis.append(row)

        if not buscar_unis:
            st.warning("No hay universidades disponibles con la nota de corte requerida.")
            return

        # Crear el mapa
        mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
        
        # Añadir marcadores de universidades al mapa
        for uni in buscar_unis:
            folium.Marker(
                location=[uni['Latitud'], uni['Longitud']],
                popup=uni['Universidad'],
                icon=folium.Icon(color='blue')
            ).add_to(mapa)

        # Mostrar el mapa en Streamlit
        folium_map = mapa._repr_html_()  # Convertir el mapa a HTML
        components.html(folium_map, width=700, height=500)  # Mostrar el mapa en Streamlit

# Llamar a la función en la aplicación Streamlit
    buscar_universidades()
