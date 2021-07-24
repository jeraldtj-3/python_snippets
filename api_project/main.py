


# importing libraries 
import os 
import psycopg2
import psycopg2.extras
import pandas as pd 


# for postgress database 
class SQL_Connection:
    # getting the necessary data for creating the connection 
    def __init__(self,user, password, host):
        self.user = user
        self.password = password
        self.host = host        
        # opening connection 
        self.sql_conn = psycopg2.connect(user = self.user,password = self.password,
                                           host = self.host)        
        # opening cursor 
        self.curs = self.sql_conn.cursor()
        
    # getting all the databases available 
    def get_databases(self):
        statement = """SELECT datname FROM pg_database"""
        self.curs.execute(statement)
        databases = [i[0] for i in self.curs.fetchall()]
        return databases
    
    # create db 
    def create_db(self, new_db_name):
        if new_db_name not in self.get_databases():                      
            statement = f"CREATE DATABASE {new_db_name}" 
            self.curs.execute(statement)
        else:
            print('database already exists')
    
    # delte method in sql connection 
    def delete_db(self, db_name):
        try:
            self.curs.execute(f'DROP DATABASE {db_name}')
        except Exception as e:
            print('database does not exist')  
    
class DB_connection(SQL_Connection):
    
    # adding an additional argument db_name 
    def __init__(self,user, password, host,dbname):
        super().__init__(user, password, host)
        self.dbname = dbname     
        # connection with the database 
        self.db_connection = psycopg2.connect(user= self.user, password = self.password, 
                                              host = self.host,dbname = self.dbname)
        # corresponding curser 
        self.curs2 = self.db_connection.cursor()
                             
    def get_tables(self):   # working 
            statement=""" 
                    SELECT table_name FROM information_schema.tables
                    where table_type = 'BASE TABLE' 
                    and table_schema = 'public';
                    """
            return pd.read_sql(statement, self.db_connection)
            
    def selection_execute(self, statement):   # working 
        return pd.read_sql(statement,self.db_connection)
    
    def create_table(self, statement):    
        self.curs2.execute(statement)
        
    
class DB_Table(DB_connection):
    def __init__(self,user,password,host, db_name, tbl_name):
        super().__init__(user,password,host,db_name)
        self.tbl_name = tbl_name
        self.tbl_connection = psycopg2.connect(user= self.user, password = self.password, 
                                               host = self.host,dbname = self.db_name, 
                                               tbl_name = self.tbl_name)
        self.curs3 = self.tbl_connection.cursor()
    def get_schema(self):
        statement = f"""
        SELECT column_name,data_type, FROM information_schema.columns
        where TABLE_NAME = {self.tbl_name}"""
        
        return pd.read_sql(statement,self.connection)
    
    def insert_into(self,row):
        statement = f"""
        INSERT INTO {self.tbl_name} VALUES {row}
        """
    # upload bulk data 
    def upload_data(self,path):
        """
        file should follow the same number of fields and datatypes.
        """
        file = open('path')
        row_list = list()
        # avoiding the headers 
        for i in file.readlines()[1::]:
            # adding -1 to remove the \n charactor
            row_list.append(tuple(i[:-1].split(',')))
        for row in row_list:
            statement = """
                INSERT INTO {self.tbl_name} VALUES {row} 
                """
            self.curs3.execute(statement) 

