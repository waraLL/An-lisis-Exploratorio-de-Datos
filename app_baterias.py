import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN
st.set_page_config(page_title="Dashboard de Baterías",page_icon="🔋",layout="wide")
# TÍTULO
st.title("🔋 Dashboard de Salud de Baterías")
st.write(
    "Exploración interactiva de las características "
    "y salud de las baterías.")
# CARGA DE DATOS
df = pd.read_csv("dataset_limpio_baterias.csv")
# VARIABLES DERIVADAS
df["Capacidad_Retenida"] = (df["Capacidad_Carga_Completa"] /df["Capacidad_Diseño"]) * 100

def clasificar_salud(salud):
    if salud >= 80:
        return "Buena"
    elif salud >= 60:
        return "Regular"
    else:
        return "Baja"

df["Categoria_Salud"] = df["Salud_Bateria"].apply(clasificar_salud)
# FILTROS
st.sidebar.header("🔎 Filtros")

edad_max = st.sidebar.slider(
    "Edad máxima (años)",
    int(df["Edad_Bateria"].min()),
    int(df["Edad_Bateria"].max()),
    int(df["Edad_Bateria"].max())
)

ciclos_max = st.sidebar.slider(
    "Ciclos máximos",
    int(df["Ciclos_Carga"].min()),
    int(df["Ciclos_Carga"].max()),
    int(df["Ciclos_Carga"].max())
)

usuarios = st.sidebar.multiselect(
    "Tipo de usuario",
    options=sorted(df["Usuario_Gamer"].unique()),
    default=sorted(df["Usuario_Gamer"].unique())
)

categorias = st.sidebar.multiselect(
    "Nivel de salud",
    options=["Buena", "Regular", "Baja"],
    default=["Buena", "Regular", "Baja"]
)
# DATAFRAME FILTRADO
df_filtrado = df[
    (df["Edad_Bateria"] <= edad_max) &
    (df["Ciclos_Carga"] <= ciclos_max) &
    (df["Usuario_Gamer"].isin(usuarios)) &
    (df["Categoria_Salud"].isin(categorias))
]
# INDICADORES PRINCIPALES
total_baterias = len(df_filtrado)
salud_promedio = df_filtrado["Salud_Bateria"].mean()
edad_promedio = df_filtrado["Edad_Bateria"].mean()
ciclos_promedio = df_filtrado["Ciclos_Carga"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🔋 Baterías analizadas",total_baterias)
with col2:
    st.metric("❤️ Salud promedio",f"{salud_promedio:.1f}%")
with col3:
    st.metric("⏳ Edad promedio",f"{edad_promedio:.1f} años")
with col4:
    st.metric("🔄 Ciclos promedio",f"{ciclos_promedio:.0f}")
    
# DISTRIBUCIÓN DE SALUD
st.subheader("Distribución de la salud de las baterías")

fig = px.histogram(
    df_filtrado,
    x="Salud_Bateria",
    nbins=30,
    title="Distribución de la salud de las baterías",
    labels={
        "Salud_Bateria": "Salud de batería (%)",
        "count": "Cantidad de baterías"
    },
    color_discrete_sequence=["#B963BB"]  
)
st.plotly_chart(fig,use_container_width=True)
# GRÁFICOS: EDAD Y CICLOS
st.subheader("Relación entre variables")

col1, col2 = st.columns(2)

with col1:
    fig = px.scatter(
        df_filtrado,
        x="Edad_Bateria",
        y="Salud_Bateria",
        color="Categoria_Salud",
        title="Edad vs Salud",
        labels={
            "Edad_Bateria": "Edad de batería (años)",
            "Salud_Bateria": "Salud (%)",
            "Categoria_Salud": "Nivel de salud"
        },
        color_discrete_map={
            "Buena": "#27AE60",
            "Regular": "#F1C40F",
            "Baja": "#E74C3C"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:
    fig = px.scatter(
        df_filtrado,
        x="Ciclos_Carga",
        y="Salud_Bateria",
        color="Categoria_Salud",
        title="Ciclos de carga vs Salud",
        labels={
            "Ciclos_Carga": "Ciclos de carga",
            "Salud_Bateria": "Salud (%)",
            "Categoria_Salud": "Nivel de salud"
        },
        color_discrete_map={
            "Buena": "#27AE60",
            "Regular": "#F1C40F",
            "Baja": "#E74C3C"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# CAPACIDAD RETENIDA Y CATEGORÍAS
col1, col2 = st.columns(2)

with col1:
    fig = px.scatter(
        df_filtrado,
        x="Capacidad_Retenida",
        y="Salud_Bateria",
        color="Categoria_Salud",
        title="Capacidad retenida vs Salud",
        labels={
            "Capacidad_Retenida": "Capacidad retenida (%)",
            "Salud_Bateria": "Salud (%)",
            "Categoria_Salud": "Nivel de salud"
        },
        color_discrete_map={
            "Buena": "#27AE60",
            "Regular": "#F1C40F",
            "Baja": "#E74C3C"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:
    conteo_salud = (
        df_filtrado["Categoria_Salud"]
        .value_counts()
        .reset_index()
    )

    conteo_salud.columns = [
        "Categoria_Salud",
        "Cantidad"
    ]

    fig = px.bar(
        conteo_salud,
        x="Categoria_Salud",
        y="Cantidad",
        color="Categoria_Salud",
        title="Baterías según nivel de salud",
        labels={
            "Categoria_Salud": "Nivel de salud ",
            "Cantidad": "Cantidad de baterías "
        },
        color_discrete_map={
            "Buena": "#27AE60",
            "Regular": "#F1C40F",
            "Baja": "#E74C3C"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )