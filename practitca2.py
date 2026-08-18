import streamlit as st

st.title("Practica 2")
numero1=st.number_input("ingrese un numero", value=0)
numero2=st.number_input("ingrese OTRO numero", value=0)

resultado=numero1+numero2
st.write ("El resultado es", resultado)


