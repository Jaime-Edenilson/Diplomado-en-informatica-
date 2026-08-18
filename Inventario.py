import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventario Escolar")

st.title("📚 Inventario Escolar")

if "inventario" not in st.session_state:
    st.session_state.inventario = []

producto = st.text_input("Producto")
precio = st.number_input("Precio", min_value=0.0, step=0.01)
cantidad = st.number_input("Cantidad", min_value=1)

if st.button("Agregar"):
    if producto:
        st.session_state.inventario.append({
            "Producto": producto,
            "Precio": precio,
            "Cantidad": cantidad,
            "Total": precio * cantidad
        })
        st.success("Producto agregado.")
    else:
        st.warning("Debes escribir un producto.")

st.divider()

if st.session_state.inventario:

    df = pd.DataFrame(st.session_state.inventario)

    st.subheader("📊 Dashboard del inventario")
    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Productos", len(df))
    col2.metric("Unidades", df["Cantidad"].sum())
    col3.metric("Valor total", f"${df['Total'].sum():.2f}")

    if st.button("🗑️ Limpiar inventario"):
        st.session_state.inventario = []
        st.rerun()

else:
    st.info("No hay productos registrados.")