import streamlit as st
import os

# Configurações iniciais
st.set_page_config(page_title="Escala dos MESCE", page_icon="☁️")
PASTA_ARQUIVOS = "arquivos_armazenados"

if not os.path.exists(PASTA_ARQUIVOS):
    os.makedirs(PASTA_ARQUIVOS)

# 1. Sistema de Senha Simples
st.sidebar.title("🔐 Login")
senha_digitada = st.sidebar.text_input("Insira a senha:", type="password")

if senha_digitada != "mesce": # <--- MUDE SUA SENHA AQUI
    st.warning("Aguardando senha correta para liberar acesso...")
    st.stop()

st.title("☁️ Escala dos MESCE")

# 2. Área de Upload (Celular -> Nuvem)
st.subheader("📤 Enviar arquivo")
arquivo_enviado = st.file_uploader("Escolha um arquivo do seu celular")

if arquivo_enviado is not None:
    with open(os.path.join(PASTA_ARQUIVOS, arquivo_enviado.name), "wb") as f:
        f.write(arquivo_enviado.getbuffer())
    st.success(f"Arquivo '{arquivo_enviado.name}' salvo com sucesso!")

st.divider()

# 3. Área de Download (Nuvem -> Celular)
st.subheader("📥 Arquivos Disponíveis")
arquivos = os.listdir(PASTA_ARQUIVOS)

if not arquivos:
    st.info("A pasta está vazia.")
else:
    for arquivo in arquivos:
        caminho = os.path.join(PASTA_ARQUIVOS, arquivo)
        with open(caminho, "rb") as f:
            st.download_button(
                label=f"⬇️ Baixar {arquivo}",
                data=f,
                file_name=arquivo,
                key=arquivo # Chave única para o Streamlit
            )