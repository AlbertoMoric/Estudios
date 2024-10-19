pip install folium
pip install streamlit streamlit-folium

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
