import streamlit as st

# Título de la página
st.title("Contactanos 📧")

# Campos del formulario
nombre = st.text_input("Nombre")
correo = st.text_input("Correo Electrónico")
mensaje = st.text_area("Mensaje")

# Botón de envío
if st.button("Enviar"):
    # Aquí puedes agregar la lógica para procesar el formulario, como enviar un correo electrónico, almacenar en una base de datos, etc.
    st.success("Formulario enviado exitosamente")

