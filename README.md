# 🔐 Gerador de Senhas com Streamlit

Um aplicativo web interativo que transforma uma chave em uma senha segura através de mapeamento de caracteres.

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar a Aplicação

```bash
streamlit run codigo-fonte/app.py
```

A aplicação abrirá automaticamente no seu navegador padrão em `http://localhost:8501`.

## 📋 Funcionalidades

- **Conversão Automática**: Converte letras específicas em caracteres especiais
- **Interface Intuitiva**: Design limpo e responsivo
- **Estatísticas**: Mostra métricas sobre a senha gerada
- **Tabela de Conversão**: Visualize como cada letra é convertida

## 🔤 Tabela de Mapeamento

| Letra | Símbolo |
|-------|---------|
| A/a   | @       |
| I/i   | !       |
| O/o   | &       |
| U/u   | ?       |
| E/e   | *       |
| F/f   | -       |
| R/r   | #       |
| T/t   | %       |
| S/s   | $       |

## 📝 Exemplo

**Entrada:** `Python`  
**Saída:** `Py%h&n`

## 🔒 Segurança

Suas senhas são geradas completamente no lado do cliente. Nenhuma informação é armazenada ou enviada para servidores.

## 📂 Estrutura do Projeto

```
GeradorSenhaAPP/
├── codigo-fonte/
│   ├── gerador_senhas_v2.py    (Script original)
│   └── app.py                  (Frontend Streamlit)
└── requirements.txt            (Dependências)
```
