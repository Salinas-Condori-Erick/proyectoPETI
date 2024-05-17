import streamlit as st

def login():
    st.title("Sistema de Login")

    nombre_usuario = st.text_input("Nombre de Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    st.button("Iniciar Sesión")

login()