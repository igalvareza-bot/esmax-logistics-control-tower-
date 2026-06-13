import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="ESMAX Control Tower", layout="wide")

# =========================
# HEADER
# =========================
st.title("ESMAX Logistics Control Tower 4.0")
st.caption("Sistema de supervisión logística basado en KPIs, analítica de datos y Logística 4.0")

st.divider()

# =========================
# KPIs EJECUTIVOS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Nivel de Servicio", "96.2%")
col2.metric("OTIF", "94.5%")
col3.metric("Rotación Inventario", "12.4")
col4.metric("Stock Crítico", "3.1%")

st.divider()

# =========================
# DATOS SIMULADOS
# =========================
np.random.seed(42)

df = pd.DataFrame({
    "Centro de Distribución": ["Norte", "Centro", "Sur", "RM", "Industrial"],
    "Stock": np.random.randint(60, 200, 5),
    "Demanda": np.random.randint(50, 180, 5)
})

# =========================
# GRÁFICO PRINCIPAL
# =========================
fig = px.bar(
    df,
    x="Centro de Distribución",
    y=["Stock", "Demanda"],
    barmode="group",
    title="Comparación de Stock vs Demanda por Centro de Distribución"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# FODA ESTRATÉGICO
# =========================
st.subheader("Análisis Estratégico FODA")

st.write("✔ Fortalezas: red logística nacional, cobertura operativa")
st.write("✔ Debilidades: baja visibilidad en tiempo real, procesos manuales")
st.write("✔ Oportunidades: digitalización logística, analítica predictiva")
st.write("✔ Amenazas: variabilidad de demanda, costos de transporte")

st.divider()

# =========================
# RIESGO OPERACIONAL
# =========================
st.subheader("Mapa de Riesgo Logístico")

riesgo = np.random.choice(["Bajo", "Medio", "Alto"])

if riesgo == "Bajo":
    st.success("Riesgo BAJO: operación estable")
elif riesgo == "Medio":
    st.warning("Riesgo MEDIO: requiere monitoreo")
else:
    st.error("Riesgo ALTO: posible quiebre de stock")

st.divider()

# =========================
# MENSAJE EJECUTIVO FINAL
# =========================
st.info("""
ESMAX Logistics Control Tower 4.0 permite mejorar la toma de decisiones logísticas
mediante la integración de KPIs, visualización de datos y análisis de riesgo operativo,
alineado con principios de Supply Chain Management y Logística 4.0.
""")