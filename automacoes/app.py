import streamlit as st
from ferramentas.gerar_links import gerar_links_page
from ferramentas.mesclar_pdf import mesclar_pdf_page

st.set_page_config(page_title="Ferramentas Internas", layout="wide")

st.title("🛠️ Ferramentas Internas")

opcao = st.sidebar.selectbox(
    "Escolha a ferramenta:",
    ["Gerar links", "Mesclar PDFs"]
)

if opcao == "Gerar links":
    gerar_links_page()
elif opcao == "Mesclar PDFs":
    mesclar_pdf_page()
