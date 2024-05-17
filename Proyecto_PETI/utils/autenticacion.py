import streamlit as st

def verificar():
    if 'authenticated' in st.session_state and st.session_state['authenticated']:
        return True
    else:
        return False