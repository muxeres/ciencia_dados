import pandas as pd
import sqlite3

# Conectar ao arquivo .db
conn = sqlite3.connect('computer_store_Final.db')

# Obter todas as tabelas do banco de dados
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)

# Criar um objeto ExcelWriter para escrever várias planilhas
with pd.ExcelWriter('Computer_store_Final.xlsx', engine='xlsxwriter') as writer:
    for table_name in tables['name']:
        # Ler cada tabela do banco de dados
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        # Escrever cada tabela em uma planilha diferente do arquivo Excel
        df.to_excel(writer, sheet_name=table_name, index=False)

# Fechar a conexão com o banco de dados
conn.close()

print("Arquivo Excel gerado com sucesso!")
