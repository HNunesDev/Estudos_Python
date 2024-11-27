import psycopg2
import os
from dotenv import load_dotenv



load_dotenv()
#Realizando conexao
host = os.getenv('host')
database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')

conexao = psycopg2.connect(host= host, database = database, user = user, password = password, port = port)


#Criar um cursor
cursor = conexao.cursor()
#Definindo consulta
consulta = "select * from clientes"
#Executando
cursor.execute(consulta)

#Recuperando todos os registros
registros = cursor.fetchall()

for row in registros:
    print(f'Nome: ', row[1],
          f'Estado: ', row[2],
          f'Status: ', row[4] )
    
#Fechar conexao
cursor.close
conexao.close()