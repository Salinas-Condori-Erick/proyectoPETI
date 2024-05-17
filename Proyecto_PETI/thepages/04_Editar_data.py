import streamlit as st

import engine

# Configurando la parte superior de la página
engine.home_title()

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Edita tus datos'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

engine.edit_data()

engine.save_file()
