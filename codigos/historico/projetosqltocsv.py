import sqlite3
import csv

# Conteúdo do arquivo projetoloja.sql
sql_content = """
CREATE TABLE Manufacturers IF NOT EXIST(
    Code INTEGER PRIMARY KEY NOT NULL,
    Name CHAR(50) NOT NULL 
);

CREATE TABLE Products IF NOT EXIST(
    Code INTEGER PRIMARY KEY NOT NULL,
    Name CHAR(50) NOT NULL ,
    Price REAL NOT NULL ,
    Manufacturer INTEGER NOT NULL 
        CONSTRAINT fk_Manufacturers_Code REFERENCES Manufacturers(Code)
);

INSERT INTO Manufacturers(Code,Name) VALUES 
(1,'Sony'),
(2,'Creative Labs'),
(3,'Hewlett-Packard'),
(4,'Iomega'),
(5,'Fujitsu'),
(6,'Winchester');

INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES
(1,'Hard drive',240,5),
(2,'Memory',120,6),
(3,'ZIP drive',150,4),
(4,'Floppy disk',5,6),
(5,'Monitor',240,1),
(6,'DVD drive',180,2),
(7,'CD drive',90,2),
(8,'Printer',270,3),
(9,'Toner cartridge',66,3),
(10,'DVD burner',180,2);
"""

# Criando o arquivo projetoloja.sql
with open('projetoloja.sql', 'w') as file:
    file.write(sql_content)

print("Arquivo projetoloja.sql criado com sucesso!")

# Conectando ao banco de dados SQLite (criando um novo banco de dados físico)
conn = sqlite3.connect('loja_computadores.db')  # Aqui criamos ou abrimos o banco de dados loja_computadores.db
cursor = conn.cursor()

# Executando o script SQL para criar as tabelas e inserir os dados
cursor.executescript(sql_content)

# Fazendo um JOIN entre as tabelas Products e Manufacturers
query = """
SELECT Products.Code AS Product_Code, Products.Name AS Product_Name, 
       Products.Price, Manufacturers.Name AS Manufacturer_Name
FROM Products
JOIN Manufacturers ON Products.Manufacturer = Manufacturers.Code;
"""
cursor.execute(query)

# Obtendo os dados e os nomes das colunas
dados = cursor.fetchall()
colunas = [description[0] for description in cursor.description]

# Exportando todos os dados para um único arquivo CSV
with open('loja_computadores.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(colunas)  # Escrevendo os nomes das colunas
    writer.writerows(dados)  # Escrevendo os dados

# Fechando a conexão com o banco de dados
conn.close()

print("Exportação para CSV concluída com sucesso!")
