import streamlit as st

image = 'src/img/neurona.jpg'
st.image(image, caption='Neurona')

st.title("¡Hola neurona!")
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:

    st.header("Una entrada")
    # Input bar 1
    x = st.number_input("Entrada")
    w = st.slider('peso', 0.0, 5.0)

    if st.button("Calcular la salida", key='salida1'):
        y = x * w
        st.text(f"El resultado es {y}")

with tab2:


    st.header("Dos entradas")
    # Input bar 1
    col1, col2 = st.columns(2)

    with col1:
        x0 = st.number_input("Entrada 1", key='x1')
        w0 = st.slider('peso 1', 0.0, 5.0, key='w1')
    
    with col2:
        x1 = st.number_input("Entrada 2", key='x2')
        w1 = st.slider('peso 2', 0.0, 5.0, key='w2')

    if st.button("Calcular la salida", key='salida2'):
        y = x0 * w0 + x1 * w1
        st.text(f"El resultado es {y}")

with tab3:

    st.header("Tres entradas y sesgos")
    # Input bar 1
    col1, col2, col3 = st.columns(3)

    with col1:
        x0 = st.number_input("Entrada 1", key='x11')
        w1 = st.slider('peso 1', 0.0, 5.0, key='w11')

    with col2:
        x1 = st.number_input("Entrada 2", key='x12')
        w0 = st.slider('peso 2', 0.0, 5.0, key='w12')

    with col3:
        x2 = st.number_input("Entrada 3", key='x13')
        w2 = st.slider('peso 3', 0.0, 5.0, key='w13')


    b = st.number_input("Introduzca el valor del sesgo")

# Display the entered name
    if st.button("Calcular la salida", key='salida3'):

        y = x0 * w0 + x1 * w1 + x2 * w2 + b

        st.text(f"El resultado es {y}")

