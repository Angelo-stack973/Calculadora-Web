import streamlit as st

st.title("🧮 Calculadora Web con Python")

# Entradas numéricas
num1 = st.number_input("Ingresa el primer número:", value=0 )
num2 = st.number_input("Ingresa el segundo número:", value=0 )

#Botones en horizontal
col1, col2, col3, col4 = st.columns(4)
#Botones para los cálculos
with col1:
    if st.button("Sumar"):
        suma = num1 + num2
        st.success(f"El resultado es: {suma}")
with col2:
    if st.button("Restar"):
        resta = num1 - num2
        st.success(f"El resultado es: {resta}")
with col3:
    if st.button("Multiplicar"):
        multiplicacion = num1 * num2
        st.success(f"El resultado es: {multiplicacion}")
with col4:
    if st.button("Dividir"):
        if num2 != 0:
            division = num1 / num2
            st.success(f"El resultado es: {division}")
        else:
            st.error("Error: No se puede dividir entre cero.")