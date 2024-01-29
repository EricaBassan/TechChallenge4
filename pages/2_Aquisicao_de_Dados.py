
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
## Aquisição e Armazenamento dos dados
'''
'''
Os dados históricos do preço do petróleo estavam inicialmente disponíveis em uma página Web ( http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view - Ipeadata).
Eles foram carregados para o banco de dados da Google Cloud Plataform, o Big Query. 

Para tanto, realizamos um web scrapping em um arquivo Jupyter, que realizasse a extração dos dados de um html e incluisse-os em banco de dados.
Se já houvessem dados carregados no banco, ele iria comparar a data mais recente do hmtl com a data mais recente armazenada, para garantir que a carga realizada fosse incremental.

Tal processo foi realizado com o intuito de que sempre houvessem dados disponníveis para o modelo e o Dahsboard serem atualizados, mesmo que o hmtl não estivesse disponível.

Abaixo, podemos ver a organização da tabela do IPEA no banco de dados:

'''
st.image(load_img('Images/Tbl_Ipea_BigQuery.PNG'))
'''
Os dados armazenados posteriormente foram utilizados para construção de um modelo e um Dashboard.



'''






