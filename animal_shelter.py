from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self):
        # Hard-wired connection variables
        USER = 'aacuser'   
        PASS = 'password'   
        HOST = 'nv-desktop-services.apporto.com'       
        PORT = 34796           
        DB = 'AAC'               
        COL = 'animals'          

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # 'C' in CRUD (Create operation)
    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)  # Insert the data (should be a dictionary)
                return True  # Return True if the insertion was successful
            except Exception as e:
                print(f"Error inserting data: {e}")
                return False  # Return False if insertion failed
        else:
            raise Exception("No data to save, the provided data parameter is empty.")

    # 'R' in CRUD (Read operation)
    def read(self, searchData=None):
        try:
            if searchData:
                # Search for documents that match the search criteria and exclude the _id field
                data = list(self.collection.find(searchData, {"_id": False}))
            else:
                # Return all documents excluding the _id field if no search criteria
                data = list(self.collection.find({}, {"_id": False}))
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            return []

    # 'U' in CRUD (Update operation)
    def update(self, searchData, newData):
        try:
            # Update document(s) matching searchData with newData
            result = self.collection.update_many(searchData, {'$set': newData})
            return result.modified_count  # Return the number of documents modified
        except Exception as e:
            print(f"Error updating data: {e}")
            return 0  # Return 0 if update failed

    # 'D' in CRUD (Delete operation)
    def delete(self, searchData):
        try:
            # Delete document(s) matching the searchData
            result = self.collection.delete_many(searchData)
            return result.deleted_count  # Return the number of documents deleted
        except Exception as e:
            print(f"Error deleting data: {e}")
            return 0  # Return 0 if deletion failed