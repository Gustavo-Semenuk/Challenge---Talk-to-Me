#Importação das bibliotecas

##Bibliotecas Streamlit
import streamlit as st
from streamlit_option_menu import option_menu
##Bibliotecas Web Scrapping
from bs4 import BeautifulSoup
import requests
##Bibliotecas Conexão com banco Oracle
import oracledb
##Bibliotecas Data Science
import pandas as pd
import numpy as np

import streamlit as st


#Estrutura Home 
def home():
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/Fundo.png", caption=" ", use_column_width=True)
    st.divider()
    st.title("Nossa solução")
    st.write("Veja o link abaixo da nossa apresentação .ppt")
    st.write("Nosso pitch deck")
    url_pitch = "https://www.youtube.com/watch?v=B-eDFx2Kb0g&t=5s"
    st.video(url_pitch)
    st.divider()
    st.title("Nosso grupo - SofIA")

    

def comece_aqui():
    st.title("Comece Aqui")
    #Upload de Arquivos
    st.header('Upload de arquivos')
    uploaded_file = st.file_uploader('Escolha um arquivo', type=['WAV'])

def dashboards():
    st.title("Dashboards")

def analise():
    st.title("Análise")


# Sidebar para navegação
st.sidebar.image("D:/DEV/Challenge---Talk-to-Me/Imagens/Logo.png", caption=" ", use_column_width=True)

with st.sidebar:
    pagina_selecionada = option_menu(
        "Menu",  # Título do menu
        ["Home", "Comece Aqui", "Dashboards","Análise"],  # Páginas
        icons=["house", "info", "bar-chart","gear"],  # Ícones (opcional)
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da página inicial
    )

# Exibir a página selecionada
if pagina_selecionada == "Home":
    home()
elif pagina_selecionada == "Comece Aqui":
    comece_aqui()
elif pagina_selecionada == "Dashboards":
    dashboards()
elif pagina_selecionada == "Análise":
    analise()

#Carregamento dos dados Oracle




