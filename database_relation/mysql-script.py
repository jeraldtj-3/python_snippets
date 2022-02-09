import mysql.connector as connection

# showing databases
try:
    # providing the connection
    conn = connection.connect(host = 'localhost',
        user = 'root',
        passwd = 'Computer123@',
        use_pure = True)
    query = "SHOW DATABASES"
    curs = conn.cursor() # creating the cursor for the connection
    curs.execute(query)
    print(curs.fetchall())
    conn.close()
except Exception as e:
    print(str(e))

# checking connection
conn.is_connected()

# dropping database
try:
    # providing the connection
    conn = connection.connect(host = 'localhost',
        user = 'root',
        passwd = 'Computer123@',
        use_pure = True)
    query = "DROP DATABASE Mytestdb"
    curs = conn.cursor() # creating the cursor for the connection
    curs.execute(query)
    # print(curs.fetchall())
    conn.close()
except Exception as e:
    print(str(e))


# creating new database
# CREATE DATABASE mydb
conn = connection.connect(host = 'localhost',
                          user = 'root',
                         passwd = 'Computer123@',
                         use_pure = True)
curs = conn.cursor()
curs.execute('CREATE DATABASE Mytestdb')
conn.close()

# checking
conn = connection.connect(host = 'localhost', user = 'root',
                          passwd = 'Computer123@',use_pure = True)
curs = conn.cursor()
curs.execute('show databases')
print(curs.fetchall())
conn.close()

# creating a table inside the database
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement = """
CREATE TABLE StudentDetails(
    studentId INT(10) AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    registrationDate DATE,
    class VARCHAR(20),
    section VARCHAR(10))
"""
curs.execute(statement)

test_db_conn.close()

# checking the tables
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
print(curs.fetchall())
test_db_conn.close()


# inserting records into database table
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement = """
        INSERT INTO StudentDetails VALUES
        ('1132', 'Thomas', 'Reji','2020-12-21', 'pg', 'Four')
"""
curs.execute(statement)
test_db_conn.commit()
test_db_conn.close()


# selecting the records
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
print(curs.fetchall())
test_db_conn.close()

test_db_conn = connection.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Computer123@',
    database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement1 = """
        INSERT INTO StudentDetails VALUES
        ('1133', 'Maria', 'Thomas','2020-11-20', 'pg', 'Four')
        """
statement2= """
        INSERT INTO StudentDetails VALUES
        ('1134', 'steve', 'martin','2020-08-25', 'ug', 'Second')
"""
statement3 = """
        INSERT INTO StudentDetails VALUES
        ('1135', 'Colins', 'James','2020-11-20', 'pg', 'First')
"""
curs.execute(statement1)
curs.execute(statement2)
curs.execute(statement3)

test_db_conn.commit()
test_db_conn.close()

# getting all the inserted rows
# selecting the records
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
print(curs.fetchall())
test_db_conn.close()

test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
for i in curs.fetchall():
    print(i)
test_db_conn.close()


# gettting data in tabular form
import pandas as pd
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
pd.read_sql("select * from StudentDetails", test_db_conn)


# reading the data using pandas
glass_data = pd.read_csv('glass.csv')
curs = test_db_conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS GlassData (
    Index_Number INT(10),
    RI float(10,5),
    Na float(10,5),
    Mg float(10,5),
    Al float(10,5),
    Si float(10,5),
    K float(10,5),
    Ca float(10,5),
    Ba float(10,5),
    Fe float(10,5),
    Class INT(5)
) """
curs.execute(query)

# glass_data.to_sql(name = 'glassDetails',con = test_db_conn)
glass_data.dtypes

import csv
with open ('glass.csv', 'r') as f:
    next(f)
    glass_data = csv.reader(f, delimiter = '\n')
    for line in enumerate(glass_data):
        for list_ in line[1]:
            curs.execute('INSERT INTO GlassData values ({values})'.format(values=(list_)))
test_db_conn.commit()
curs.close()
test_db_conn.close()

# reading the uploaded glass data from the database =
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
pd.read_sql('select * from GlassData',test_db_conn)


# delete table
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)

statement = "DELETE FROM StudentDetails WHERE firstName = 'Colins'"
curs = test_db_conn.cursor()
curs.execute(statement)
test_db_conn.commit()
test_db_conn.close()


test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
for i in curs.fetchall():
    print(i)
test_db_conn.close()

# update the values
test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement = """
        UPDATE StudentDetails SET firstName = 'Merin' WHERE studentId = 1132
"""
curs.execute(statement)
test_db_conn.commit()
test_db_conn.close()

test_db_conn = connection.connect(host = 'localhost',user = 'root',
                                  passwd = 'Computer123@',
                         database = 'Mytestdb',use_pure = True)
curs = test_db_conn.cursor()
statement  = "select * from StudentDetails"
curs.execute(statement)
for i in curs.fetchall():
    print(i)
test_db_conn.close()



