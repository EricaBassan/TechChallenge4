import matplotlib.pyplot as plt
import streamlit as st



# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

st.set_page_config(layout="centered")

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

st.divider()

'''
## Analise de Dados (Dashboard)


Um Dahsboard interativo foi criado para analisar insights a respeito do nosso Dataset.

'''
st.image(load_img('Images/Dashboard_1.png'))
st.image(load_img('Images/Dashboard_2.png'))
'''
A primeira analise diz respeito o valor do preço do petróleo ao longo do anos. Podemos observar diversos movimentos politicos/sociais que contribuiram para a alteração do valor do petróleo.

'''
st.image(load_img('Images/historia_preco_petroleo.png'))
'''
A figura acima destaca os principais eventos responsáveis por influenciar o valor do petróleo brent, sendo eles:

-Guerra do Golfo (1990): Guerra entre Estados Unidos e Iraque, países que ocupam o top 5 de maiores produtores globais de petróleo;

-Atentado de 11/setembro: Atentado terrorista que estreitaria relações entre o maior produto de petróleo (EUA) e os países do Oriente Médio;

-Grande Recessão (2008): Crise financeira dos EUA, que resultou em diversas recessões pelo mundo, inclusive no petróleo;

-Guerra da Síria (2011): Conflito na Síria que desencadeou a Primera Árabe, responsável por diversas revoluções no Oriente Médio;

-Guerra Ucrania- Rússia: Rússia que faz parte da OPEP (Organizaçao dos Países Exportadores de Petróleo) entrou em conflito com a Ucrânia, o que acabou resultando em diversas sanções a respeito do petróleo.


Essses conflitos influenciaram o mercado, pois foram protagonizados pelos grande produtores de Petroleo (conforme imagem abaixo):
'''
st.image(load_img('Images/producao-petroleo.png'))
'''
Sendo os Estados Unidos o principal produtor de petróleo atualmente, suas ações políticas influenciam diretamente o valor do brent, assim como o valor do dólar, por exemplo.
'''
st.image(load_img('Images/comparacao-dolar-petroleo.png'))
'''
O gráfico acima, compara o valor da cotação do dólar, com o valor do brent de petróleo.
Podemos ver que de modo geral, são inversamente proporcionais.

O mercado explica o fenômeno da seguinte forma: "(...) à medida que o dólar se valoriza, as moedas estrangeiras se depreciam, tornando mais lucrativo para os produtores globais de petróleo negociar em moedas locais (exceto nos EUA). Isso incentiva mais produção de petróleo, aumentando a oferta e reduzindo a cotação do barril do petróleo."
O trecho anterior foi extraído de uma entrevista da Revista Exame e explica o movimento do mercado financeiro.

O Dashboard ainda conta com uma visão dos principais países consumidores de petróleo, sendo o top 3: Estados Unidos, China e Índia.

'''
st.image(load_img('Images/consumo-petroleo.png'))
'''

Podemos ver que além de serem 3 países extremamente populosos, são nações que não contam com outras fontes de energia/combustível.

-Os EUA, por exemeplo, possuem cerca de 60% da sua energia derivada de energia fóssil;

-A China e a Índia, países com alta concentração de habitantes, possuem uma demanda alta por combustível e energia. E embora sejam países que refinam petroleo, não estão entre os maiores produtores.

'''
