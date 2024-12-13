import pyodbc
# 1. Crear conexion SQL Server 
mydb = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=LAPTOP-QKJ8CHC7;"
    "Database=Proyecto Zoologico;"
    "Trusted_Connection=yes;"
)

# 2. Creo un cursor
# El cursor es el que ejectura las sentencias
mycursor = mydb.cursor()

# 3. Ejecutar SQL 
table_name = "Empleado"
mycursor.execute(f"SELECT * FROM {table_name};")

# 4. Mostrar el resultado (La respuesta de la Sentencia SQL)
records = mycursor.fetchall()

for record in records:
    print(record)