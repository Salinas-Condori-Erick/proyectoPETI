import streamlit as st

def introduccion():
    st.title('Cómo Elaborar un Plan Estratégico')

    st.write("""
    El éxito de las organizaciones reside en gran parte en la capacidad que tienen sus directivos en ejecutar una estrategia más que en la calidad de la estrategia en sí. Su planificación y asignación de recursos son fundamentales para el logro de la misma. En este sentido, un Plan Estratégico puede entenderse como el conjunto de acciones que han de llevarse a cabo para alinear los recursos y potencialidades al objeto de conseguir el estado deseado, es decir, adaptación y adquisición de competitividad empresarial.
    """)

    st.write("""
    Esta aplicación le ayudará a reflexionar sobre la estrategia que debe llevar a cabo. Visualizará dónde quiere estar, dónde está actualmente y, qué camino tendrá que trazar para llevarle a otro estado.
    """)

    st.header("Para visualizar dónde quiere estar su empresa tendrá que definir:")
    st.write("1. Misión")
    st.write("2. Visión")
    st.write("3. Valores")

    st.header("Para entender dónde está tendrá que llevar a cabo un doble análisis:")
    st.write("1. Análisis interno")
    st.write("2. Análisis externo")

    st.header("Para trazar el camino de un punto a otro tendrá que:")
    st.write("1. Identificar la estrategia más conveniente")
    st.write("2. Determinar acciones para el facilitar el logro de la estrategia")

    st.markdown("Gracias al Plan Empresarial determinará la forma de lograr una ventaja competitiva para su proyecto de inversión.")


def recomendaciones():
    st.header('Recomendaciones')
    st.write("""
    1. Antes que nada, haz una copia de este fichero y guárdala.
    2. Antes de ponerte a trabajar con la aplicacion, echa una mirada general a su funcionamiento y contenido.
    3. Intente responder y reflexionar sobre el mayor número de apartados posibles. Tómese el tiempo que estime necesario.
    4. Durante el recorrido haya botones para facilitar la movilidad entre las distintas secciones.
    5. Se recomienda utilizar las herramientas "Estudio de Mercado", "Plan de Marketing", "Plan de Comunicación", "Plan de negocio" y "Plan Económico-Financiero" de uso libre y gratuito.
    6. En caso de duda, ponte en contacto con el especialista.
    7. Si tiene alguna sugerencia, comentario o detectas algún error en este producto, por favor, ponte en contacto con nosotros email1, email2, email3.
    """)


def manejo_aplicacion():
    st.header('Manejo de la Aplicación')
    st.write("""
    1. Todas las hojas y el libro están protegidos pero no tienen password.
    2. La aplicación dispone de ejemplos y de información a modo de consulta.
    3. El resultado final será la obtención de un Resumen Ejecutivo de su Plan Estratégico de su empresa.
    4. Al final de cada fase visualizará un apartado resumen, bordeado en color "azul", que será el que se trasladará al resumen ejecutivo del "Plan Estratégico". De esta manera, una vez haya realizado el recorrido completo ud. dispondrá del resumen ejecutivo de su Plan Estratégico, listo para su impresión. Tenga especial cuidado en su redacción y cerciórese de que en el mismo se recogen los aspectos más significativos que considere aptos para mencionar en el informe final.
    5. Cada hoja de la aplicación (formato excel) está configurada para que se pueda imprimir. Si usted modifica el ancho de las columnas y/o añade alguna nueva, recuerde que deberá ajustar la configuración de nuevo antes de su impresión. Es aconsejable que antes de imprimir el resumen ejecutivo del plan Estratégico, recurra a la "vista preliminar" para asegurarse de que la configuración es correcta.
    """)

    st.markdown("""
    El usuario de este proyecto puede usarlo y modificarlo como desee para su uso personal o profesional pero no puede distribuirlo públicamente, comerciar con él, usarlo para crear productos destinados a la venta o arrogarse su autoría total o parcial sin el permiso previo y por escrito.
    """)
    st.markdown("""
    Por último, No imprima aquello que no le resulte necesario, así contribuirá a la conservación de los recursos naturales.
    """)
