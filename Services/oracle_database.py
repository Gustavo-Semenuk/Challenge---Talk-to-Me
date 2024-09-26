import oracledb

server = 'oracledb'
database = 'FIAP'
username = 'RM550472'
password = '070600'
cnxn = pyodbc.connect
cursor = cnxn.cursor






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

