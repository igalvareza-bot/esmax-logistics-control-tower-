import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="ESMAX Control Tower", layout="wide")

# Título principal
st.title("ESMAX Logistics Control Tower 4.0")
st.subheader("Panel Ejecutivo de Supervisión Logística")

st.divider()

# =========================
# KPIs PRINCIPALES
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Nivel de Servicio", "96%", "+2%")
col2.metric("OTIF", "94%", "+1%")
col3.metric("Rotación Inventario", "12.4", "+0.8")
col4.metric("Stock Crítico", "3.2%", "-0.5%")

st.divider()

# =========================
# DATOS SIMULADOS
# =========================
np.random.seed(42)

df = pd.DataFrame({
    "Centro de Distribución": ["Norte", "Centro", "Sur", "RM", "Industrial"],
    "Stock": np.random.randint(50, 200, 5),
    "Demanda": np.random.randint(40, 180, 5)
})

# =========================
# GRÁFICO OPERACIONAL
# =========================
fig = px.bar(
    df,
    x="Centro de Distribución",
    y=["Stock", "Demanda"],
    barmode="group",
    title="Comparación de Stock vs Demanda por Centro"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# SEMÁFORO DE RIESGO
# =========================
st.subheader("Semáforo de Riesgo Logístico")

riesgo = np.random.choice(["Bajo", "Medio", "Alto"])

if riesgo == "Bajo":
    st.success("Riesgo Operacional: BAJO")
    st.write("Operación estable sin alertas críticas.")
elif riesgo == "Medio":
    st.warning("Riesgo Operacional: MEDIO")
    st.write("Se recomienda monitoreo de inventarios y abastecimiento.")
else:
    st.error("Riesgo Operacional: ALTO")
    st.write("Posible quiebre de stock o retrasos en la cadena de suministro.")

st.divider()

# =========================
# MENSAJE EJECUTIVO
# =========================
st.info("Sistema de apoyo a la toma de decisiones basado en analítica logística y principios de Logística 4.0.")