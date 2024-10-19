import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium  # Asegúrate de instalar esta biblioteca

# Título de la aplicación
st.title("Programa Analizador de Datos")

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)
df2 = pd.read_csv('datos_universidades.csv')

# Instala la biblioteca streamlit_folium si aún no la tienes
# pip install streamlit-folium

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
