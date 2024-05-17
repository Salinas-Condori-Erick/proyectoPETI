import pandas as pd
import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
import altair


# TÍTULOS Y PÁGINA DE INICIO
def home_title():
    # Esta función establece el diseño general de la página y el banner superior
    url = icon()
    st.set_page_config(page_title='StraApp',
                       layout='wide',
                       page_icon=url)
    st.image(url)
    st.markdown(f'<span style="color: #4b7fd1; '
                f'font-size: 24px"><b>StraApp - Planificación Estratégica</b></span>'
                , unsafe_allow_html=True)


def icon():
    url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/' \
          'jigsaws-puzzle_pieces-planning-creative-strategy-128.png'
    return url


def home_menu():
    # with st.container():
    #     url1 = 'https://cdn4.iconfinder.com/data/icons/evil-icons-user-interface/64/arrow_right-64.png'
    #     st.image(url1)
    #
    #     st.markdown(f'<span style="color: #4b7fd1; '
    #                 f'font-size: 18px"><b>Data  **  Analyze  **  Results</b></span>'
    #                 , unsafe_allow_html=True)
    # st.markdown('___')

    with st.container():
        url2 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-3/24/edit-48.png'
        url3 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-6/24/upload-48.png'
        st.image(url2)
        if st.button('Ingresar datos'):
            st.success("Presiona 'Ingresar Parámetros Externos' en la barra lateral")

        st.image(url3)
        upload_file()
        # st.write(st.session_state)
    save_file()


def save_file():
    # Función para guardar y descargar el archivo de datos en formato csv
    if 'df' in st.session_state:
        df = st.session_state.df
        csv = df.to_csv(index=False)

        st.sidebar.markdown(f'<span style="color: #f0410c; '
                    f'font-size: 16px"><b>Descargar y guardar datos</b></span>'
                    , unsafe_allow_html=True)
        st.sidebar.download_button('Presiona para descargar',
                                   data=csv,
                                   file_name='mis_datos.csv',
                                   )

    else:
        pass

def data_external():
    # Esta función permite al usuario ingresar datos -
    # variables externas que afectan a la organización

    dfe = initial_dfe()

    with st.form('external_form'):

        parameter1 = st.text_input(f'**Parámetro** #1', key='param1_e')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Importancia** para la organización',
                                ['promedio', 'por encima del promedio', 'alto', 'muy alto'],
                                 index=3, horizontal=True, key='sig1_e')
        probability1 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_e')
        influencer11 = st.text_input('**Influenciador** #1', key='inf11_e')
        influencer12 = st.text_input('**Influenciador** #2', key='inf12_e')
        influencer13 = st.text_input('**Influenciador** #3', key='inf13_e')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parámetro** #2', key='param2_e')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alto', 'muy alto'],
                                 index=3, horizontal=True, key='sig2_e')
        probability2 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_e')
        influencer21 = st.text_input('**Influenciador** #1', key='inf21_e')
        influencer22 = st.text_input('**Influenciador** #2', key='inf22_e')
        influencer23 = st.text_input('**Influenciador** #3', key='inf23_e')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parámetro** #3', key='param3_e')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alto', 'muy alto'],
                                 index=3, horizontal=True, key='sig3_e')
        probability3 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_e')
        influencer31 = st.text_input('**Influenciador** #1', key='inf31_e')
        influencer32 = st.text_input('**Influenciador** #2', key='inf32_e')
        influencer33 = st.text_input('**Influenciador** #3', key='inf33_e')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parámetro** #4', key='param4_e')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alto', 'muy alto'],
                                 index=3, horizontal=True, key='sig4_e')
        probability4 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_e')
        influencer41 = st.text_input('**Influenciador** #1', key='inf41_e')
        influencer42 = st.text_input('**Influenciador** #2', key='inf42_e')
        influencer43 = st.text_input('**Influenciador** #3', key='inf43_e')
        st.markdown('___')

        parameter5= st.text_input(f'**Parámetro** #5', key='param5_e')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alto', 'muy alto'],
                                 index=3, horizontal=True, key='sig5_e')
        probability5 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_e')
        influencer51 = st.text_input('**Influenciador** #1', key='inf51_e')
        influencer52 = st.text_input('**Influenciador** #2', key='inf52_e')
        influencer53 = st.text_input('**Influenciador** #3', key='inf53_e')
        st.markdown('___')


       # Botón para enviar el formulario
        submit_external = st.form_submit_button(type='primary')

        # Si se ha enviado el formulario externo
        if submit_external:
            # Recopilar datos en listas
            parameter = [parameter1, parameter2, parameter3, parameter4, parameter5]
            significance = [significance1, significance2, significance3,
                            significance4, significance5]
            prob_low = [probability1[0], probability2[0], probability3[0],
                        probability4[0], probability5[0]]
            prob_high = [probability1[1], probability2[1], probability3[1],
                        probability4[1], probability5[1]]
            influencer1 = [influencer11, influencer21, influencer31, influencer41,
                        influencer51]
            influencer2 = [influencer12, influencer22, influencer32, influencer42,
                        influencer52]
            influencer3 = [influencer13, influencer23, influencer33, influencer43,
                        influencer53]
            # Crear un DataFrame con los datos recopilados
            dfe = pd.DataFrame({'environment': ['external', 'external', 'external', 'external', 'external'],
                                'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high,
                                'influencer1': influencer1,
                                'influencer2': influencer2,
                                'influencer3': influencer3})
            # Mostrar un mensaje de éxito
            st.success("Tus datos han sido guardados. Puedes ver y editar los datos yendo a la página 'Editar datos'")

        # Si dfe no está en la sesión de estado
        if dfe not in st.session_state:
            # Guardar dfe en la sesión de estado
            st.session_state.dfe = dfe
        else:
            # Actualizar dfe en la sesión de estado
            st.session_state.dfe = dfe

        # Agregar dfi (parámetros internos) si no existe en la sesión de estado
        if 'dfi' not in st.session_state:
            # Crear dfi inicial
            dfi = initial_dfi()
            # Guardar dfi en la sesión de estado
            st.session_state.dfi = dfi

        # Llamar a la función parameters
        parameters()

        # Retornar dfe
        return dfe


def data_internal():
    # Esta función permite al usuario ingresar datos -
    # variables internas que afectan a la organización

    # Obtener el DataFrame inicial para los datos internos
    dfi = initial_dfi()

    with st.form('internal_form'):

        # Entradas para el primer parámetro
        parameter1 = st.text_input(f'**Parámetro** #1', key='param1_i')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Importancia** para la organización',
                                ['promedio', 'por encima del promedio', 'alta', 'muy alta'],
                                 index=3, horizontal=True, key='sig1_i')
        probability1 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_i')
        influencer11 = st.text_input('**Influyente** #1', key='inf11_i')
        influencer12 = st.text_input('**Influyente** #2', key='inf12_i')
        influencer13 = st.text_input('**Influyente** #3', key='inf13_i')
        st.markdown('___')

        # Entradas para el segundo parámetro
        parameter2 = st.text_input(f'**Parámetro** #2', key='param2_i')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alta', 'muy alta'],
                                 index=3, horizontal=True, key='sig2_i')
        probability2 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_i')
        influencer21 = st.text_input('**Influyente** #1', key='inf21_i')
        influencer22 = st.text_input('**Influyente** #2', key='inf22_i')
        influencer23 = st.text_input('**Influyente** #3', key='inf23_i')
        st.markdown('___')

        # Entradas para el tercer parámetro
        parameter3 = st.text_input(f'**Parámetro** #3', key='param3_i')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alta', 'muy alta'],
                                 index=3, horizontal=True, key='sig3_i')
        probability3 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_i')
        influencer31 = st.text_input('**Influyente** #1', key='inf31_i')
        influencer32 = st.text_input('**Influyente** #2', key='inf32_i')
        influencer33 = st.text_input('**Influyente** #3', key='inf33_i')
        st.markdown('___')

        # Entradas para el cuarto parámetro
        parameter4 = st.text_input(f'**Parámetro** #4', key='param4_i')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alta', 'muy alta'],
                                 index=3, horizontal=True, key='sig4_i')
        probability4 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_i')
        influencer41 = st.text_input('**Influyente** #1', key='inf41_i')
        influencer42 = st.text_input('**Influyente** #2', key='inf42_i')
        influencer43 = st.text_input('**Influyente** #3', key='inf43_i')
        st.markdown('___')

        # Entradas para el quinto parámetro
        parameter5 = st.text_input(f'**Parámetro** #5', key='param5_i')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Importancia** para la organización',
                                 ['promedio', 'por encima del promedio', 'alta', 'muy alta'],
                                 index=3, horizontal=True, key='sig5_i')
        probability5 = st.slider('**Probabilidad**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_i')
        influencer51 = st.text_input('**Influyente** #1', key='inf51_i')
        influencer52 = st.text_input('**Influyente** #2', key='inf52_i')
        influencer53 = st.text_input('**Influyente** #3', key='inf53_i')
        st.markdown('___')

        # Botón para enviar el formulario interno
        submit_internal = st.form_submit_button(type='primary')

        if submit_internal:
            # Recolectar datos en listas
            parameter = [parameter1, parameter2, parameter3, parameter4, parameter5]
            significance = [significance1, significance2, significance3,
                            significance4, significance5]
            prob_low = [probability1[0], probability2[0], probability3[0],
                        probability4[0], probability5[0]]
            prob_high = [probability1[1], probability2[1], probability3[1],
                         probability4[1], probability5[1]]
            influencer1 = [influencer11, influencer21, influencer31, influencer41,
                           influencer51]
            influencer2 = [influencer12, influencer22, influencer32, influencer42,
                           influencer52]
            influencer3 = [influencer13, influencer23, influencer33, influencer43,
                           influencer53]
            # Crear un DataFrame con los datos recolectados
            dfi = pd.DataFrame({'environment': ['interno', 'interno', 'interno', 'interno', 'interno'],
                                'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high,
                                'influencer1': influencer1,
                                'influencer2': influencer2,
                                'influencer3': influencer3})
            # Mostrar un mensaje de éxito
            st.success("Tus datos han sido guardados. Puedes ver y editar los datos yendo a la página 'Editar datos'")

    # Si dfi no está en la sesión de estado
    if 'dfi' not in st.session_state:
        # Guardar dfi en la sesión de estado
        st.session_state.dfi = dfi
    else:
        # Actualizar dfi en la sesión de estado
        st.session_state.dfi = dfi

        # Agregar dfe (parámetros internos) si no existe en la sesión de estado
        if 'dfe' not in st.session_state:
            # Obtener dfe inicial
            dfe = initial_dfe()
            # Guardar dfe en la sesión de estado
            st.session_state.dfe = dfe

    # Llamar a la función parameters
    parameters()

    # Retornar dfi
    return dfi



def initial_dfe():
    dfe = pd.DataFrame({'environment': ['external', 'external', 'external', 'external', 'external'],
                        'parameter': ['None', 'None', 'None', 'None', 'None'],
                        'significance': ['muy alto', 'muy alto', 'muy alto', 'muy alto', 'muy alto'],
                        'prob_low': [45, 45, 45, 45, 45],
                        'prob_high': [55, 55, 55, 55, 55],
                        'influencer1': ['None', 'None', 'None', 'None', 'None'],
                        'influencer2': ['None', 'None', 'None', 'None', 'None'],
                        'influencer3': ['None', 'None', 'None', 'None', 'None']})
    return dfe

def initial_dfi():
    dfi = pd.DataFrame({'environment': ['internal', 'internal', 'internal', 'internal', 'internal'],
                        'parameter': ['None', 'None', 'None', 'None', 'None'],
                        'significance': ['muy alto', 'muy alto', 'muy alto', 'muy alto', 'muy alto'],
                        'prob_low': [45, 45, 45, 45, 45],
                        'prob_high': [55, 55, 55, 55, 55],
                        'influencer1': ['None', 'None', 'None', 'None', 'None'],
                        'influencer2': ['None', 'None', 'None', 'None', 'None'],
                        'influencer3': ['None', 'None', 'None', 'None', 'None']})
    return dfi

def parameters():
    # Función que une los DataFrames para los parámetros externos e internos
    # que afectan a la organización
    if 'dfe' in st.session_state and 'dfi' in st.session_state:
        df = pd.concat([st.session_state['dfe'], st.session_state['dfi']], axis=0)
    elif 'dfe' not in st.session_state and 'dfi' not in st.session_state:
        dfe = pd.DataFrame({'environment': [],
                            'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        dfi = pd.DataFrame({'environment': [],
                            'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([dfe, dfi], axis=0)
    elif 'dfe' not in st.session_state and 'dfi' in st.session_state:
        dfe = pd.DataFrame({'environment': [],
                            'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([dfe, st.session_state.dfi], axis=0)
    elif 'dfe' in st.session_state and 'dfi' not in st.session_state:
        dfi = pd.DataFrame({'environment': [],
                            'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([st.session_state.dfe, dfi], axis=0)
    else:
        df = None
        st.warning('Algo está mal')

    if df is not None:
        if 'df' not in st.session_state:
            st.session_state.df = df
        elif 'df' in st.session_state:
            st.session_state.df = df

    return df



def upload_file():
    with st.container():
        # Subir archivo que contiene parámetros internos y externos que afectan a la organización
        my_file = st.file_uploader('Cargue su archivo de **parámetros** (.csv)', type=['csv'])
        if my_file is not None:

            # Crear DataFrame a partir del archivo cargado
            df = pd.read_csv(my_file)
            if 'df' not in st.session_state:
                st.session_state.df = df
            else:
                st.session_state.df = df

            # Verificar que el archivo cargado esté correcto
            column_list = df.columns.tolist()

            if column_list == ['environment', 'parameter', 'significance', 'prob_low',
                               'prob_high', 'influencer1', 'influencer2', 'influencer3']:
                if len(df) == 10:
                    st.success("Su archivo se cargó correctamente. Para editar sus datos, vaya a la página 'Editar datos'")
            else:
                st.warning('Su archivo no tiene el formato correcto')


def edit_data():
    # Definir df - desde archivo cargado o desde la entrada de datos
    if 'df' in st.session_state:
        df = st.session_state.df
    else:
        df = parameters()

    # si df está vacío
    if df.shape == (0, 0):
        st.warning('No hay datos. Por favor ingrese datos en las páginas relevantes')

    df = st.data_editor(data=df, column_config={
                                            'significance': st.column_config.SelectboxColumn(
                                               'significance',
                                               options=['promedio', 'arriba del promedio', 'alto', 'muy alto']),
                                            'prob_low': st.column_config.SelectboxColumn(
                                                options=range(0, 100, 5)),
                                            'prob_high': st.column_config.SelectboxColumn(
                                                options=range(0, 100, 5)),
                                            },
                                     hide_index=True)

    st.session_state.df = df


# ANALIZAR
def analyze():
    # Verificar si df está en st.session
    if 'df' in st.session_state:
        df = st.session_state.df
    else:
        st.warning('Necesita ingresar sus datos para analizar su posición estratégica')

    dfa = df

    for i in range(len(df)):
        #my_list = ['average', 'above average', 'high', 'very high']
        my_list = ['promedio', 'arriba del promedio', 'alto', 'muy alto']
        #dfa['sig_code'] = my_list.index(dfa['significance'][i]) + 1
        dfa['sig_code'] = my_list.index(dfa['significance'].iloc[i]) + 1

    c = altair.Chart(dfa).mark_circle().encode(
        x=altair.X('prob_high', ).scale(zero=False),
        y=altair.Y('prob_low', ).scale(zero=False),

        color='parameter',
        size=altair.Size('significance', title='test'),
        )
    st.altair_chart(c, use_container_width=True)
    
    

def explanation():
    # Esta función presenta la información en la página 'Acerca de'
    with st.container():
        st.write('La planificación estratégica de T.I. es la piedra angular de cualquier organización '
                 'en su intento de prepararse para y abrazar las oportunidades y desafíos '
                 'del futuro. Este proceso significativo permite a los interesados '
                 'definir objetivos estratégicos, identificar posibles caminos y facilitar '
                 'un proceso de toma de decisiones proactivo. Esta aplicación'
                 'está destinada para el curso de Planeamiento Estratégico de TI (PETI), '
                 'para realizar un proceso estratégico tecnológico mediante:')
        st.write('* identificar las principales áreas que requieren atención')
        st.write('* desarrollar posibles caminos de escenarios')
        st.write('* promover decisiones estratégicas explícitas')
        st.markdown('___')

        st.write('Terminología:')
        st.write('PARÁMETROS EXTERNOS: Factores exógenos que afectan significativamente '
                 'la capacidad de la organización para alcanzar su visión y misión. '
                 'La organización tiene poco o ninguna influencia en estos parámetros.')
        st.write('PARÁMETROS INTERNOS: Parámetros dentro del ámbito de influencia de la '
                 'organización que afectan significativamente la capacidad de la organización '
                 'para alcanzar su visión y misión.')
        st.write('INFLUENCIADORES: Variables sujetas a decisiones por parte de la organización '
                 'que pueden influir en la capacidad para enfrentar/aprovechar los desafíos y '
                 'oportunidades presentados por los parámetros externos e internos.')
        st.markdown('___')







