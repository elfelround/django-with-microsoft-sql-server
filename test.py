import pyodbc

server = '127.0.0.1'
username = 'sa'
password = 'StrongPass123'
PORT = '1433'

cnxn = pyodbc.connect(
    'DRIVER={FreeTDS};SERVER=' +
    server + ';PORT=' + PORT + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

print ('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print (str(row[0]))
