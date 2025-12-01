import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# ---------------------------------------------------------------------
# Configuración inicial
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="California Housing Explorer",
    page_icon="🏠",
    layout="wide")

st.title("🏠 Análisis Interactivo – California Housing")
st.caption("Proyecto de análisis de datos con Streamlit.")
st.markdown("---")

# ---------------------------------------------------------------------
# Diccionario de variables
# ---------------------------------------------------------------------
st.subheader("📘 Diccionario de variables del dataset")

features_info = {
    "HouseAge": "Mediana de la edad de las casas dentro del grupo de bloques.",
    "AveRooms": "Promedio de habitaciones por hogar.",
    "AveBedrms": "Promedio de dormitorios por hogar.",
    "Population": "Población del grupo de bloques.",
    "Latitude": "Latitud del centro geográfico del grupo de bloques.",
    "Longitude": "Longitud del centro geográfico del grupo de bloques.",
    "MedHouseVal (Target)": "Mediana del valor de la vivienda (cientos de miles USD)."}

df_diccionario = pd.DataFrame(
    list(features_info.items()),
    columns=["Característica", "Descripción"])

st.dataframe(df_diccionario)
st.markdown("---")

# ---------------------------------------------------------------------
# Fase 1: Carga y Preparación
# ---------------------------------------------------------------------
st.subheader("Fase 1: Carga y Preparación de Datos")

housing = fetch_california_housing()

df_california = pd.DataFrame(housing.data, columns=housing.feature_names)
df_california["MedHouseVal"] = housing.target

st.markdown("**Primeras 5 filas del DataFrame**")
st.dataframe(df_california.head())

st.markdown("**Tipos de datos por columna**")
st.write(df_california.dtypes)

st.markdown("**Valores faltantes por columna**")
st.write(df_california.isna().sum())

st.markdown("---")

# ---------------------------------------------------------------------
# Fase 2: Análisis Interactivo
# ---------------------------------------------------------------------
st.subheader("Fase 2: Análisis Descriptivo Interactivo")

st.sidebar.markdown("## 🎛 Controles de Filtrado")
st.sidebar.markdown(
    "Ajustá el rango de **HouseAge** y la **Latitud mínima** para "
    "explorar el valor de la vivienda (**MedHouseVal**).")

houseage_min = float(df_california["HouseAge"].min())
houseage_max = float(df_california["HouseAge"].max())

houseage_range = st.sidebar.slider(
    "Rango de HouseAge",
    min_value=houseage_min,
    max_value=houseage_max,
    value=(houseage_min, houseage_max))

lat_min_user = st.sidebar.number_input(
    "Latitud mínima",
    min_value=float(df_california["Latitude"].min()),
    max_value=float(df_california["Latitude"].max()),
    value=float(df_california["Latitude"].min()))

df_filtrado = df_california[
    (df_california["HouseAge"] >= houseage_range[0]) &
    (df_california["HouseAge"] <= houseage_range[1]) &
    (df_california["Latitude"] >= lat_min_user)].copy()

st.markdown(f"**Registros filtrados:** {df_filtrado.shape[0]}")

# Resumen del target
st.markdown("### Resumen de MedHouseVal")

med_series = df_filtrado["MedHouseVal"]

st.write(f"**Mediana:** {med_series.median():.3f}")
st.write(f"**Rango:** {(med_series.max() - med_series.min()):.3f}")
st.write(f"**Media:** {med_series.mean():.3f}")
st.write(f"**Desvío estándar:** {med_series.std():.3f}")

# ---------------------------------------------------------------------
# Fase 3: Visualización
# ---------------------------------------------------------------------
st.subheader("Fase 3: Visualización Dinámica")

st.markdown(
    "Exploramos visualmente la relación entre variables usando los "
    "datos filtrados.")

columnas_numericas = df_filtrado.select_dtypes(
    include="float64").columns.tolist()

# ---------------------------------------------------------------------
# Histograma
# ---------------------------------------------------------------------
st.markdown("### 📊 Distribución de una variable")

columna_hist = st.selectbox(
    "Elegí la columna:",
    options=columnas_numericas,
    index=columnas_numericas.index("MedHouseVal"))

fig_hist, ax_hist = plt.subplots()
ax_hist.hist(df_filtrado[columna_hist], bins=30, color="skyblue")
ax_hist.set_xlabel(columna_hist)
ax_hist.set_ylabel("Frecuencia")
ax_hist.set_title(f"Distribución de {columna_hist}")

st.pyplot(fig_hist)

# ---------------------------------------------------------------------
# Scatter Plot
# ---------------------------------------------------------------------
st.markdown("### 📈 Relación entre dos variables")

col1, col2 = st.columns(2)

with col1:
    columna_x = st.selectbox(
        "Eje X:",
        options=columnas_numericas,
        index=columnas_numericas.index("HouseAge"))

with col2:
    columna_y = st.selectbox(
        "Eje Y:",
        options=columnas_numericas,
        index=columnas_numericas.index("MedHouseVal"))

fig_scatter, ax_scatter = plt.subplots()
ax_scatter.scatter(
    df_filtrado[columna_x],
    df_filtrado[columna_y],
    alpha=0.5,
    color="blue")

ax_scatter.set_xlabel(columna_x)
ax_scatter.set_ylabel(columna_y)
ax_scatter.set_title(f"{columna_x} vs {columna_y}")

st.pyplot(fig_scatter)





