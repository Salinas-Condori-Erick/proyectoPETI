import streamlit as st
from modelos.PlanEstrategico import PlanEstrategico

# def mision():

# def vision():


def valores():
    st.title('3. Valores')

    st.write("""
    Los VALORES de una empresa son el conjunto de principios, reglas y aspectos culturales con los que se rige la organización. Son las pautas de comportamiento de la empresa y generalmente son pocos, entre 3 y 6. Son tan fundamentales y tan arraigados que casi nunca cambian.
    """)

    st.write("""
    Ejemplo de valores:
    - Integridad
    - Compromiso con el desarrollo humano.
    - Ética profesional
    - Responsabilidad social
    - Innovación
    - Etc.
    """)

    st.header("Ejemplos")

    st.markdown("""
    **Empresa de servicios**  
    - La excelencia en la prestación de servicios
    - La innovación orientada a la mejora continua de procesos productos y servicios.
    - La promoción del diálogo y compromiso con los grupos de interés.

    **Empresa productora de café**  
    - Nuestro valor es la búsqueda de la perfección o bien la pasión por la excelencia, entendida como amor por lo bello y bien hecho, la ética, entendida como construcción de valor en el tiempo a través de la sostenibilidad, la transparencia, y la valorización de las personas.

    **Agencia de certificación**  
    - Integridad y ética
    - Consejo y validación imparciales
    - Respeto por todas las personas
    - Responsabilidad social y medioambiental
    """)

    if 'plan_seleccionado' in st.session_state:
        plan_est = PlanEstrategico()

        #Listar Valores segun plan seleccionado
        valores = plan_est.obtener_valores_por_plan_id(st.session_state['plan_seleccionado'])

        if valores:
            st.header("En este apartado exponga los Valores de su empresa")
            for valor in valores:
                with st.form(key=str(valor['IdValor'])):  # Crear formulariocon key diferente
                    st.write(f"Valor: {valor['IdValor']}")
                    nueva_descripcion = st.text_area("Descripción:", value=valor['Descripcion'], key=f"desc_{valor['IdValor']}")
                    submit_button = st.form_submit_button("Guardar Cambios")

                    if submit_button:
                        st.success(f"Valor {valor['IdValor']} actualizado con éxito!")
                        #if plan_est.actualizar_valor(valor['IdValor'], nueva_descripcion):
                        #    st.success(f"Valor {valor['IdValor']} actualizado con éxito!")
                        #else:
                        #    st.error(f"Error al actualizar el valor {valor['IdValor']}.")


        ## Listar valores Sin Formulario
        #if valores:
        #        for valor in valores:
        #            st.text_area("Descripción del Valor", value=valor['Descripcion'], key=f"valor_{valor['IdValor']}")
        #        if st.button("Guardar Cambios"):
        #            # editar_valor
        #            st.success("Valores actualizados con éxito!")

        else:
            st.write("No se encontraron valores asociados a este plan.")



        # Formulario agregar_valor
        with st.form("new_value_form"):
            st.write("Agregar un nuevo valor:")
            nueva_descripcion = st.text_area("Descripción del nuevo valor")
            submit_new_value = st.form_submit_button("Agregar Valor")

            if submit_new_value:
                st.success("Nuevo valor agregado con éxito!")
                #if plan_est.agregar_valor(st.session_state['plan_seleccionado'], nueva_descripcion):
                #   st.success("Nuevo valor agregado con éxito!")
                #else:
                #    st.error("Error al agregar el valor.")



    else:
        st.error("No se ha seleccionado ningún plan estratégico.")









def gestion_planes():
    st.title("Mis Planes Estratégicos")
    plan_est = PlanEstrategico()

    if st.sidebar.button("Agregar Plan Estrategico"):
        form_agregar_plan(st.session_state['user_id'])

    st.sidebar.button("Volver")

    planes = plan_est.listar_planes_por_id_usuario(st.session_state['user_id'])
    for plan in planes:
        with st.expander(f" {plan[1]}"):
            st.write(f"Empresa: {plan[2]}")

            #Opciones de editar y eliminar planes V2
            action = st.selectbox(f"Seleccione acción para {plan[1]}", ['Editar', 'Eliminar'], key=f"action_{plan[0]}")
            
            if st.button("Confirmar Acción", key=f"confirm_{plan[0]}"):
                if action == 'Editar':
                    form_editar_plan(plan[0])
                elif action == 'Eliminar':
                    if plan_est.eliminar_plan(plan[0]):
                        st.success(f"Plan {plan[1]} eliminado correctamente.")
                    else:
                        st.error(f"No se pudo eliminar el plan {plan[1]}.")

            #Opciones de editar y eliminar planes V1
            #if st.button(f"Editar {plan[1]}"):
            #    # form_editar_plan()
            #    print("form_editar_plan")## en lugar de ejecutar el boton parece q se actualiza la pagina y no envia los datos para procesarlos
            #    form_editar_plan(plan[0])
            #    #st.write(f"Editar el plan {plan[1]}")

            #if st.button(f"Eliminar {plan[1]}"):
            #    # funcion de eliminar()
            #    st.write(f"Eliminar el plan {plan[1]}")
    st.stop()



def form_editar_plan(id_plan):
    st.title("Editar Plan Estratégico")
    plan_est = PlanEstrategico()

    plan = plan_est.obtener_plan_por_id(id_plan)
    if plan:
        with st.form("form_plan"):
            st.write(f"Editando el plan: {plan['Nombre']} (ID: {id_plan})")
            nombre = st.text_input("Nombre del Plan", value=plan['Nombre'])
            empresa = st.text_input("Empresa", value=plan['Empresa'])
            mision = st.text_area("Misión", value=plan['Mision'])
            vision = st.text_area("Visión", value=plan['Vision'])
            
            if st.form_submit_button("Actualizar Plan"):
                if plan_est.actualizar_plan(id_plan, nombre, empresa, mision, vision):
                    st.success("Plan actualizado correctamente.")
                else:
                    st.error("Error al actualizar el plan.")
    else:
        st.error("No se encontró el Plan Estratégico.")


    #with st.form("form_plan"):
    #    id_plan = st.number_input("ID del Plan Estratégico", min_value=1, format='%d')
    #    if st.form_submit_button("Buscar Plan"):
    #        plan = plan_est.obtener_plan_por_id(id_plan)
    #        if plan:
    #            nombre = st.text_input("Nombre del Plan", value=plan['Nombre'])
    #            empresa = st.text_input("Empresa", value=plan['Empresa'])
    #            mision = st.text_area("Misión", value=plan['Mision'])
    #            vision = st.text_area("Visión", value=plan['Vision'])
    #            if st.form_submit_button("Actualizar Plan"):
    #                if plan_est.actualizar_plan(id_plan, nombre, empresa, mision, vision):
    #                    st.success("Plan actualizado correctamente.")
    #                else:
    #                    st.error("Error al actualizar el plan.")
    #        else:
    #            st.error("No se encontró el Plan Estratégico.")



def form_agregar_plan(id_usuario):#id_usuario
    st.title("Agregar Plan Estratégico")
    plan_est = PlanEstrategico()

    st.sidebar.button("Volver")

    with st.form("form_agregar_plan"):
        nombre = st.text_input("Nombre del Plan")
        empresa = st.text_input("Empresa")
        mision = st.text_area("Misión")
        vision = st.text_area("Visión")
        if st.form_submit_button("Crear Plan"):
            resultado = plan_est.agregar_plan(nombre, empresa, mision, vision, id_usuario)#id_usuario
            if resultado:
                st.success("Plan añadido correctamente.")
            else:
                st.error("Error al añadir el plan.")
    st.stop()






############################################################################################################
'''
def mostrar_planes_usuario():
    if 'authenticated' in st.session_state and st.session_state['authenticated']:
        planes = obtener_planes_por_usuario_id(st.session_state['user_id'])  # Función hipotética que busca planes por ID de usuario
        for plan in planes:
            st.write(plan['Nombre'], plan['Mision'])
    else:
        st.error("Por favor, inicia sesión para ver tus planes.")


def actualizar_plan_form(id_plan):
    plan = obtener_plan_por_id(id_plan)
    if plan:
        with st.form("update_plan_form", clear_on_submit=False):
            nombre = st.text_input("Nombre del Plan", value=plan['Nombre'])
            mision = st.text_area("Misión", value=plan['Mision'])
            vision = st.text_area("Visión", value=plan['Vision'])
            submitted = st.form_submit_button("Actualizar")
            if submitted:
                resultado = actualizar_plan(id_plan, nombre, mision, vision)  # Suponiendo que esta función existe
                if resultado:
                    st.success("Plan actualizado correctamente.")
                else:
                    st.error("Error al actualizar el plan.")
    else:
        st.error("Plan no encontrado.")
'''