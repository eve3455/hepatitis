import streamlit as st
import pandas as pd
import sweetviz as sv
import streamlit.components.v1 as components
import datetime

# ==========================================
# # CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Análisis de Datos Médicos - Hepatitis C",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# # BARRA LATERAL (PERSONALIZACIÓN)
# ==========================================
with st.sidebar:
    st.image("c:\\Users\\Usuario\\Prueba MD\\yo.jpeg", width=80) # Icono médico
    st.markdown("## **Presentado por:**")
    st.markdown("👤 **Evelyn tuba**")
    st.markdown("🎓 **BIG DATA / Mineria de datos**")
    
    st.markdown("---")
    st.markdown("📅 **4/6/2026:**")
    # Muestra la fecha actual automáticamente de forma elegante
    fecha_actual = datetime.date.today().strftime("%d / %m / %Y")
    st.info(f"{fecha_actual}")
    
    st.markdown("---")
    st.caption("Desarrollado con Python 🐍 y Streamlit")

# ==========================================
# # CUERPO PRINCIPAL
# ==========================================
st.title("🧬 Análisis Automático de Datos Médicos")
st.markdown("#### *Estudio y diagnóstico predictivo de Hepatitis C y condiciones hepáticas.*")
st.markdown("---")

# Explicación breve de la app
st.write(
    "Esta plataforma permite explorar de forma interactiva las variables clínicas de los pacientes "
    "y generar reportes automatizados de salud mediante la librería **Sweetviz**."
)

# ==========================================
# # SECCIÓN DE DATOS (Métricas clave para HepatitisCdata.csv)
# ==========================================
# Intentamos cargar tu archivo automáticamente si está en la misma carpeta
try:
    df = pd.read_csv("HepatitisCdata.csv", index_col=0)
    
    st.subheader("📊 Resumen del Conjunto de Datos")
    
    # Creamos columnas visuales para métricas de tu data
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total de Pacientes", value=len(df))
    with col2:
        st.metric(label="Edad Promedio", value=f"{int(df['Age'].mean())} años")
    with col3:
        st.metric(label="Hombres 👨", value=len(df[df['Sex'] == 'm']))
    with col4:
        st.metric(label="Mujeres 👩", value=len(df[df['Sex'] == 'f']))
        
    # Organizar la vista en Pestañas (Tabs) para que se vea limpio
    tab1, tab2 = st.tabs(["📋 Vista Previa de Datos", "🔥 Reporte Avanzado (Sweetviz)"])
    
    with tab1:
        st.markdown("### Primeros registros de la base de datos:")
        # Modificamos el diseño del dataframe para que use todo el ancho y se vea mejor
        st.dataframe(df.head(10), use_container_width=True)
        
    with tab2:
        st.markdown("### Generación del Reporte Automatizado")
        if st.button("🚀 Generar / Actualizar Reporte de Sweetviz"):
            with st.spinner("Analizando variables médicas... Esto puede tardar unos segundos."):
                # Generar reporte con Sweetviz enfocado en la categoría diagnóstica ('Category')
                reporte = sv.analyze(df)
                reporte.show_html('reporte_sweetviz.html', open_browser=False)
                st.success("¡Reporte generado con éxito!")
            
            # Mostrar el reporte de Sweetviz embebido directamente dentro de Streamlit
            try:
                with open("reporte_sweetviz.html", 'r', encoding='utf-8') as f:
                    html_content = f.read()
                components.html(html_content, height=800, scroller=True)
            except Exception as e:
                st.error("No se pudo desplegar el HTML en pantalla, pero se guardó en tu carpeta.")

except FileNotFoundError:
    st.warning("⚠️ No se encontró el archivo 'HepatitisCdata.csv' en esta carpeta. Colócalo aquí para habilitar las funciones avanzadas.")