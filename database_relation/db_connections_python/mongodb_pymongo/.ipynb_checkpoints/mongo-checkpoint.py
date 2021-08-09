

# creating class and object for mongodb connection 
import pymongo 
class MongoConnection:
    # getting the client url 
    def __init__(self,client):
        self.client=client
        
        
    # creating a database 
    def create_db(self,newdb_name):
        self.client[newdb_name]
        
    # getting the available databases for this mongo db connection     
    def get_db(self):
        databases = self.client.list_database_names()
        return databases

class dbConnection(MongoConnection):
    # get a particular db inside mongo connection 
    def __init__(self,client,db_name):
        super.__init__(client)
        self.db = self.client[db_name]
    
    # adding a new collection into db
    def add_collection(self,collection_name):
        collection = self.db[collection_name]
        print(f'created {collection_name} collection')
        
    # delete a particular collection 
    def delete_collection(self,collection_name):
        self.db[collection_name].drop()
        print(f'{collection_name} dropped') 
    
    # insert one record into a collection 
    def insert_one(self,collection_name,record):
        self.db[collection_name].insert_one(record)
    
    # deleting one record 
    def delete_single(self, colllection_name, condition):
        self.db[collection_name].delete_one(condition) 
    
    # delete many 
    def delete_mulitple(self,collection_name, condition):
        self.db[collection_name].delete_many(condition)
    
    # update_collection 
    def update(self,collection_name,old_data, new_data):
        self.db[collection_name].update(old_data, new_data)
    
    def get_one(self,collection_name):
        return self.db.find_one()
    
    def get(self, collection_name,statement:
        '''statement should be in json'''
        return self.db.find(statement)
