import pandas as pd
from sqlalchemy import create_engine
import os

# Ruta al archivo Excel
excel_file_path = r'C:\sql\dash\Computer_store_Final.xlsx'
if not os.path.exists(excel_file_path):
    raise FileNotFoundError(f"El archivo no se encontró en: {excel_file_path}")

# Obtener el directorio donde se encuentra el archivo Excel
directory = os.path.dirname(excel_file_path)

# Nombre del archivo de la base de datos, en la misma carpeta que el Excel
db_file_path = os.path.join(directory, 'computer_store_Final.db')

# Leer todas las hojas en un diccionario de DataFrames
df_dict = pd.read_excel(excel_file_path, sheet_name=None)

# Crear una conexión a la base de datos SQL (SQLite en este caso)
engine = create_engine(f'sqlite:///{db_file_path}')

# Iterar sobre cada hoja y guardarla en la base de datos
for sheet_name, df in df_dict.items():
    # Convertir cada DataFrame en una tabla SQL
    df.to_sql(sheet_name, con=engine, if_exists='replace', index=False)
    print(f"Hoja '{sheet_name}' guardada en la tabla '{sheet_name}' en la base de datos.")

print("Conversión completa de todas las hojas a tablas SQL.")
