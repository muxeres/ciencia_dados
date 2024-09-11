import pandas as pd
from sqlalchemy import create_engine, inspect
import os

# Ruta al archivo de la base de datos SQLite
db_file_path = r'C:\sql\dash\computer_store_Final.db'

# Ruta del directorio para guardar el archivo CSV
csv_directory = os.path.dirname(db_file_path)

# Crear una conexión a la base de datos SQL (SQLite en este caso)
engine = create_engine(f'sqlite:///{db_file_path}')

# Obtener el nombre de todas las tablas en la base de datos
inspector = inspect(engine)
tables = inspector.get_table_names()

# Lista para almacenar DataFrames
df_list = []

# Iterar sobre cada tabla y agregar el DataFrame a la lista
for table_name in tables:
    df = pd.read_sql_table(table_name, con=engine)
    df['source_table'] = table_name  # Agregar columna con el nombre de la tabla
    df_list.append(df)
    print(f"Tabla '{table_name}' cargada en el DataFrame.")

# Concatenar todos los DataFrames en uno solo
combined_df = pd.concat(df_list, ignore_index=True)

# Guardar el DataFrame combinado en un archivo CSV
combined_csv_file_path = os.path.join(csv_directory, 'combined_data.csv')
combined_df.to_csv(combined_csv_file_path, index=False)

print(f"Todos los datos combinados guardados en '{combined_csv_file_path}'.")


# import pandas as pd
# from sqlalchemy import create_engine
# import os

# # Ruta al archivo de la base de datos SQLite
# db_file_path = r'C:\sql\dash\computer_store_Final.db'

# # Ruta del directorio para guardar el archivo CSV
# csv_directory = os.path.dirname(db_file_path)

# # Crear una conexión a la base de datos SQL (SQLite en este caso)
# engine = create_engine(f'sqlite:///{db_file_path}')

# # Obtener el nombre de todas las tablas en la base de datos
# tables = engine.table_names()

# # Lista para almacenar DataFrames
# df_list = []

# # Iterar sobre cada tabla y agregar el DataFrame a la lista
# for table_name in tables:
#     df = pd.read_sql_table(table_name, con=engine)
#     df['source_table'] = table_name  # Agregar columna con el nombre de la tabla
#     df_list.append(df)
#     print(f"Tabla '{table_name}' cargada en el DataFrame.")

# # Concatenar todos los DataFrames en uno solo
# combined_df = pd.concat(df_list, ignore_index=True)

# # Guardar el DataFrame combinado en un archivo CSV
# combined_csv_file_path = os.path.join(csv_directory, 'combined_data.csv')
# combined_df.to_csv(combined_csv_file_path, index=False)

# print(f"Todos los datos combinados guardados en '{combined_csv_file_path}'.")
