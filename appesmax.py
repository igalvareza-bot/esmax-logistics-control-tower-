import streamlit as st
import numpy as np

st.set_page_config(page_title="ESMAX Control Tower 4.0", layout="wide")

# =========================
# HEADER
# =========================
st.markdown("# 🏢 ESMAX LOGISTICS CONTROL TOWER 4.0")
st.markdown("### Supervisión logística ejecutiva basada en datos, KPIs y simulación avanzada")
st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# KPI
# =========================
st.markdown("## 📊 KPIs Estratégicos")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Nivel de Servicio", "96.2%", "+2.1%")
col2.metric("OTIF", "94.5%", "+1.3%")
col3.metric("Rotación Inventario", "12.4", "+0.8")
col4.metric("Stock Crítico", "3.1%", "-0.6%")

with st.expander("📌 Interpretación ejecutiva de KPIs"):
    st.markdown("""
    ➤ Nivel de Servicio: cumplimiento de entrega al cliente  
    ➤ OTIF: entregas completas y a tiempo  
    ➤ Rotación: eficiencia del inventario  
    ➤ Stock Crítico: riesgo de quiebre operativo  

    ⚠ Estado general: operación estable con riesgo moderado en inventario.
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# ABC INVENTARIO
# =========================
st.markdown("## 📦 Clasificación ABC de Inventario")

st.code("""
A (20%) ───────── Alta rotación / prioridad crítica
B (60%) ───────── Rotación media / control operativo
C (20%) ───────── Baja rotación / almacenamiento largo
""")

with st.expander("📌 Análisis ABC logístico"):
    st.markdown("""
    ➤ SKU totales: 600  
    ➤ Posiciones pallet: 1.560  

    ➤ Impacto:
    - Optimización de espacio
    - Reducción de costos logísticos
    - Mejora en nivel de servicio
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# LAYOUT BODEGA
# =========================
st.markdown("## 🏗️ Layout Operacional de Bodega")

st.code("""
ENTRADA → RECEPCIÓN → STORAGE → PICKING → DESPACHO
   ↓           ↓          ↓         ↓         ↓
  8%         10%        65%       7%       10%
""")

with st.expander("📌 Flujo operacional"):
    st.markdown("""
    ➤ Flujo en U implementado  
    ➤ Reducción de cruces operativos  
    ➤ Optimización de rutas Reach Truck  

    Resultado:
    ↓ 18% en tiempos internos de operación
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# NORMATIVA
# =========================
st.markdown("## ⚖️ Marco Legal y Normativo")

with st.expander("📌 Normativa vigente aplicada"):
    st.markdown("""
    ➤ Ley 18.410 (SEC – seguridad energética)  
    ➤ DS 160 (combustibles y almacenamiento)  
    ➤ Ley 16.744 (seguridad laboral)  
    ➤ Ley 19.300 (medio ambiente)  
    ➤ ISO 9001 (calidad)  
    ➤ ISO 14001 (medio ambiente)  
    ➤ ISO 45001 (seguridad laboral)  
    ➤ ISO 28000 (cadena de suministro)  

    Impacto:
    - Cumplimiento regulatorio
    - Reducción de riesgos operacionales
    - Trazabilidad completa
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# MODELO PREDICTIVO
# =========================
st.markdown("## 🤖 Modelo Predictivo de Demanda")

demanda = np.random.randint(100, 200)
prediccion = demanda * np.random.uniform(0.85, 1.15)

st.write("Demanda actual simulada:", demanda)
st.write("Predicción futura:", int(prediccion))

with st.expander("📌 Lógica del modelo"):
    st.markdown("""
    ➤ Modelo estocástico básico  
    ➤ Variación ±15%  
    ➤ Simulación de escenarios  

    Uso:
    - planificación de stock
    - anticipación de demanda
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# AHORRO ECONÓMICO
# =========================
st.markdown("## 💰 Impacto Económico")

with st.expander("📌 Análisis financiero estimado"):
    st.markdown("""
    ➤ Reducción inventario: -12%  
    ➤ Mejora eficiencia: +18%  
    ➤ Reducción errores: -25%  

    💵 Ahorro estimado anual:
    → USD 80.000 – 150.000  

    ROI estimado:
    → 6 a 12 meses
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# PYTHON
# =========================
st.markdown("## 🐍 Uso de Python en la solución")

with st.expander("📌 Justificación técnica"):
    st.markdown("""
    Python permite:

    ➤ Automatización de procesos logísticos  
    ➤ Análisis de grandes volúmenes de datos  
    ➤ Simulación de escenarios  
    ➤ Visualización ejecutiva  

    Beneficio:
    - mayor velocidad de decisión
    - reducción de análisis manual
    - soporte a decisiones ejecutivas
    """)

st.markdown("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# CONCLUSIÓN
# =========================
st.success("Sistema de torre de control logística orientado a decisiones ejecutivas en ESMAX.")