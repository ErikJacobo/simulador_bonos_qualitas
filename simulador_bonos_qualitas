import streamlit as st

def formato_pesos(valor):
    return "${:,.2f}".format(valor)

st.set_page_config(page_title="Simulador Quálitas 2025", layout="centered")

# Estilo general
st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Quálitas 2025</h3>", unsafe_allow_html=True)

# Campo nombre
nombre = st.text_input("Nombre del Agente")

# Entradas
produccion_2024 = st.number_input("Producción 2024 ($)", min_value=0.0, format="%.2f")
produccion_2025 = st.number_input("Producción 2025 ($)", min_value=0.0, format="%.2f")
polizas_emitidas = st.number_input("Pólizas individuales emitidas (emisión delegada)", min_value=0, step=1)

# Calcular
if st.button("Calcular Bonos"):
    total_bono = 0
    st.markdown("---")
    st.markdown(f"### 🧾 Resultado para {nombre if nombre else 'el agente'}")

    # Datos ingresados
    st.markdown("#### 📊 Datos Ingresados:")
    st.markdown(f"- Producción 2024: {formato_pesos(produccion_2024)}")
    st.markdown(f"- Producción 2025: {formato_pesos(produccion_2025)}")

    if produccion_2024 > 0:
        crecimiento = ((produccion_2025 - produccion_2024) / produccion_2024) * 100
        st.markdown(f"- Crecimiento Real: {crecimiento:.2f}%")
    else:
        crecimiento = None
        st.markdown("- Crecimiento Real: No calculado (falta producción 2024)")

    st.markdown(f"- Pólizas Emitidas: {polizas_emitidas}")

    # Resultados de bonos
    st.markdown("#### 💵 Resultados de Bono:")

    # BONO PRODUCCIÓN
    bono_prod = 0
    if produccion_2025 >= 300000:
        if produccion_2025 <= 500000:
            porc_prod = 0.01
        elif produccion_2025 <= 1250000:
            porc_prod = 0.02
        elif produccion_2025 <= 2100000:
            porc_prod = 0.03
        elif produccion_2025 <= 3300000:
            porc_prod = 0.04
        elif produccion_2025 <= 5100000:
            porc_prod = 0.05
        else:
            porc_prod = 0.06

        bono_prod = produccion_2025 * porc_prod
        total_bono += bono_prod
        st.markdown(f"- Bono de Producción: **{porc_prod*100:.2f}%** → {formato_pesos(bono_prod)} ✅ Aplica bono del {int(porc_prod*100)}%.")
    else:
        st.markdown("- Bono de Producción: ❌ No aplica — Producción 2025 menor a $300,000.")

    # BONO CRECIMIENTO
    bono_crec = 0
    if crecimiento is not None:
        if crecimiento >= 5:
            if crecimiento <= 10:
                porc_crec = 0.01
            elif crecimiento <= 15:
                porc_crec = 0.02
            elif crecimiento <= 20:
                porc_crec = 0.03
            elif crecimiento <= 25:
                porc_crec = 0.04
            else:
                porc_crec = 0.05
            bono_crec = (produccion_2025 - produccion_2024) * porc_crec
            total_bono += bono_crec
            st.markdown(f"- Bono de Crecimiento: **{porc_crec*100:.2f}%** → {formato_pesos(bono_crec)} ✅ Aplica bono del {int(porc_crec*100)}%.")
        else:
            st.markdown(f"- Bono de Crecimiento: ❌ No aplica — Crecimiento de {crecimiento:.2f}% menor al 5%.")
    else:
        st.markdown("- Bono de Crecimiento: ❌ No aplica — Se necesita producción 2024 para comparar.")

    # BONO EMISIÓN DELEGADA
    bono_emision = 0
    if produccion_2025 >= 500000:
        bono_emision = polizas_emitidas * 100
        total_bono += bono_emision
        st.markdown(f"- Bono por Emisión Delegada: {formato_pesos(bono_emision)} ✅ Aplica — Cumple con producción mínima anual.")
    else:
        st.markdown("- Bono por Emisión Delegada: ❌ No aplica — Se requiere al menos $500,000 en producción 2025.")

    # Total
    st.markdown("#### 🧮 Total del Bono:")
    st.markdown(f"### {formato_pesos(total_bono)}")

    # Pie
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Aplican restricciones y condiciones conforme al cuaderno oficial de <strong>Quálitas 2025</strong>.</p>", unsafe_allow_html=True)
