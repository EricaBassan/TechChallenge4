import matplotlib.pyplot as plt
import streamlit as st

# Configurando a página
st.set_page_config(
    page_title="Tech Challenge 4 - Data Analytics FIAP",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto criado para o *tech-challenge* do curso de pós-graduação de Data Analytics da FIAP."
    }
)

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Titulo de Página
st.title('Análise de dados: analisando os dados de preço por barril do petróleo bruto (Brent)')

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Alterando cor dos hyperlinks
st.markdown(
   """
    <style>
     a:link {
       color: #F63366;
       background-color: transparent;
       text-decoration: none;
     }

     a:visited {
        color: #98072d;
        background-color: transparent;
        text-decoration: none;
    }

     a:hover {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }

    a:active {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }
    </style>
    """ , unsafe_allow_html=True
)

url = 'https://ichef.bbci.co.uk/news/640/cpsprodpb/36d8/live/545b30a0-faf4-11ed-92cc-b3a9bf1f67e9.jpg'
st.image(load_img('Images/Petroleo.jpg'))

'''
## 'Análise de dados: analisando os dados de preço por barril do petróleo bruto (Brent)'


GitHub do Projeto:

(https://github.com/EricaBassan/TechChallenge4) - Github Érica Bassan


'''
st.divider()
'''
## Apresentação

Este projeto foi criado para atender os requisitos do projeto Tech Challenge da Faculdade de Tecnologia - FIAP.

O Desafio consistia em analisar uma base de dados do IPEA a respeito do histórico do preço do petróleo (brent), contruir um modelo de Machine Learning que conseguisse prever o fechamento dos últimos dias, além de criar um Dashboard que contlempasse os principais indicadores a respeito do tema.

O desafio precisava cumprir os critérios abaixo:

-Criação de um Dashboard interativo;

-Construção de um storytelling com insights importantes sobre a variação do preço do petróleo;

-Criação de um modelo de Machine Learing que fosse capaz de realizar previsões diárias, bem como sua perfomance;

-Criação de um plano de Deploy em produção do modelo;

-Realizar um MVP do modelo em produção, com o Streamlit.

As próximas páginas contém o plano de desenvolvimento e resultados do projeto.

'''
st.divider()
'''
## Páginas

'''
col1, col2, col3, col4 = st.columns([0.13,0.13,0.13, 0.13])
with col1:
    if st.button('## Apresentação', type='primary'):
       st.switch_page("Apresentacao.py")
with col2:
    if st.button('## Aquisição e Armazenamento dos dados'):
        st.switch_page("pages/2_Aquisicao_de_Dados.py")
with col3:
    if st.button('## Analise de Dados (Dashboard)'):
        st.switch_page("pages/3_Analise_de_Dados.py")
with col4:
   if st.button('## Modelo de Machine Learnig'):
       st.switch_page("pages/4_Modelo.py")

st.divider()

