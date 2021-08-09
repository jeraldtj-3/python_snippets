import mysql.connector as connection 

# connection 
try:
    conn = connection.connect(host ='localhost',
                              user =  'root',
                              passwd = 'Thomas@29inf',
                              use_pure = True)
    query = 'SHOW DATABASES'
    cursor = conn.cursor() # create a cursor to excecute queries 
    cursor.execute(query) 
    print(cursor.fetchall())
    
except Exception as e:
    print('some error occured')
    print(e)
    try:    
        conn.close()
    except:
        print('remove the errors')
'''
dbname = database name 
tables 
'''
# none type 
type(cursor.execute(query))

print(cursor.fetchall())


# creating a new database 
try:
    query = 'CREATE DATABASE Empdb'
    cursor = conn.cursor() 
    cursor.execute(query) 
except:
    print('error occured') 

# checking 
query = 'show databases'
cursor = conn.cursor() 
cursor.execute(query) 
cursor.fetchall()







# creating table 

empdb = connection.connect(host = 'localhost',
                     database = 'Empdb', 
                     user = 'root', 
                     passwd = 'Thomas@29inf')

empdb.is_connected()
curs = empdb.cursor() 
query ="CREATE TABLE EmployeeDetails( EmployeeId INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(15), LastName VARCHAR(60), RegistrationDate DATE, Class VARCHAR(20), Section VARCHAR(10))" 
curs.execute(query) 




empdb.close() 










