import requests
import oracledb
from bs4 import BeautifulSoup

titulo = 'Programa de respagem de dados web via web scraping\n'
print(f'{titulo:^100}')

start_programa = input('Quer iniciar o programa? (Sim ou Não) \n')

while start_programa in ['Sim', 'sim', 'SIM', 'S', 's']:
    site = input('Cole ou digite a url do seu site: \n')

    response = requests.get(site)

    if response.status_code == 200:

        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        nome_arquivo = input(
            'Digite o nome do arquivo: (Exemplo:. teste.txt) \n')

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for linha in soup.stripped_strings:
                arquivo.write(linha + "\n")

        print(f"Arquivo '{nome_arquivo}' gerado com sucesso.\n")
    else:
        print(
            f"A solicitação HTTP retornou o código de status {response.status_code}. Não foi possível obter o conteúdo da página.\n")

    oracle = 'Conexão com o banco de dados ORACLE\n'
    print(f'{oracle:^100}')

    try:
        conn = oracledb.connect(
            user=f"XXXXXX", password="XXXXXX", dsn="nome_host:porta/SID")
    except Exception as e:
        print("Erro de conexão com o Oracle:", e)
        conexao = False
    else:
        conexao = True
    with conn.cursor() as c_insert:
        texto_coletado = "\n".join(soup.stripped_strings)

        cmd = f"insert into NOME_TABELA (ATRIBUTO1, ATRIBUTO2, ATRIBUTO3)" \
              f" values " \
              f" (1, '{nome_arquivo}', :DS_CONTEUDO)"

        c_insert.execute(cmd, DS_CONTEUDO=texto_coletado)

        print(cmd)
        conn.commit()

    conn.close()

    start_programa = input(f'Quer coletar mais algum dado? (Sim ou Não) \n')

    if start_programa in ['Não', 'NÃO', 'não', 'N', 'n']:
        print('Programa Finalizado\n')





# Função de consulta
def consultar_dados(conn):
    try:
        cursor = conn.cursor()

        # Exemplo de uma consulta SQL - Altere para sua tabela
        cursor.execute("SELECT * FROM T_BS_LIVRO")

        # Obtenha todos os resultados da consulta
        colunas = [col[0] for col in cursor.description]  # Nomes das colunas
        dados = cursor.fetchall()  # Dados da consulta

        # Converta para um DataFrame Pandas para melhor exibição
        df = pd.DataFrame(dados, columns=colunas)

        # Mostra os dados em formato de tabela
        print(df)
    except Exception as e:
        print(f"Erro ao consultar os dados: {e}")
    finally:
        cursor.close()  # Fechar o cursor após o uso

# Executa a consulta se a conexão for bem-sucedida
if conexao:
    consultar_dados(conn)
    
    # Fechando a conexão
    conn.close()
    print("Conexão fechada com sucesso.")