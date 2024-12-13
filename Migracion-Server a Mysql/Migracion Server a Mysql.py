import pyodbc
import mysql.connector
def connect_to_sql_server(server, database):
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server}; DATABASE={database};Trusted_Connection=Yes;"
    return pyodbc.connect(connection_string)
# Conexión a MySQL
def connect_to_mysql_without_database(host, user, password):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
def connect_to_mysql_with_database(host, database, user, password):
    return mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
#Extrae la extructur a del SQL SERVER
def fetch_data_from_sql_server(cursor, table):
    cursor.execute(f"SELECT * FROM {table}")
    columns = [column[0] for column in cursor.description]
    columns = [col.replace('.', '') for col in columns]
    columns = [col.replace(' ', '') for col in columns]
    data = cursor.fetchall()
    return columns, data
def create_mysql_table(mysql_cursor, table_name, columns):
    columns_definitions = ", ".join([f"`{col}` TEXT" for col in columns])  
    create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns_definitions})"
    mysql_cursor.execute(create_table_query)
# Insertar datos en MySQL
def insert_data_into_mysql(mysql_cursor, table_name, columns, data):
    placeholders = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ({placeholders})"
    mysql_cursor.executemany(insert_query, data)
# Proceso de migración
def migrate_data(sql_server_config, mysql_config, table_name):
    try:
        # Conectar a SQL Server
        sql_server_conn = connect_to_sql_server(**sql_server_config)
        sql_server_cursor = sql_server_conn.cursor()
        
        # Conectar a MySQL
        mysql_conn = connect_to_mysql_with_database(**mysql_config)
        mysql_cursor = mysql_conn.cursor()
        
        # Obtener datos de SQL Server
        columns, data = fetch_data_from_sql_server(sql_server_cursor, table_name)
        
        # Crear tabla en MySQL
        create_mysql_table(mysql_cursor, table_name, columns)
        # Insertar datos en MySQL
        insert_data_into_mysql(mysql_cursor, table_name, columns, data)
        # Confirmar cambios
        mysql_conn.commit()
        mysql_cursor.description
        print(f"Tabla `{table_name}` migrada exitosamente.")

        #
        sql_server_cursor.close()
        sql_server_conn.close()
        mysql_cursor.close()
        mysql_conn.close()
    except Exception as e:
        print(f"Error durante la migración: {e}")
def fetch_tables_names_from_sql_server(cursor):
    cursor.execute(f"select name from sys.tables;")
    tablas = cursor.fetchall()
    character_to_eliminate=['(',')',',','\'']
    tables_names=[]
    for var1 in range(len(tablas)):
        table_name =''
        tabla = tablas[var1]
        for var2 in range(len(tabla)):
            if tabla[var2] != character_to_eliminate:
                table_name += tabla[var2] 
        tables_names.append(table_name)
    return tables_names 
def migrate_data_base():
    #Se le pide al usuario los datos de la base de datos de sql server a migrar
    print("Introduzca el Server de Sql server a utilizar")
    sql_server_server:str = input()
    print("Introduzca la base de datos a migrar a Mysql")
    sql_server_database:str = input()
    sql_server_config = {
    "server": sql_server_server,
    "database": sql_server_database,
    }
    #Se le pide al usuario los datos del mysql al cual se va  a migrar
    print("Introduzca el Host de Mysql a utilizar")
    mysql_host:str = input()
    print("Introduzca el Username de Mysql a utilizar")
    mysql_user:str = input()
    print("Introduzca la passworddel Mysql a utilizar")
    mysql_password:str = input()
    mysql_config = {
    "host": mysql_host,
    "user": mysql_user,
    "password": mysql_password
    }
    try:
        # Conectar a SQL Server
        sql_server_conn = connect_to_sql_server(**sql_server_config)
        sql_server_cursor = sql_server_conn.cursor()
        # Conectar a MySQL
        mysql_conn = connect_to_mysql_without_database(**mysql_config)
        mysql_cursor = mysql_conn.cursor()
       
        #Creamos la database en Mysql
        mysql_cursor.execute(f"CREATE DATABASE {sql_server_database}")
        #Actualizamos las configuraciones de coneccion de Mysql
        mysql_config = {
            "host": mysql_host,
            "database": sql_server_database,
            "user": mysql_user,
            "password": mysql_password
            }
        
        tables_names = fetch_tables_names_from_sql_server(sql_server_cursor)
        print("a")
        for var3 in range (len(tables_names)):
            migrate_data(sql_server_config, mysql_config, tables_names[var3])
        
        sql_server_cursor.close()
        sql_server_conn.close()
        mysql_cursor.close()
        mysql_conn.close()
    except Exception as e:
        print(f"Error durante la migración: {e}")
migrate_data_base()
