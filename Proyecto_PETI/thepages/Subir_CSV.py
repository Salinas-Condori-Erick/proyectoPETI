import pandas as pd
import streamlit as st


with st.container():
    my_file = st.file_uploader('Sube tu archivo de **parámetros** (.csv)', type=['csv'])

    if my_file is not None:
        if 'my_file' not in st.session_state:
            st.session_state.my_file = my_file

        st.write(st.session_state)

        df = pd.read_csv(my_file)

        st.write(df)
