import pandas as pd
import streamlit as st

import engine

engine.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Parámetros internos que afectan a la organización'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 14px"><b>'
            f'Ingresa hasta 5 parámetros internos'
            f'</b></span>'
            , unsafe_allow_html=True)

# DataFrame de parámetros internos
engine.data_internal()
