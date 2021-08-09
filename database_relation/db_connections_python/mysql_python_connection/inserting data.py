import mysql_connection as connection 

# creating the connection 
mydb = connection.connect(host = 'localhost', 
                          database = 'Empdb', 
                          user = 'root', 
                          passwd = 'Thomas@29inf')

# creating the cursor 
cur = mydb.cursor()

# inseritng query 
query = "INSERT INTO  EmployeeDetails VALUES(101, 'Thomaskutty','Reji',"2021-07-17",'a','s1')"


