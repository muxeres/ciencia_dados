import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta al archivo CSV combinado
csv_file_path = r'C:\sql\dash\combined_data.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Reemplazar valores 0 con NaN para no considerarlos en los cálculos
df.replace(0, np.nan, inplace=True)

# Paletas de colores
palettes = {
    'Tab20': 'tab20',
    'Viridis': 'viridis',
    'Plasma': 'plasma',
    'Magma': 'magma',
    'Cividis': 'cividis'
}

# Crear directorio para guardar los gráficos si no existe
plots_dir = 'C:/sql/dash/plots/'
os.makedirs(plots_dir, exist_ok=True)

# Crear una función para guardar los gráficos
def save_plot(title):
    plt.savefig(os.path.join(plots_dir, f'{title}.png'), bbox_inches='tight')
    plt.close()  # Cerrar la figura para liberar memoria

# 1. Distribución de Precios (Price)
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'].dropna(), kde=True, color=sns.color_palette(palettes['Tab20'])[0])
plt.title('Distribución de Precios')
save_plot('Distribución de Precios')

# 2. Relación entre Cost per Unit y Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Cost per Unit'], y=df['Price'], color=sns.color_palette(palettes['Viridis'])[0])
plt.title('Relación entre Cost per Unit y Price')
save_plot('Relación entre Cost per Unit y Price')

# 3. Total Sales por Store
plt.figure(figsize=(10, 6))
sns.barplot(x='Store', y='Total Sales', data=df, color=sns.color_palette(palettes['Plasma'])[0])
plt.title('Total Sales por Store')
save_plot('Total Sales por Store')

# 4. Contribución de cada Categoría (Category)
plt.figure(figsize=(8, 8))
df['Category'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette(palettes['Magma']), startangle=90)
plt.title('Contribución de cada Categoría')
save_plot('Contribución de cada Categoría')

# 5. Unidades Vendidas por Mes (Units Sold vs Month)
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Units Sold', data=df, color=sns.color_palette(palettes['Cividis'])[0])
plt.title('Unidades Vendidas por Mes')
save_plot('Unidades Vendidas por Mes')

# 6. Total Sales por Manufacturer
plt.figure(figsize=(10, 6))
sns.barplot(x='Manufacturer', y='Total Sales', data=df, color=sns.color_palette(palettes['Tab20'])[0])
plt.title('Total Sales por Manufacturer')
save_plot('Total Sales por Manufacturer')

# 7. Correlación entre Total Sales y Units Sold
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Total Sales', data=df, color=sns.color_palette(palettes['Viridis'])[0])
plt.title('Correlación entre Total Sales y Units Sold')
save_plot('Correlación entre Total Sales y Units Sold')

# 8. Contribución de cada Producto al Total de Ventas
plt.figure(figsize=(10, 6))
df.groupby('Product')['Total Sales'].sum().plot(kind='bar', color=sns.color_palette(palettes['Plasma']))
plt.title('Contribución de cada Producto al Total de Ventas')
save_plot('Contribución de cada Producto al Total de Ventas')

# 9. Distribución de Ventas por Sales Channel
plt.figure(figsize=(8, 8))
df['Sales Channel'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette(palettes['Magma']), startangle=90)
plt.title('Distribución de Ventas por Sales Channel')
save_plot('Distribución de Ventas por Sales Channel')

# 10. Unidades Vendidas por Producto
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='Units Sold', data=df, color=sns.color_palette(palettes['Cividis'])[0])
plt.title('Unidades Vendidas por Producto')
save_plot('Unidades Vendidas por Producto')
