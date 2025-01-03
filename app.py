#Importação das bibliotecas

##Bibliotecas Streamlit
import streamlit as st
from streamlit_option_menu import option_menu
##Bibliotecas Conexão com banco Oracle
import oracledb
import Controllers.formulario_controler as formulario_controler
import Models.Formulario as Formulario
##Bibliotecas Data Science
import pandas as pd
import numpy as np
###Bibliotecas Stream lit 
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
#Fim da estrura da Home   

def sobre_nos():
    st.title("Sobre Nós")
    st.write("Que tal conhecer um pouco mais sobre o nosso grupo antes de explorarmos a nossa plataforma ?")
    st.write("Veja abaixo um pouco mais sobre a SophIA:")
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/SOFIA.png", caption=" ", use_column_width=True)
    st.subheader("O nome do nosso grupo! Da onde veio SophIA?")
    st.write('O nome do projeto, SophIA, foi inspirado tanto no personagem Sofia, do livro "O Mundo de Sofia", quanto na junção com "IA", que representa Inteligência Artificial.')
    st.write('Assim como a personagem do livro, o projeto reflete uma curiosidade profunda, a busca por conhecimento e a capacidade de questionar e evoluir. O uso de "IA" reforça o foco em tecnologia avançada e inovação, trazendo o espírito explorador de Sofia para o contexto da inteligência artificial, evidenciando a busca do nosso grupo por trazer uma solução fora da caixa.')
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/o_mundo_de_sofia.jpg", caption=" ", width=300)
    st.subheader("Os integrantes do nosso grupo, ou melhor dizendo o único integrante do grupo e idealizador da solução")
    st.image("D:/DEV/Challenge---Talk-to-Me/Imagens/Sobre mim.jpg", caption=" ", width=800)
    st.markdown('<a href="https://www.linkedin.com/in/gustavo-semenuk/" target="_blank">Clique aqui para visitar o meu LinkedIN</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/Gustavo-Semenuk" target="_blank">Clique aqui para conhecer os meus repositórios no GitHub</a>', unsafe_allow_html=True)

def formulario():
    st.title("Formulário")

    # Lista de estados brasileiros
    estados_brasil = [
        'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal',
        'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 
        'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 
        'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 
        'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'
    ]

    with st.form(key="cadastro_cliente"):
        input_name = st.text_input("Digite o seu nome completo*")
        input_email = st.text_input("Digite o seu email*")
        input_estado = st.selectbox("Selecione o seu estado atual*", estados_brasil)
        input_contexto = st.selectbox("Selecione o contexto do que você quer transcrever*", [
            "Não sei informar ainda", "Central Atendimento ao Cliente", "Ouvidoria e Jurídico",
            "Suporte Técnico", "Negociação e Cobrança", "Empresarial e Negócios"
        ])
        input_nome_empresa = st.text_input("Digite o nome fantasia da sua empresa*")
        input_site = st.text_input("Caso sua empresa possua site, cole a URL do site da sua empresa aqui*")

        input_segmento = st.selectbox("Escolha o segmento que mais se adeque a sua empresa*",[
    "Tecnologia", 
    "Saúde e Farmacêutica", 
    "Indústria e Manufatura", 
    "Serviços Financeiros", 
    "Energia e Utilidades", 
    "Agronegócio", 
    "Varejo", 
    "Alimentos e Bebidas", 
    "Transporte e Logística", 
    "Telecomunicações e Mídia", 
    "Imobiliário", 
    "Educação", 
    "Turismo e Lazer", 
    "Moda e Vestuário", 
    "Serviços Profissionais", 
    "Entretenimento e Esportes", 
    "Meio Ambiente e Sustentabilidade", 
    "Segurança e Defesa"
])
        # Upload de Arquivos
        st.header('Upload de arquivos*')
        uploaded_file = st.file_uploader('Escolha um arquivo', accept_multiple_files=True, type=['WAV'])

        # Botão de Enviar
        if st.form_submit_button("Enviar"):
            if not input_name or not input_email or not input_estado or not input_contexto or not input_segmento:
                st.error("Por favor, preencha todos os campos obrigatórios!")
            else:
                st.success("Formulário enviado com sucesso!")
                Formulario.nome = input_name
                Formulario.email = input_email
                Formulario.estado = input_estado
                Formulario.contexto = input_contexto
                Formulario.nome_empresa = input_nome_empresa
                Formulario.site = input_site
                Formulario.segmento = input_segmento

                formulario_controler.insert_formulario(Formulario)

def dashboards():
    st.title("Dashboards")

def analise():
    st.title("Análise")


# Sidebar para navegação
st.sidebar.image("D:/DEV/Challenge---Talk-to-Me/Imagens/Logo.png", caption=" ", use_column_width=True)

with st.sidebar:
    pagina_selecionada = option_menu(
        "Menu",  # Título do menu
        ["Home","Sobre Nós", "Formulario", "Dashboards","Análise"],  # Páginas
        icons=["house","info","clipboard", "bar-chart","gear"],  # Ícones (opcional)
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da página inicial
    )

# Exibir a página selecionada
if pagina_selecionada == "Home":
    home()
elif pagina_selecionada == "Sobre Nós":
    sobre_nos()
elif pagina_selecionada == "Formulario":
    formulario()
elif pagina_selecionada == "Dashboards":
    dashboards()
elif pagina_selecionada == "Análise":
    analise()

#Carregamento dos dados Oracle




