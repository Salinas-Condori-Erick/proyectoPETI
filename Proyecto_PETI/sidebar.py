import streamlit as st

def home_page():
    st.header("Home")
    st.write("Bienvenido a la página principal.")

def parametros_externos():
    st.header("Parámetros Externos")
    st.write("Gestión de parámetros externos.")

def parametros_internos():
    st.header("Parámetros Internos")
    st.write("Gestión de parámetros internos.")

def editar_data():
    st.header("Editar Data")
    st.write("Herramientas para editar datos.")

def analizar():
    st.header("Analizar")
    st.write("Herramientas de análisis de datos.")

def informacion():
    st.header("Información")
    st.write("Información sobre la herramienta o sistema.")

def login():
    st.header("Login")
    st.write("Página de inicio de sesión.")

def new_page_espacio_pagina():
    st.header("Nueva Página")
    st.write("Contenido de la nueva página.")

def subir_csv():
    st.header("Subir CSV")
    st.write("Carga archivos CSV para análisis.")








# Configuración del sidebar
st.sidebar.title("Navegación")
options = ["Home", "Parámetros Externos", "Parámetros Internos", "Editar Data", "Analizar",
           "Información", "Login", "New Page Espacio Pagina", "Subir CSV"]
choice = st.sidebar.selectbox("Menú", options)

# Diccionario para relacionar opciones con funciones
pages = {
    "Home": home_page,
    "Parámetros Externos": parametros_externos,
    "Parámetros Internos": parametros_internos,
    "Editar Data": editar_data,
    "Analizar": analizar,
    "Información": informacion,
    "Login": login,
    "New Page Espacio Pagina": new_page_espacio_pagina,
    "Subir CSV": subir_csv
}

# Ejecución de la función seleccionada
if choice:
    pages[choice]()










# pip install streamlit-option-menu
# from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu(
#     menu_title = "Main Menu",
#     options = ["Home","Warehouse","Query Optimization and Processing","Storage","Contact Us"],
#     icons = ["house","gear","activity","snowflake","envelope"],
#     menu_icon = "cast",
#     default_index = 0,
#     #orientation = "horizontal",
# )
