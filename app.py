import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Boston Housing Explorer",
    page_icon="🏠",
    layout="wide")

st.title("🏠 Análisis Interactivo – Boston Housing")
st.caption("Proyecto de análisis de datos con Streamlit. ")
st.markdown("---")

st.subheader("📘 Diccionario de variables del dataset")

features_info = {
    "CRIM": "Tasa de criminalidad per cápita por ciudad.",
    "ZN": "Proporción de suelo residencial con lotes > 25.000 pies².",
    "INDUS": "Proporción de acres de negocios no minoristas por ciudad.",
    "CHAS": "Dummy del Río Charles (=1 si limita con el río, 0 en caso contrario).",
    "RM": "Número promedio de habitaciones por vivienda.",
    "LSTAT": "Porcentaje de población con menor estatus socioeconómico.",
    "MEDV (Target)": "Valor mediano de viviendas ocupadas por propietarios (en miles de USD)."}

df_diccionario = pd.DataFrame(
    list(features_info.items()),
    columns=["Característica", "Descripción"])

st.dataframe(df_diccionario)

st.markdown("---")

st.subheader("Fase 1: Carga y Preparación de Datos")

url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df_boston = pd.read_csv(url)

df_boston.columns = df_boston.columns.str.upper()

st.markdown("**Primeras 5 filas del DataFrame (df_boston)**")
st.dataframe(df_boston.head())

st.markdown("**Tipos de datos por columna**")
st.write(df_boston.dtypes)

st.markdown("**Valores faltantes por columna**")
st.write(df_boston.isna().sum())

st.markdown("---")
st.subheader("Fase 2: Análisis Descriptivo Interactivo")

# Sidebar con título y descripción
st.sidebar.markdown("## 🎛 Controles de Filtrado")
st.sidebar.markdown(
    "Ajusta el nivel de **CRIM** (criminalidad) y el filtro de **CHAS** "
    "para analizar cómo varía el valor mediano de vivienda (**MEDV**).")

crim_min = float(df_boston["CRIM"].min())
crim_max = float(df_boston["CRIM"].max())

max_crim = st.sidebar.slider(
    "Filtrar por CRIM (tasa de criminalidad)",
    min_value=crim_min,
    max_value=crim_max,
    value=crim_max)

only_river = st.sidebar.checkbox("Limita con Río Charles (CHAS = 1)")

df_filtrado = df_boston[df_boston["CRIM"] <= max_crim].copy()

if only_river:
    df_filtrado = df_filtrado[df_filtrado["CHAS"] == 1]

st.markdown(f"**Registros después de aplicar filtros:** {df_filtrado.shape[0]}")

st.markdown("### Resumen de MEDV (Valor Mediano de la Vivienda)")

if df_filtrado.empty:
    st.warning("No hay datos con los filtros seleccionados.")
else:
    medv_values = df_filtrado["MEDV"].values

    mean_medv  = medv_values.mean()
    med_medv   = medv_values.mean()
    median_medv = medv_values.mean()
    std_medv   = medv_values.std()

    st.write(f"**Media:** {mean_medv:.2f}")
    st.write(f"**Mediana:** {median_medv:.2f}")
    st.write(f"**Desviación estándar:** {std_medv:.2f}")


