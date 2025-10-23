# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:   
            self.database.animals.insert_one(data)  # data should be dictionary  
            return True
        except Exception as e:
            return False

    # Create method to implement the R in CRUD.
    def read(self, data):
        try:
            return list(self.database.animals.find(data))
        except Exception as e:
            return 'An error occurred while searching'
    
    # Method that implements the U in CRUD
    def update(self, updateCriteria, updateData):
        try:
            documents_modified = self.database.animals.update_many(updateCriteria, updateData)
            message = f'Documents modified: {documents_modified.modified_count}'
        except Exception as e:
            message = 'An error occurred while updating'
        return message
    
    # Method that implement the D in CRUD
    def delete(self, deleteCriteria):
        try:
            documents_deleted = self.database.animals.delete_many(deleteCriteria)
            message = f'Documents deleted: {documents_deleted.deleted_count}'
        except Exception as e:
            message = 'An error occurred while deleting'
        return message
    