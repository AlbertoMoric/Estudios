# Seleccionar solo las columnas numéricas para la matriz de correlación
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns

# Calcular la matriz de correlación
correlation_matrix = data[numerical_columns].corr()

# Visualizar la matriz de correlación con Matplotlib y Streamlit
plt.figure(figsize=(10, 6))  # Ajuste del tamaño para una mejor visualización en Streamlit
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlación de las Columnas Numéricas')

# Usar st.pyplot() para mostrar la figura en Streamlit
st.pyplot(plt.gcf())  # plt.gcf() obtiene la figura actual

# Mostrar la matriz de correlación como tabla con st.dataframe()
st.subheader('Matriz de Correlación como Tabla')
st.dataframe(correlation_matrix)
