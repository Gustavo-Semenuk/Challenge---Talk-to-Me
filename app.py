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
    st.write("A solução da Talk to Me by SophIA, vem com o objetivo de trazer funcionalidades que irão além das ferramentas convencionais de transcrição de áudio. Tudo dentro de uma plataforma web simples e intuitiva.")
    st.markdown("""
    <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGFBfCLs4A/_guxZpY248GLpzszbmxFhw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGFBfCLs4A&#x2F;_guxZpY248GLpzszbmxFhw&#x2F;view?utm_content=DAGFBfCLs4A&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener"> 
    """, unsafe_allow_html=True)

    st.subheader("Veja também o nosso pitch deck para conhcer mais sobre a nossa solução ;)")
    url_pitch = "https://www.youtube.com/watch?v=B-eDFx2Kb0g&t=5s"
    st.video(url_pitch)
    st.divider()
    st.title("Nosso grupo - SophIA")
    st.write("Que tal conhecer um pouco mais sobre o nosso grupo antes de explorarmos a nossa plataforma ?")
    st.write("Veja abaixo um pouco mais sobre a SophIA:")
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/SOFIA.png", caption=" ", use_column_width=True)
    st.subheader("O nome do nosso grupo! Da onde veio SophIA?")
    st.write('O nome do projeto, SophIA, foi inspirado tanto no personagem Sofia, do livro "O Mundo de Sofia", quanto na junção com "IA", que representa Inteligência Artificial.')
    st.write('Assim como a personagem do livro, o projeto reflete uma curiosidade profunda, a busca por conhecimento e a capacidade de questionar e evoluir. O uso de "IA" reforça o foco em tecnologia avançada e inovação, trazendo o espírito explorador de Sofia para o contexto da inteligência artificial, evidenciando a busca do nosso grupo por trazer uma solução fora da caixa.')
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/o_mundo_de_sofia.jpg", caption=" ", width=300)
    st.subheader("Os integrantes do nosso grupo, ou melhor dizendo o único integrante do grupo e idealizador da solução")
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/semenuk.png", caption=" ", width=300)
    st.write('Gustavo Semenuk - Analista de Estratégia de Prevenção a Fraude Jr. - PicPay')
    st.markdown('<a href="https://www.linkedin.com/in/gustavo-semenuk/" target="_blank">Clique aqui para visitar o meu LinkedIN</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/Gustavo-Semenuk" target="_blank">Clique aqui para conhecer os meus repositórios no GitHub</a>', unsafe_allow_html=True)
    

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




