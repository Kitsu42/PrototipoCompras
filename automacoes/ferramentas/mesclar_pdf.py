import streamlit as st
from PyPDF2 import PdfMerger
import tempfile

def mesclar_pdf_page():
    st.header("📎 Mesclar PDFs")

    arquivos = st.file_uploader(
        "Envie os PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if arquivos and st.button("Mesclar PDFs"):
        merger = PdfMerger()

        for pdf in arquivos:
            merger.append(pdf)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            merger.write(tmp.name)
            merger.close()

            st.success("PDF mesclado com sucesso!")
            with open(tmp.name, "rb") as f:
                st.download_button(
                    "📥 Baixar PDF",
                    f,
                    file_name="PDF_Mesclado.pdf",
                    mime="application/pdf"
                )
