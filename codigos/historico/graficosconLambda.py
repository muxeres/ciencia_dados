import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Leer el archivo CSV en un DataFrame
csv_file_path = r'C:\sql\dash\combined_data.csv'
df = pd.read_csv(csv_file_path)

# Reemplazar valores 0 con NaN para no considerarlos en los cálculos
df.replace(0, np.nan, inplace=True)

# Crear el directorio para los gráficos si no existe
plots_directory = r'C:\sql\dash\plots'
if not os.path.exists(plots_directory):
    os.makedirs(plots_directory)

# Función para guardar gráficos
def save_plot(title):
    plt.savefig(os.path.join(plots_directory, f'{title}.png'), bbox_inches='tight')
    plt.close()

# Definir gráficos y sus títulos
plots = {
    'Distribución de Precios': lambda: sns.histplot(df['Price'].dropna(), bins=30, color='violet', kde=True),
    'Relación entre Cost per Unit y Price': lambda: sns.scatterplot(data=df, x='Cost per Unit', y='Price', color='green'),
    'Total Sales por Store': lambda: sns.barplot(data=df, x='Store', y='Total Sales', palette='magma'),
    'Contribución de cada Categoría': lambda: plt.pie(df['Category'].dropna().value_counts(), labels=df['Category'].dropna().value_counts().index, colors=sns.color_palette("tab20", len(df['Category'].dropna().value_counts())), autopct='%1.1f%%'),
    'Unidades Vendidas por Mes': lambda: sns.lineplot(data=df, x='Month', y='Units Sold', marker='o', color='magenta'),
    'Total Sales por Manufacturer': lambda: sns.barplot(data=df, x='Manufacturer', y='Total Sales', palette='coolwarm'),
    'Correlación entre Total Sales y Units Sold': lambda: sns.scatterplot(data=df, x='Units Sold', y='Total Sales', color='cyan'),
    'Contribución de cada Producto al Total de Ventas': lambda: plt.bar(df.groupby('Product')['Total Sales'].sum().sort_values().index, df.groupby('Product')['Total Sales'].sum().sort_values().values, color='red'),
    'Distribución de Ventas por Sales Channel': lambda: plt.pie(df['Sales Channel'].dropna().value_counts(), labels=df['Sales Channel'].dropna().value_counts().index, colors=sns.color_palette("Set2", len(df['Sales Channel'].dropna().value_counts())), autopct='%1.1f%%'),
    'Unidades Vendidas por Producto': lambda: sns.barplot(data=df, x='Product', y='Units Sold', palette='pastel')
}

# Generar y guardar los gráficos
for title, plot_func in plots.items():
    plt.figure(figsize=(10, 6))
    plot_func()
    plt.title(title)
    save_plot(title)
