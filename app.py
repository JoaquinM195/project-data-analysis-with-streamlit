import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing


st.set_page_config(
    page_title="California Housing Explorer",
    page_icon="🏠",
    layout="wide")

st.title("🏠 Análisis Interactivo – California Housing")
st.caption("Proyecto de análisis de datos con Streamlit.")
st.markdown("---")

st.subheader("📘 Diccionario de variables del dataset")

features_info = {
    "HouseAge": "Mediana de la edad de las casas dentro del grupo de bloques.",
    "AveRooms": "Promedio de habitaciones por hogar.",
    "AveBedrms": "Promedio de dormitorios por hogar.",
    "Population": "Población del grupo de bloques.",
    "Latitude": "Latitud del centro geográfico del grupo de bloques.",
    "Longitude": "Longitud del centro geográfico del grupo de bloques.",
    "MedHouseVal (Target)": "Mediana del valor de la vivienda (en cientos de miles de dólares)."}

df_diccionario = pd.DataFrame(
    list(features_info.items()),
    columns=["Característica", "Descripción"])

st.dataframe(df_diccionario)

st.markdown("---")

st.subheader("Fase 1: Carga y Preparación de Datos")

housing = fetch_california_housing()

df_california = pd.DataFrame(housing.data, columns=housing.feature_names)
df_california["MedHouseVal"] = housing.target

st.markdown("**Primeras 5 filas del DataFrame (df_california)**")
st.dataframe(df_california.head())

st.markdown("**Tipos de datos por columna**")
st.write(df_california.dtypes)

st.markdown("**Valores faltantes por columna**")
st.write(df_california.isna().sum())

st.markdown("---")

st.subheader("Fase 2: Análisis Descriptivo Interactivo")

st.sidebar.markdown("## 🎛 Controles de Filtrado")
st.sidebar.markdown(
    "Ajustá el rango de **HouseAge** (edad mediana de la casa) "
    "y la **Latitud** (desde 32,54 hasta 41,95) para explorar el valor de la vivienda (**MedHouseVal**)."
)

houseage_min = float(df_california["HouseAge"].min())
houseage_max = float(df_california["HouseAge"].max())

houseage_range = st.sidebar.slider(
    "Rango de la mediana del Valor de la Casa (HouseAge)",
    min_value=houseage_min,
    max_value=houseage_max,
    value=(houseage_min, houseage_max))

st.sidebar.markdown("### Filtro por Latitud mínima")
lat_min_user = st.sidebar.number_input(
    "Latitud mínima",
    min_value=float(df_california["Latitude"].min()),
    max_value=float(df_california["Latitude"].max()),
    value=float(df_california["Latitude"].min()))

df_filtrado = df_california[
    (df_california["HouseAge"] >= houseage_range[0]) &
    (df_california["HouseAge"] <= houseage_range[1]) &
    (df_california["Latitude"] >= lat_min_user)
].copy()

st.markdown(f"**Registros después de aplicar filtros:** {df_filtrado.shape[0]}")

st.markdown("### Resumen de MedHouseVal (Valor de la Vivienda)")

med_series = df_filtrado["MedHouseVal"]

mediana_valor = med_series.median()
rango_valor = med_series.max() - med_series.min()

st.write(f"**Mediana de MedHouseVal:** {mediana_valor:.3f}")
st.write(f"**Rango (Máx - Mín) de MedHouseVal:** {rango_valor:.3f}")


