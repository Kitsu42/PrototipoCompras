import streamlit as st

def gerar_links_page():
    st.header("🔗 Gerar links de pesquisa")

    entrada = st.text_area(
        "Cole os números (um por linha):",
        height=200
    )

    if st.button("Gerar links"):
        base_url = "https://sistemas.grupotecnoseg.com.br/suprimentos/redirect_to_rc/"
        numeros = [linha.strip() for linha in entrada.splitlines() if linha.strip()]

        st.subheader("Resultado:")
        for num in numeros:
            st.write(base_url + num)
