
import pymongo 
class MongoConnection:

    def __init__(self,client):
        self.client = pymongo.MongoClient(client)
    def get_db(self):
        databases = self.client.list_database_names()
        return databases


    def create_db(self, newdb_name):
        newdb = self.client[newdb_name]
        return newdb


    def add_collection(self,db_name, collection_name):
        db = self.client[db_name]
        new_collection = db[collection_name]
        return new_collection


    def delete_collection(self, db_name, collection_name):
        db = self.client[db_name]
        collection = db[collection_name]

        if collection.drop(): 
            return "Deletion successful" 
        else:
            return "Deletion failed"
    
    def insert_one(self,db_name, collection_name, record):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.insert_one(record) 


    def get_one(self,db_name, collection_name):
        db  = self.client[db_name]
        return db[collection_name].find_one()


    def get_all(self,db_name, collection_name, statement):
        db = self.client[db_name]
        for i in db[collection_name].find(statement):
            print(i)

    def update(self,db_name, collection_name, old,new):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.update(old,new) 

    def delete_single(self,db_name, collection_name, condition):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.delete_one(condition)

    def delete_many(self,db_name, collection_name, condition):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.delete_many(condition)