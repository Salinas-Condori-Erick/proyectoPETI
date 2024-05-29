import streamlit as st
from modelos.PlanEstrategico import PlanEstrategico

def mision():

    st.title('1. Misión')

    st.write("""
    La MISIÓN es la razón de ser de la empresa/organización.
    - Debe ser clara, concisa y compartida.
    - Siempre orientada hacia el cliente no hacia el producto o servicio.
    - Refleja el propósito fundamental de la empresa en el mercado.
    """)

    st.write("""
    En términos generales describe la actividad y razón de ser de la organización y contribuye como una referencia permanente en el proceso de planificación estratégica.
    Se expresa a través de una oración que define el propósito fundamental de su existencia, estableciendo qué hace la empresa, por qué y para quién lo hace.
    """)

    st.header("Ejemplos")

    st.markdown("""
    **Empresa de servicios**  
    La gestión de servicios que contribuyen a la calidad de vida de las personas y generan valor para los grupos de interés.

    **Empresa productora de café**  
    Gracias a nuestro entusiasmo, trabajo en equipo y valores, queremos deleitar a todos aquellos que, en el mundo aman la calidad de vida, a través del mejor café que la naturaleza pueda ofrecer, ensalzado por las mejores tecnologías, por la emoción y la iluminación intelectual que nacen de la búsqueda de lo bello en todo lo que hacemos.

    **Agencia de certificación**  
    Dar a nuestros clientes avivamiento económico a través de la gestión de la Calidad, la Salud y la Seguridad, el Medio Ambiente y la Responsabilidad Social de sus activos, proyectos, productos y sistemas, obteniendo como resultado la capacidad para lograr la reducción de riesgos y la mejora de los resultados.
    """)

    if 'plan_seleccionado' in st.session_state:

        plan_est = PlanEstrategico()
        plan_id = st.session_state['plan_seleccionado']
        plan = plan_est.obtener_plan_por_id(plan_id)

        if plan:
            st.header("En este apartado describa la Misión de su empresa")
            nueva_mision = st.text_area("Ingrese la misión de su empresa", value=plan['Mision'], height=150)
            if st.button("Guardar Misión"):
                #funcion para guardar mision? o guardar todo? o enviar a form_editar_plan?
                st.success("Misión guardada con éxito!")

        else:
            st.error("No se encontró el Plan Estratégico.")
    else:
            st.error("No se ha seleccionado ningún plan estratégico.")




def vision():
    st.title('2. Visión')

    st.write("""
    La VISIÓN de una empresa define lo que la empresa/organización quiere lograr en el futuro.
    - Debe ser retadora, positiva, compartida y coherente con la misión.
    - Marca el fin último que la estrategia debe seguir.
    - Proyecta la imagen del destino que se pretende alcanzar.
    """)

    st.write("""
    En términos generales, describe la aspiración de la organización y actúa como una guía para el futuro. Se expresa a través de una oración que proyecta el estado futuro deseado, definiendo lo que la empresa aspira a ser, por qué y para quién.
    """)

    st.header("Ejemplos")

    st.markdown("""
    **Empresa de servicios**  
    Ser el grupo empresarial de referencia en nuestras áreas de actividad.

    **Empresa productora de café**  
    Queremos ser en el mundo el punto de referencia de la cultura y de la excelencia del café. Una empresa innovadora que propone los mejores productos y lugares de consumo que, gracias a ello, crece y se convierte en líder de la alta gama.

    **Agencia de certificación**  
    Ser líderes en nuestro sector y un actor principal en todos los segmentos de mercado en los que estamos presentes, en los mercados clave.
    """)

    if 'plan_seleccionado' in st.session_state:
        plan_est = PlanEstrategico()
        plan_id = st.session_state['plan_seleccionado']
        plan = plan_est.obtener_plan_por_id(plan_id)

        if plan:
            st.header("En este apartado describa la Visión de su empresa")
            nueva_vision = st.text_area("Ingrese la visión de su empresa", value=plan['Vision'], height=150)
            if st.button("Guardar Visión"):
                #funcion para guardar vision? o guardar todo? o enviar a form_editar_plan?
                st.success("Visión guardada con éxito!")

        else:
            st.error("No se encontró el Plan Estratégico.")
    else:
        st.error("No se ha seleccionado ningún plan estratégico.")






# def valores():




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