
from classes import DATA, Dataprocess,DbMongo
from dotenv import load_dotenv
from classes import *

def main():
    client, db = DbMongo.getDB()
    #user = 'Adimari'
    #password = '99725478Adimari'
    #cluster = 'poounahclase3.v7p4vxg.mongodb.net'
    #query_string = 'retryWrites=true&w=majority'
#
#
    ### Connection String
    #uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
    #    user
    #    , password
    #    , cluster
    #    , query_string
    #)
#
    #client = pymongo.MongoClient(uri)
    #db = client['courses-careers-students']
   
   
   # #Elina todo lo que hay en la db para que no dupliquen los documentos
    #delete_all = collection.delete_many({})
#
   # #Añadir la data a la coleccion de estudiantes
    #collection.insert_many(DATA)
    
    pipeline = Dataprocess(DATA)
    
    pipeline.create_students(db)
    pipeline.create_careers(db)
    pipeline.create_enrollments(db)
    
    client.close()
    
if __name__ == "__main__":
   load_dotenv()
   main() 
   