import streamlit as st

st.title("Calculadora basica")
numero1=st.number_input("ingrese un numero", value=0)
numero2=st.number_input("ingrese OTRO numero", value=0)

operacion=st.selectbox("Seleccione la operacion", ["Suma","Resta","Division","Multiplicacion"])
if st.button("Calcular"):
    if operacion=="Suma":
        st.success(numero1+numero2)
    elif operacion=="Resta":
        st.success(numero1-numero2)
    elif operacion=="Multiplicacion":
        st.success(numero1*numero2)
    elif operacion=="Division":
        st.success(numero1/numero2)
        if numero2 !=0:
            st.success(numero1/numero2)
        else:
            st.error("No se puede dividir entre 0")
