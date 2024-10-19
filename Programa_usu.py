import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Análisis de Factores de Rendimiento Estudiantil')

# Subtítulo
st.write('Este es un análisis exploratorio utilizando datos del rendimiento estudiantil.')

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)

# Mostrar los primeros registros del DataFrame
st.subheader('Vista previa de los datos')
st.write(data.head())

# Mostrar información sobre el DataFrame
st.subheader('Información del conjunto d
