# Proyecto

## Análisis Interactivo de Datos con Streamlit


**Objetivo:** Desarrollar una aplicación interactiva en **Streamlit** que cargue, analice y visualice un conjunto de datos estándar, aplicando conceptos de manipulación de datos con **Pandas** e integración de *widgets* interactivos.



## Dataset Seleccionado: Boston House Prices

Utilizaremos el *dataset* de precios de viviendas de Boston, un conjunto de datos clásico de regresión.

* **Librería de Origen:** `sklearn.datasets`
* **Nombre de la Función:** `sklearn.datasets.load_boston()` (o `fetch_california_housing` si la anterior es deprecada en tu entorno).

### Descripción del Dataset

El *dataset* de Boston contiene información socioeconómica de diferentes áreas de Boston, con el objetivo de predecir el valor mediano de las viviendas.

| Característica | Descripción |
| :--- | :--- |
| **CRIM** | Tasa de criminalidad per cápita por ciudad. |
| **ZN** | Proporción de suelo residencial dividido en lotes de más de 25,000 pies cuadrados. |
| **INDUS** | Proporción de acres de negocios no minoristas por ciudad. |
| **CHAS** | Variable *dummy* del río Charles (= 1 si el tramo limita con el río; 0 en caso contrario). |
| **RM** | Número promedio de habitaciones por vivienda. |
| **LSTAT** | Porcentaje inferior de la población (indicador de menor estatus). |
| **MEDV** (Target) | Valor mediano de las viviendas ocupadas por sus dueños (en miles de \$). |

---

## Actividades Requeridas del Proyecto

El proyecto se dividirá en cuatro fases: 
- Carga y Preparación de Datos (Pandas), 
- Análisis Descriptivo Interactivo (Streamlit), y 
- Visualización Dinámica.
- Despliegue en la Nube

### Fase 1: Carga y Preparación de Datos con Pandas

Deberás cargar el *dataset* desde `sklearn.datasets` y convertirlo en un único **Pandas DataFrame** llamado `df_boston`.

1.  **Carga y Estructura:** Cargar las características (`data`) y la variable objetivo (`target`) y combinarlas en un único `df_boston`. Asignar los nombres de columna correctos usando la lista de características proporcionadas por `load_boston()`.
2.  **Preparación Inicial (Pandas):**
    * Verificar si hay valores faltantes.
    * Mostrar las **primeras 5 filas** y el **tipo de dato** de cada columna utilizando `st.dataframe()` y `st.write()` en Streamlit.

### Fase 2: Análisis Descriptivo Interactivo (Streamlit Widgets)

Esta fase se centra en usar los *widgets* de Streamlit para permitir al usuario explorar los datos.

1.  **Sidebar de Control (`st.sidebar`):**
    * Implementar un `st.sidebar.markdown()` para el título y descripción de los filtros.
2.  **Filtro de Crimen (`st.slider`):**
    * Crear un **slider** que permita al usuario seleccionar un rango máximo para la tasa de criminalidad (**CRIM**). El rango debe ir desde el valor mínimo hasta el valor máximo de la columna.
    * Aplicar este filtro al DataFrame.
3.  **Filtro de Vecindario (`st.checkbox`):**
    * Crear un **checkbox** (`st.checkbox`) etiquetado como **"Limita con Río Charles (CHAS)"**.
    * Si la casilla está marcada, el DataFrame filtrado debe mostrar solo las entradas donde **CHAS** es igual a 1.
4.  **Resumen Descriptivo:**
    * Mostrar la **media, mediana y desviación estándar** de la columna **MEDV** (Valor Mediano de la Vivienda) del DataFrame resultante después de aplicar todos los filtros.

### Fase 3: Visualización Dinámica

Deberás mostrar la relación entre las variables utilizando gráficos que se actualicen automáticamente con los filtros de la Fase 2.

1.  **Gráfico de Distribución del Target (`st.pyplot` o `st.plotly_chart`):**
    * Crear un **histograma** de la variable objetivo (**MEDV**) utilizando una librería externa (como Matplotlib o Plotly).
    * **Requisito:** El gráfico debe reflejar la distribución de los datos **después** de aplicar los filtros del usuario.
2.  **Gráfico de Dispersión (Regresión):**
    * Crear un **menú desplegable** (`st.selectbox`) en el cuerpo principal de la aplicación para que el usuario pueda seleccionar una de las características (ej. **RM**, **LSTAT**) para el eje X.
    * Crear un **gráfico de dispersión** (scatter plot) que muestre la relación entre la característica seleccionada (eje X) y el valor de la vivienda **MEDV** (eje Y).
    * **Requisito:** Este gráfico también debe actualizarse con los datos filtrados.

---

## Fase 4: Despliegue en la Nube

Deberás preparar tu proyecto para el despliegue.

1.  **Git/GitHub:** Crear un **repositorio público** en GitHub a partir de este template.

2.  **Estructura de Carpeta:**
    * `app.py` (código de Streamlit).
    * `notebooks/practice.ipynb` en este archivo puedes realizar un análisis previo del dataset propuesto
    * `requirements.txt` (listado de dependencias: `streamlit`, `pandas`, `scikit-learn`, `matplotlib` o `plotly`).

3.  **Despliegue:** Desplegar la aplicación final utilizando **Streamlit Community Cloud** (share.streamlit.io).

Deberás entregar: 
- el **enlace a la aplicación desplegada** y 
- el **enlace al repositorio de GitHub**.
