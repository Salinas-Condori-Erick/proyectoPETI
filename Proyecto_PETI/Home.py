import streamlit as st


import vistas.banner as banner

# Setting top of page
banner.home_title()

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 24px"><b>'
            f'Aplicación para simplificar la planificación estratégica basada en parámetros definidos por el usuario'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

#engine.home_menu()




