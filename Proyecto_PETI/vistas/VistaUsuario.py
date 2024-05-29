import streamlit as st
from modelos.Usuario import Usuario

import vistas.VistaPlanEstrategico as VistaPlanEstrategico

#import modelos.Usuario as u

def login_usuario():
    st.title("Login")
    nombre_usuario = st.text_input("Nombre de Usuario")
    contraseña = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        usuario = Usuario()
        autenticado, user_id = usuario.login(nombre_usuario, contraseña)
        if autenticado:
            st.session_state['authenticated'] = True
            st.session_state['user_id'] = user_id
            st.success("Has iniciado sesión con éxito.") # No se ve al actualizar con "st.rerun()"
            #st.experimental_rerun()
            st.rerun()
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")
    st.stop()



def form_editar_usuario(id_usuario):
    st.title("Editar Usuario")


    if st.sidebar.button("Mis Planes Estratégicos"):
        VistaPlanEstrategico.gestion_planes()

    if st.sidebar.button("Agregar Plan Estrategico"):
        VistaPlanEstrategico.form_agregar_plan(st.session_state['user_id'])

    st.sidebar.button("Volver")


    usuario = Usuario()
    user = usuario.obtener_usuario_por_id(id_usuario)

    if user:
        with st.form("form_editar_usuario"):
            nombre_usuario = st.text_input("Nombre de Usuario", value=user['NombreUsuario'])
            contrasena = st.text_input("Contraseña", type="password", value=user['Contrasena'])
            email = st.text_input("Correo Electrónico", value=user['Email'])

            if st.form_submit_button("Actualizar Usuario"):
                print("Botón presionado")
                print("ID:", id_usuario)
                print("Nombre:", nombre_usuario)
                print("Contraseña:", contrasena)
                print("Email:", email)
    else:
        st.error("Usuario no encontrado.")
    st.stop()