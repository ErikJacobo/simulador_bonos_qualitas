import streamlit as st
from PIL import Image

# Función para formato de pesos
def formato_pesos(valor):
    return "${:,.2f}".format(valor)

st.set_page_config(page_title="Simulador Quálitas 2025", layout="centered")

# Carga de logo
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("<h1 style='text-align: left;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Quálitas 2025</h3>", unsafe_allow_html=True)
with col2:
    logo = Image.open("link logo.jpg")
    st.image(logo, width=90)

# Entrada de datos
nombre = st.text_input("Nombre del Agente")
produccion_2024 = st.number_input("Producción 2024 ($)", min_value=0.0, format="%.2f")
produccion_2025 = st.number_input("Producción 2025 ($)", min_value=0.0, format="%.2f")
polizas_emitidas = st.number_input("Pólizas individuales emitidas (emisión delegada)", min_value=0, step=1)

# Calcular
if st.button("Calcular Bonos"):
    total_bono = 0
    st.markdown("---")
    st.markdown(f"### 📋 Resultado para {nombre if nombre else 'el agente'}")

    # Datos ingresados
    st.markdown("#### 📊 Datos Ingresados:")
    st.markdown(f"- Producción 2024: **{formato_pesos(produccion_2024)}**")
    st.markdown(f"- Producción 2025: **{formato_pesos(produccion_2025)}**")
    if produccion_2024 > 0:
        crecimiento = ((produccion_2025 - produccion_2024) / produccion_2024) * 100
        st.markdown(f"- Crecimiento Real: **{crecimiento:.2f}%**")
    else:
        crecimiento = None
        st.markdown("- Crecimiento Real: No calculado (falta producción 2024)")
    st.markdown(f"- Pólizas Emitidas: **{polizas_emitidas}**")

    # Resultados
    st.markdown("#### 💵 Resultados de Bono:")

    # Bono Producción
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
        st.markdown(f"🧾 **Bono de Producción:** {porc_prod*100:.2f}% → **{formato_pesos(bono_prod)}**")
        st.markdown(f"✅ Aplica bono del {int(porc_prod*100)}% sobre producción 2025.")
    else:
        st.markdown("🧾 **Bono de Producción:** ❌ No aplica.")
        st.markdown("⛔ Producción 2025 menor a $300,000.")

    # Bono Crecimiento
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
            st.markdown(f"📈 **Bono de Crecimiento:** {porc_crec*100:.2f}% → **{formato_pesos(bono_crec)}**")
            st.markdown(f"✅ Crecimiento del {crecimiento:.2f}% — Aplica bono del {int(porc_crec*100)}%.")
        else:
            st.markdown(f"📈 **Bono de Crecimiento:** ❌ No aplica.")
            st.markdown(f"⛔ Crecimiento del {crecimiento:.2f}% menor al 5%.")
    else:
        st.markdown("📈 **Bono de Crecimiento:** ❌ No aplica.")
        st.markdown("⛔ Se requiere producción 2024 para calcular crecimiento.")

    # Bono Emisión Delegada
    bono_emision = 0
    if produccion_2025 >= 500000:
        bono_emision = polizas_emitidas * 100
        total_bono += bono_emision
        st.markdown(f"📄 **Bono por Emisión Delegada:** {polizas_emitidas} x $100 → **{formato_pesos(bono_emision)}**")
        st.markdown("✅ Aplica — Cumple con producción mínima anual de $500,000.")
    else:
        st.markdown("📄 **Bono por Emisión Delegada:** ❌ No aplica.")
        st.markdown("⛔ Producción 2025 menor a $500,000.")

    # Total
    st.markdown("#### 🧮 Total del Bono:")
    st.markdown(f"### {formato_pesos(total_bono)}")

    # Pie
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Aplican restricciones y condiciones conforme al cuaderno oficial de <strong>Quálitas 2025</strong>.</p>", unsafe_allow_html=True)
