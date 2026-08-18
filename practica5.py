
import streamlit as st

st.set_page_config(page_title="Inventario Escolar")

st.title("📚 Inventario Escolar")

# Crear inventario si no existe
if "inventario" not in st.session_state:
    st.session_state.inventario = []

# Formulario para agregar productos
with st.form("form_inventario", clear_on_submit=True):
    producto = st.text_input("Producto")
    precio = st.number_input("Precio", min_value=0.0, step=0.01, format="%.2f")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    agregar = st.form_submit_button("Agregar")

    if agregar:
        if producto.strip():
            st.session_state.inventario.append({
                "Producto": producto,
                "Precio": precio,
                "Cantidad": cantidad,
                "Total": precio * cantidad
            })
            st.success(f"{producto} agregado.")
        else:
            st.warning("Debes escribir un producto.")

st.divider()

# Mostrar inventario

if st.session_state.inventario:

    st.subheader("Inventario")
    total_general = sum(item["Total"] for item in st.session_state.inventario)

    for item in st.session_state.inventario:
        st.write(
            f"**{item['Producto']}** | Cantidad: {item['Cantidad']} | "
            f"Precio: ${item['Precio']:.2f} | Total: ${item['Total']:.2f}"
        )

    st.metric("Total general", f"${total_general:.2f}")

    if st.button("🗑️ Limpiar inventario"):
        st.session_state.inventario.clear()
        st.rerun()

else:
    st.info("No hay productos en el inventario.")
