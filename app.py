import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing


# ---------------------------------------------------------------------
# Configuración inicial de la página
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="California Housing Explorer",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Análisis Interactivo – California Housing")
st.caption("Proyecto de análisis de datos con Streamlit.")
st.markdown("---")

# ---------------------------------------------------------------------
# Diccionario de variables del dataset
# ---------------------------------------------------------------------
st.subheader("📘 Diccionario de variables del dataset")

features_info = {
    "HouseAge": "Mediana de la edad de las casas dentro del grupo de bloques.",
    "AveRooms": "Promedio de habitaciones por hogar.",
    "AveBedrms": "Promedio de dormitorios por hogar.",
    "Population": "Población del grupo de bloques.",
    "Latitude": "Latitud del centro geográfico del grupo de bloques.",
    "Longitude": "Longitud del centro geográfico del grupo de bloques.",
    "MedHouseVal (Target)": (
        "Mediana del valor de la vivienda "
        "(en cientos de miles de dólares)."
    )
}

df_diccionario = pd.DataFrame(
    list(features_info.items()),
    columns=["Característica", "Descripción"]
)

st.dataframe(df_diccionario)
st.markdown("---")

# ---------------------------------------------------------------------
# Fase 1: Carga y Preparación de Datos
# ---------------------------------------------------------------------
st.subheader("Fase 1: Carga y Preparación de Datos")

housing = fetch_california_housing()

df_california = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)
df_california["MedHouseVal"] = housing.target

st.markdown("**Primeras 5 filas del DataFrame (df_california)**")
st.dataframe(df_california.head())

st.markdown("**Tipos de datos por columna**")
st.write(df_california.dtypes)

st.markdown("**Valores faltantes por columna**")
st.write(df_california.isna().sum())

st.markdown("---")

# ---------------------------------------------------------------------
# Fase 2: Análisis Descriptivo Interactivo
# ---------------------------------------------------------------------
st.subheader("Fase 2: Análisis Descriptivo Interactivo")

st.sidebar.markdown("## 🎛 Controles de Filtrado")
st.sidebar.markdown(
    "Ajustá el rango de **HouseAge** (edad mediana de la casa) y la "
    "**Latitud** (desde 32,54 hasta 41,95) para explorar el valor de "
    "la vivienda (**MedHouseVal**)."
)

houseage_min = float(df_california["HouseAge"].min())
houseage_max = float(df_california["HouseAge"].max())

houseage_range = st.sidebar.slider(
    "Rango de la mediana del Valor de la Casa (HouseAge)",
    min_value=houseage_min,
    max_value=houseage_max,
    value=(houseage_min, houseage_max)
)

st.sidebar.markdown("### Filtro por Latitud mínima")
lat_min_user = st.sidebar.number_input(
    "Latitud mínima",
    min_value=float(df_california["Latitude"].min()),
    max_value=float(df_california["Latitude"].max()),
    value=float(df_california["Latitude"].min())
)

df_filtrado = df_california[
    (df_california["HouseAge"] >= houseage_range[0]) &
    (df_california["HouseAge"] <= houseage_range[1]) &
    (df_california["Latitude"] >= lat_min_user)
].copy()

st.markdown(
    f"**Registros después de aplicar filtros:** "
    f"{df_filtrado.shape[0]}"
)

# Resumen estadístico del target
st.markdown("### Resumen de MedHouseVal (Valor de la Vivienda)")

med_series = df_filtrado["MedHouseVal"]

mediana_valor = med_series.median()
rango_valor = med_series.max() - med_series.min()
media_valor = med_series.mean()
desvio_valor = med_series.std()

st.write(f"**Mediana de MedHouseVal:** {mediana_valor:.3f}")
st.write(f"**Rango (Máx - Mín) de MedHouseVal:** {rango_valor:.3f}")
st.write(f"**Media de MedHouseVal:** {media_valor:.3f}")
st.write(f"**Desvío estándar de MedHouseVal:** {desvio_valor:.3f}")

# ---------------------------------------------------------------------
# Fase 3: Visualización Dinámica
# ---------------------------------------------------------------------
st.subheader("Fase 3: Visualización Dinámica")

st.markdown(
    "En esta fase exploramos visualmente la relación entre las variables "
    "del dataset, siempre utilizando los datos filtrados generados en la Fase 2."
)

# Obtener columnas numéricas para los selectores
columnas_numericas = df_filtrado.select_dtypes(include="float64").columns.tolist()

# ---------------------------------------------------------------------
# Histograma dinámico
# ---------------------------------------------------------------------
st.markdown("### 📊 Distribución de una variable numérica")

columna_hist = st.selectbox(
    "Elegí la columna para el histograma:",
    options=columnas_numericas,
    index=columnas_numericas.index("MedHouseVal")  # por defecto el target
)

fig_hist, ax_hist = plt.subplots()
ax_hist.hist(df_filtrado[columna_hist], bins=30, color="skyblue")

# Etiquetas dinámicas
ax_hist.set_xlabel(columna_hist)
ax_hist.set_ylabel("Frecuencia")
ax_hist.set_title(f"Distribución de {columna_hist} (datos filtrados)")

st.pyplot(fig_hist)

# ---------------------------------------------------------------------
# Scatter dinámico
# ---------------------------------------------------------------------
st.markdown("### 📈 Scatter Plot entre dos variables")

col1, col2 = st.columns(2)

with col1:
    columna_x = st.selectbox(
        "Variable para eje X:",
        options=columnas_numericas,
        index=columnas_numericas.index("HouseAge")
    )

with col2:
    columna_y = st.selectbox(
        "Variable para eje Y:",
        options=columnas_numericas,
        index=columnas_numericas.index("MedHouseVal")
    )

fig_scatter, ax_scatter = plt.subplots()

ax_scatter.scatter(
    df_filtrado[columna_x],
    df_filtrado[columna_y],
    alpha=0.5,
    color="orange"
)

# Etiquetas dinámicas
ax_scatter.set_xlabel(columna_x)
ax_scatter.set_ylabel(columna_y)
ax_scatter.set_title(
    f"Relación entre {columna_x} y {columna_y} (datos filtrados)"
)

st.pyplot(fig_scatter)




