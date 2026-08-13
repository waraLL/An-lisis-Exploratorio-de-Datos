# Análisis Exploratorio de Datos: Predicción de Salud de Baterías

## Descripción del proyecto

Este proyecto presenta un flujo completo de análisis y procesamiento de datos aplicado a un conjunto de datos de baterías.

Su función principal es demostrar las etapas fundamentales de un proyecto de ciencia de datos: generación de datos con errores, limpieza, análisis exploratorio (EDA), construcción de un modelo predictivo para estimar el estado de salud de una batería y la elaboración de un dashboard para visualizar de forma práctica la información que se tenia.

El proyecto fue desarrollado utilizando Python y sus principales librerías para análisis de datos, visualización y modelado.

## Objetivos
  - Aplicar técnicas de limpieza y preparación de datos
  - Identificar y corregir valores inconsistentes
  - Analizar patrones y relaciones entre variables
  - Realizar visualizaciones para comprender el comportamiento de los datos
  - Construir un modelo predictivo basado en las características de la batería
  - Elaborar un dashboard para facilitar la exploración de los resultados

## Etapas del proyecto

El proyecto se desarrolló en diferentes etapas:

1. **Generación de errores:** incorporación de valores inconsistentes para simular problemas presentes en datos reales
2. **Limpieza de datos:** detección y tratamiento de valores nulos, datos inconsistentes y valores atípicos
3. **Análisis exploratorio:** análisis estadístico y visualización de las principales variables
4. **Modelo predictivo:** comparación de diferentes modelos para estimar la salud de la batería
5. **Dashboard interactivo:** desarrollo de una aplicación con Streamlit y Plotly para explorar los resultados

## Dataset
El conjunto de datos contiene información relacionada con el uso y rendimiento de baterías. Este dataset fue extraído de: https://www.kaggle.com/datasets/dharmendrapandit12/laptop-battery-health-dataset

Principales variables:
  - Edad de batería
  - Horas de uso diario
  - Usuario gamer
  - Capacidad de diseño
  - Ciclos de carga
  - Uso de CPU y GPU
  - Consumo energético
  - Temperatura promedio
  - Capacidad de carga completa
  - Salud de batería
Este dataset lleva por nombre: battery_health_dataset.csv

## Herramientas utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Dashboard interactivo

El proyecto incluye un dashboard desarrollado con Streamlit y Plotly que permite explorar de forma interactiva la información de las baterías. Entre las funcionalidades se incluyen:
- Indicadores principales
- Distribución de la salud de las baterías
- Relación entre edad y salud
- Relación entre ciclos de carga y salud
- Capacidad retenida
- Clasificación de baterías según su nivel de salud
- Filtros interactivos

## Notebooks

| Notebook | Descripción |
|---|---|
| `00_Agregar_Errores.ipynb` | Generación de errores e inconsistencias en los datos |
| `01_Limpieza_de_datos.ipynb` | Limpieza, corrección e imputación de datos |
| `02_Analisis_exploratorio_EDA.ipynb` | Estadística descriptiva y análisis visual |
| `03_Modelo_predictivo.ipynb` | Entrenamiento y comparación de modelos predictivos |
| `04_Dashboard_y_Visualizacion.ipynb` | Visualizaciones interactivas con Plotly |

## Principales hallazgos

Durante el análisis exploratorio se observaron relaciones importantes entre la salud de la batería y variables relacionadas con su antigüedad y uso.
Las variables que mostrron una mayor relación con `Salud_Bateria` fueron:
- `Ciclos_Carga`
- `Edad_Bateria`
- `Capacidad_Carga_Completa`

El análisis también permitió identificar valores faltantes, valores atípicos e inconsistencias que fueron tratados durante la etapa de limpieza.

## Autor
*Ing. Wara López L.*

Proyecto desarrollado como parte del aprendizaje y aplicación práctica de técnicas de análisis de datos.
