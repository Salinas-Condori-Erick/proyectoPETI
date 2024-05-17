import streamlit as st

import vistas.VistaPlanEstrategico as VistaPlanEstrategico
import vistas.banner as banner

import utils.autenticacion as autenticacion
import vistas.VistaUsuario as VistaUsuario

#if autenticacion.verificar():


banner.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 24px"><b>'
            f'Valores'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

VistaPlanEstrategico.valores()





#    VistaPlanEstrategico.gestion_planes()
#else:
#    VistaUsuario.login_usuario()
