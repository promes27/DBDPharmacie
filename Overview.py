import streamlit as st
from datetime import date



# Sidebar
with st.sidebar:
    st.sidebar.image("images/logoMahein.png", caption="", use_container_width=True)

# Charger le fichier CSS
with open("./style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.container():
    # Création des colonnes
    col1, col2 = st.columns([5, 2])  # largeur proportionnelle (ajuste si besoin)

    with col1:
        st.markdown('<h1 class="title">Overview</h1>', unsafe_allow_html=True)

    with col2:
        date_min_possible = date(2023, 1, 1)
        date_max_possible = date(2025, 12, 31)

        plage_dates = st.date_input(
            "",
            value=(date(2024, 1, 1), date(2024, 12, 31)),  
            min_value=date_min_possible,
            max_value=date_max_possible
        )
