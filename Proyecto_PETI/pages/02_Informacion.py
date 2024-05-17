import streamlit as st

import vistas.overview as overview
import vistas.banner as banner

banner.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 24px"><b>'
            f'Informacion'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

overview.recomendaciones()
overview.manejo_aplicacion()
