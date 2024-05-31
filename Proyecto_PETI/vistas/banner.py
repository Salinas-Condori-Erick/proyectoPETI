import streamlit as st
import utils.autenticacion as autenticacion

import vistas.VistaUsuario as VistaUsuario
import vistas.VistaPlanEstrategico as VistaPlanEstrategico

from modelos.Usuario import Usuario
from modelos.PlanEstrategico import PlanEstrategico

def home_title():
    # Esta función establece el diseño general de la página y el banner superior
    url = icon()
    st.set_page_config(page_title='PETIAppVision ',
                    layout='wide',
                    page_icon=url)
    st.image(url)
    st.markdown(f'<span style="color: #4b7fd1; '
                f'font-size: 36px"><b>PETIAppVision  - Planificación Estratégica</b></span>'
                , unsafe_allow_html=True)

    # Verificar si el usuario esta autenticado

    u = Usuario()
    pe = PlanEstrategico()

    if autenticacion.verificar():

        # Nombre Usuario / noFoto
        user_id = st.session_state['user_id']
        usuario = u.obtener_usuario_por_id(user_id)


        #st.sidebar.write(f"Bienvenido, {usuario['NombreUsuario']}")


        # Opcion Editar Usuario
        if st.sidebar.button(f"Editar Usuario - {usuario['NombreUsuario']}"):
            VistaUsuario.form_editar_usuario(user_id)



        # Opcion ver planes
        if st.sidebar.button("Mis Planes Estratégicos"):
            #st.experimental_rerun()
            VistaPlanEstrategico.gestion_planes()

        if st.sidebar.button("Agregar Plan Estrategico"):
            VistaPlanEstrategico.form_agregar_plan(st.session_state['user_id'])



        #plan = pe.obtener_plan_por_id(st.session_state['plan_seleccionado'])

        #print("user_id:", st.session_state['user_id'])

        # Plan seleccionado
        planes = pe.listar_planes_por_id_usuario(user_id)
        
        if planes:
            # Establecer plan no se esta usando "dictionary=True" en el modelo
            if 'plan_seleccionado' not in st.session_state:
                st.session_state['plan_seleccionado'] = planes[0]

            # Selectbox
            plan_seleccionado = st.session_state['plan_seleccionado'] # ID del plan seleccionado
            plan_actual = st.sidebar.selectbox("Seleccionar Plan Estrategico", planes, index=planes.index(plan_seleccionado))

            # Actualizar plan seleccionado
            if plan_actual != st.session_state['plan_seleccionado']:
                st.session_state['plan_seleccionado'] = plan_actual
                #st.experimental_rerun()
                st.rerun()





            # Mostrar información del plan seleccionado
            # st.sidebar.write(f"Plan Estratégico Seleccionado: {'111111'}") # plan_seleccionado
            # mostrar_informacion_del_plan(plan_seleccionado)

        else:
            st.sidebar.write("No hay planes estratégicos disponibles.")
            if st.sidebar.button("Crear Plan Estratégico"):
                VistaPlanEstrategico.form_agregar_plan(st.session_state['user_id'])




    else:
        VistaUsuario.login_usuario()



def icon():
    url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/' \
        'jigsaws-puzzle_pieces-planning-creative-strategy-128.png'
    return url
