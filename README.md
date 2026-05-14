# Calculadora Simples em Streamlit

Uma calculadora básica desenvolvida com Python e Streamlit que realiza as quatro operações matemáticas fundamentais: adição, subtração, multiplicação e divisão.

## 📋 Descrição

Este projeto implementa uma calculadora interface usando o framework Streamlit. A aplicação permite aos usuários realizar cálculos básicos com uma interface intuitiva semelhante às calculadoras tradicionais.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **Streamlit**: Framework para criação da interface web
- **HTML/CSS**: Para estilização customizada dos componentes

## 🚀 Como Executar

1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   streamlit run calculadora.py
   ```
4. Acesse o aplicativo no seu navegador (geralmente em http://localhost:8501)

## 📱 Funcionalidades

- Interface limpa e responsiva
- Botões numéricos (0-9)
- Operações básicas: +, -, *, /
- Botão de limpar (C)
- Botão de igual (=)
- Tratamento de erro para divisão por zero
- Formatação automática de resultados (remove zeros desnecessários)
- Feedback visual interativo nos botões

## 🧪 Testes

O projeto inclui testes unitários para garantir o funcionamento correto:
- `test_calculadora.py`: Testes para a lógica da calculadora
- `test_api.py`: Testes para a API (se aplicável)
- `test_dodf_extractor.py`: Testes para extrator de DODF (Documento Oficial do Distrito Federal)

## 📁 Estrutura do Projeto

```
calculadora_paperclip/
├── calculadora.py          # Aplicação principal Streamlit
├── api.py                 # API (se aplicável)
├── dodf_extractor.py      # Extrator de DODF
├── requirements.txt       # Dependências do projeto
├── test_calculadora.py    # Testes da calculadora
├── test_api.py            # Testes da API
├── test_dodf_extractor.py # Testes do extrator de DODF
├── README.md              # Este arquivo
└── memory/                # Pasta de memória (se aplicável)
```

## ⚠️ Observações

- A aplicação usa `st.session_state` para gerenciar o estado entre as interações
- O tratamento de divisão por zero exibe "Erro" na tela
- Resultados são formatados para evitar casas decimais desnecessárias quando possível
- A interface foi estilizada com CSS customizado para melhor experiência visual

## 👨‍💻 Desenvolvido com

- Python
- Streamlit
- Amor por calculadoras simples e funcionais

---

*Projeto desenvolvido como parte do desafio IPR-50 MUDANÇA DE ESCOPO*