import streamlit as st

st.markdown("<h1 style='text-align: center; color: #002060;'> ¿Quiénes somos? 🫂 </h1>", unsafe_allow_html=True)

st.markdown('***')

col1, col2=st.columns([2,2])

col1.markdown("<h3 style='text-align: center; color: grey;'> Sebastián Di Nesta <br> Data Engineer </h3>", unsafe_allow_html=True)
# Inserta una imagen de un logotipo desde una URL
col1.image("sebastian.png", caption="",  width=300)

col2.markdown("<h3 style='text-align: center; color: grey;'> Joaquin Laurencio <br> Data Engineer </h3>", unsafe_allow_html=True)
# Inserta una imagen de un logotipo desde una URL
col2.image("Joaquin.png", caption="",  width=300)


col1.markdown("<h3 style='text-align: center; color: grey;'> Williams Amaro Roque <br> Data Analytics </h3>", unsafe_allow_html=True)
# Inserta una imagen de un logotipo desde una URL
col1.image("williams.png", caption="",  width=300)

col2.markdown("<h3 style='text-align: center; color: grey;'> Betiana Lopez Andueza <br> Data Analytics </h3>", unsafe_allow_html=True)
# Inserta una imagen de un logotipo desde una URL
col2.image("betiana.png", caption="",  width=300)


col1.markdown("<h3 style='text-align: center; color: grey;'> Nathalie Saravia <br> Data Scientist </h3>", unsafe_allow_html=True)
# Inserta una imagen de un logotipo desde una URL
col1.image("nathalie.png", caption="",  width=300)
st.markdown('***')
