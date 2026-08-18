import pandas as pd
import streamlit as st

st.set_page_config(page_title="Inventario Escolar")

st.title("📚 Inventario Escolar")

# Crear el inventario si no existe
if "inventario" not in st.session_state:
    st.session_state.inventario = []

st.subheader("Agregar productos")

# Formulario
with st.form("form_inventario", clear_on_submit=True):

    producto = st.text_input("Escribe el producto")

    precio = st.number_input(
        "Escribe el precio del producto",
        min_value=0.0,
        step=0.01,
        format="%.2f"
    )

    cantidad = st.number_input(
        "Escribe la cantidad del producto",
        min_value=1,
        step=1
    )

    agregar = st.form_submit_button("Agregar al inventario")

    if agregar:
        if producto.strip() == "":
            st.warning("Debes escribir un producto.")
        else:
            total = precio * cantidad

            st.session_state.inventario.append({
                "Producto": producto,
                "Precio": precio,
                "Cantidad": cantidad,
                "Total": total
            })

            st.success(f"'{producto}' agregado al inventario.")

st.divider()

# Mostrar inventario
if st.session_state.inventario:

    st.subheader("Inventario")

    encabezado = st.columns([3, 2, 2, 2])
    encabezado[0].markdown("**Producto**")
    encabezado[1].markdown("**Cantidad**")
    encabezado[2].markdown("**Precio**")
    encabezado[3].markdown("**Total**")

    total_general = 0

    for item in st.session_state.inventario:

        fila = st.columns([3, 2, 2, 2])

        fila[0].write(item["Producto"])
        fila[1].write(item["Cantidad"])
        fila[2].write(f"${item['Precio']:.2f}")
        fila[3].write(f"${item['Total']:.2f}")

        total_general += item["Total"]

    st.divider()

    st.metric(
        "Total general del inventario",
        f"${total_general:.2f}"
    )

    if st.button("🗑️ Limpiar inventario"):
        st.session_state.inventario.clear()
        st.rerun()

else:
    st.info("No hay productos en el inventario.")
