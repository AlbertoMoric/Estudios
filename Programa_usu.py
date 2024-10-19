# Programa_usu.py

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
st.subheader('Información del conjunto de datos')
st.write(data.describe())

# Seleccionar solo las columnas numéricas para la matriz de correlación
numerical_columns = df_limpio.select_dtypes(include=['int64', 'float64']).columns

# Calcular la matriz de correlación
correlation_matrix = df_limpio[numerical_columns].corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(6, 3))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix for Numerical Columns')
plt.show()

# Mostrar la matriz de correlación como tabla
print(correlation_matrix)

# Gráfico de ejemplo usando Seaborn
st.subheader('Distribución de un Factor Específico')
factor = st.selectbox('Seleccione un factor para visualizar:', data.columns)

# Crear gráfico usando Seaborn
fig, ax = plt.subplots()
sns.histplot(data[factor], bins=30, kde=True, ax=ax)
ax.set_title(f'Distribución de {factor}')
st.pyplot(fig)

# Mostrar correlaciones
st.subheader('Matriz de correlación')
corr = data.corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
