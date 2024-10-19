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

# Cargar el archivo CSV
file_path = 'StudentPerformanceFactors.csv'
data = pd.read_csv(file_path)

df2 = pd.read_csv('datos_universidades.csv')
