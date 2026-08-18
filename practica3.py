import streamlit as st

st.title("Calcular descuentos")

producto=st.text_input("Escribe el producto")
precio=st.number_input("Escribe el precio del producto", min_value=0)
if st.button ("Calcular total"):
    if precio>=50:
        descuento=precio*0.20
    else:
        descuento=0
    total=precio-descuento

    st.write("Producto", producto)
    st.write("Precio", precio)
    st.write("Descuento", descuento)
    st.write("Total a pagar", total)