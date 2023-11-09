import streamlit as st
import re


col1, col2, col3=st.columns([1,1,1])
# Inserta una imagen de un logotipo desde una URL
col2.image("logo.png", caption="",  width=200)

st.title('Misión')
st.markdown('***')

texto1 = (
   "En Mindful Data, nuestra misión es transformar la información dispersa en reseñas en valiosas perspectivas para inversionistas. Nos comprometemos a proporcionar análisis de datos precisos y significativos que guíen a nuestros clientes hacia decisiones financieras informadas y exitosas. Valoramos la transparencia, la ética y la innovación en nuestro enfoque de análisis de datos, brindando confianza y ventaja competitiva a quienes confían en nosotros"
)
css = f"""
    <style>
        p {{
            font-size: 18px;
            text-align: justify;
            text-justify: inter-word;
            line-height: 1.4;
        }}
    </style>
"""
st.markdown(f"{css}{texto1}", unsafe_allow_html=True)


st.title('Visión')
st.markdown('***')
texto2 = (
    "En Mindful Data, aspiramos a ser líderes reconocidos en la consultoría de datos, proporcionando análisis de reseñas de Yelp y Google Maps que permitan a inversionistas identificar oportunidades de manera estratégica. Visualizamos un futuro en el que nuestros servicios sean un pilar fundamental en la toma de decisiones financieras, contribuyendo al éxito de nuestros clientes y a la evolución de la industria de inversión. Nos esforzamos por mantener la excelencia en análisis de datos, fomentando un entorno de aprendizaje constante y colaboración creativa"
)
st.markdown(f"{css}{texto2}", unsafe_allow_html=True)

st.title('Valores')
st.markdown('***')

st.markdown("<ul><li>Colaboración que potencia.🏋️‍♂️</li><li>Creatividad que innova.🧑🏽‍💻</li><li> Esfuerzo que cumple objetivos.✅</li><li>Empatía que se pone en acción.🏃🏿‍♂️</li><li> Transparencia que genera confianza.🙏🏽</li></ul>", unsafe_allow_html=True)

st.title('Compromisos')
st.markdown('***')

st.markdown("<ul><li>Hacer de la calidad una prioridad.🫵🏽</li><li>Transferir generosamente nuestro conocimiento.🤓</li><li> Compartir nuestra visión de futuro.🧙🏿‍♂️</li><li>Conectar mundos y soluciones. 🌍</li><li>Forjar vínculos significativos. 🤝</li></ul>", unsafe_allow_html=True)