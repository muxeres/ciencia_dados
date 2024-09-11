import pandas as pd
import numpy as np

# Ruta al archivo CSV combinado
csv_file_path = r'C:\sql\dash\combined_data.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Convertir la columna 'Code' a enteros, manejando valores no convertibles como NaN
df['Code'] = pd.to_numeric(df['Code'], errors='coerce').fillna(0).astype(int)

# Lista de columnas a limpiar (excluyendo 'Code')
columns_to_check = [
    'Name', 'Country', 'source_table', 'Product', 'Price', 'Manufacturer',
    'Cost per Unit', 'Manufacturer Name', 'Category', 'Product Code',
    'Month', 'Store', 'Units Sold', 'Total Sales', 'Product Name',
    'Sales Channel', 'Total_Sales', 'Total_Units_Sold', 'Contribution_Percentage'
]

# Reemplazar valores cero con NaN en las columnas de cantidad o precio
columns_with_zero_to_nan = ['Price', 'Cost per Unit', 'Total Sales', 'Units Sold', 'Total_Sales', 'Total_Units_Sold']
df[columns_with_zero_to_nan] = df[columns_with_zero_to_nan].replace(0, np.nan)

# Guardar el DataFrame limpio en un nuevo archivo CSV sin eliminar filas
cleaned_csv_file_path = r'C:\sql\dash\cleaned_data.csv'
df.to_csv(cleaned_csv_file_path, index=False)

print(f"Datos limpios guardados en '{cleaned_csv_file_path}'.")
