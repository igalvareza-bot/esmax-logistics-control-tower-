import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="ESMAX CONTROL TOWER", layout="wide")

# =========================
# TÍTULO
# =========================
st.markdown("# 🏢 ESMAX LOGISTICS CONTROL TOWER 4.0")
st.markdown("### Sistema de supervisión logística y analítica ejecutiva")
st.markdown("---")

# =========================
# AUTORES
# =========================
st.markdown("## 👥 Equipo de Proyecto")

st.markdown("""
- Ignacio Álvarez  
- Benjamín Tello  
- Renato Soto  
""")

st.markdown("---")

# =========================
# KPIs
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Nivel de Servicio", "96.2%")
col2.metric("OTIF", "94.5%")
col3.metric("Rotación Inventario", "12.4")
col4.metric("Stock Crítico", "3.1%")

st.markdown("---")

# =========================
# DATOS
# =========================
np.random.seed(42)

df = pd.DataFrame({
    "Centro": ["Norte", "Centro", "Sur", "RM", "Industrial"],
    "Stock": np.random.randint(60, 200, 5),
    "Demanda": np.random.randint(50, 180, 5)
})

fig = px.bar(df, x="Centro", y=["Stock", "Demanda"], barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# FODA
# =========================
st.markdown("## FODA")

st.markdown("""
Fortalezas: red logística nacional  
Debilidades: baja visibilidad en tiempo real  
Oportunidades: digitalización  
Amenazas: variabilidad de demanda  
""")

st.markdown("---")

# =========================
# MARCO LEGAL
# =========================
st.markdown("## ⚖️ Marco Legal y Normativo")

st.markdown("""
- Ley 18.410 (SEC)  
- DS 160 combustibles  
- Ley 16.744 seguridad laboral  
- Ley 19.300 medio ambiente  
- ISO 9001 / 14001 / 45001 / 28000  
""")

st.markdown("---")

# =========================
# RIESGO
# =========================
riesgo = np.random.choice(["BAJO", "MEDIO", "ALTO"])

st.markdown("## ⚠ Riesgo Operacional")

if riesgo == "BAJO":
    st.success("Operación estable")
elif riesgo == "MEDIO":
    st.warning("Monitoreo requerido")
else:
    st.error("Riesgo crítico")

st.markdown("---")

# =========================
# CONCLUSIÓN
# =========================
st.info("Sistema de control logístico orientado a soporte de decisiones ejecutivas en cadena de suministro.")