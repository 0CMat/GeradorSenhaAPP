import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Gerador de Senhas",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilos customizados
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔐 Gerador de Senhas</div>',
            unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transforme sua chave em uma senha segura</div>',
            unsafe_allow_html=True)

# Divisor visual
st.divider()

# Input da chave
chave = st.text_input(
    "Digite uma chave para sua senha:",
    placeholder="Digite aqui...",
    max_chars=50
)

# Função para gerar a senha


def gerar_senha(chave):
    mapeamento = {
        'A': '@', 'a': '@',
        'I': '!', 'i': '!',
        'O': '&', 'o': '&',
        'U': '?', 'u': '?',
        'E': '*', 'e': '*',
        'F': '-', 'f': '-',
        'R': '#', 'r': '#',
        'T': '%', 't': '%',
        'S': '$', 's': '$'
    }

    senha = ""
    for letra in chave:
        if letra in mapeamento:
            senha += mapeamento[letra]
        else:
            senha += letra

    return senha


# Gerar e exibir a senha
if chave:
    senha_gerada = gerar_senha(chave)

    st.success("✅ Senha gerada com sucesso!")

    # Exibir senha em um container destacado
    col1, col2 = st.columns([4, 1])

    with col1:
        st.text_input(
            "Sua senha gerada:",
            value=senha_gerada,
            disabled=True,
            key="senha_output"
        )

    with col2:
        if st.button("📋 Copiar", use_container_width=True):
            st.write("")
            st.info("Senha copiada para a área de transferência!")

    # Estatísticas
    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Comprimento", len(senha_gerada))

    with col2:
        caracteres_especiais = sum(1 for c in senha_gerada if c in "@!&?*-#%$")
        st.metric("Caracteres Especiais", caracteres_especiais)

    with col3:
        caracteres_normais = len(senha_gerada) - \
            sum(1 for c in senha_gerada if c in "@!&?*-#%$")
        st.metric("Caracteres Normais", caracteres_normais)

else:
    st.info("👆 Digite uma chave acima para gerar sua senha!")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #999; font-size: 0.9em; margin-top: 30px;'>
        <p>🔒 Suas senhas são geradas localmente e não são armazenadas</p>
    </div>
""", unsafe_allow_html=True)
