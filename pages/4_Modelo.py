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

'''
## Modelo de Machine Learnig
'''
'''
A partir do dados armazenados no Google Cloud, construímos um modelo de Machine Learnign capaz de realizar provisões a respeito do valor do brent do petroleo.

Para a construção do modelo, utilizamos a biblioteca Prophet, e conseguimos alcançar uma perfomance boa.

'''
st.image(load_img('Images/Previsão.png'))
'''
Seus erros calculados, ficaram dentro da magem desejável, e possuem um Erro Médio Percentual Absoluto Ponderado, de 13.96%.

'''
st.image(load_img('Images/perfomance-modelo1.png'))
st.image(load_img('Images/perfomance-modelo2.png'))


'''
Seus resultados foram salvos em um arquivo .csv e em seguida, incluímos esses dados em uma tabela do Big Query.
'''
st.image(load_img('Images/Tbl_Previsao_BigQuery.png'))
'''

Os dados de previsão alimentados no GCP, foram utilizados posteriormente em um Dashboard.

'''
st.image(load_img('Images/previsao-petroleo.png'))

'''

O plano de desenvolvimento do projeto está contido na imagem abaixo e contém todos as etapas aplicadas.

'''
st.image(load_img('Images/Projeto.png'))

'''

'''




