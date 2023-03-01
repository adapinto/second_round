import pymongo
from pymongo import MongoClient
from classes import DATA, Dataprocess,Students,DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
   # user = 'Adimari'
   # password = '99725478Adimari'
   # cluster = 'poounahclase3.v7p4vxg.mongodb.net'
   # query_string = 'retryWrites=true&w=majority'
#
#
   # ## Connection String
   # uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
   #     user
   #     , password
   #     , cluster
   #     , query_string
   # )
#
   #client = pymongo.MongoClient(uri)
   #db = client['courses-careers-students']
    collection = db['students']
   
   # #Elina todo lo que hay en la db para que no dupliquen los documentos
    delete_all = collection.delete_many({})
#
   # #Añadir la data a la coleccion de estudiantes
   # collection.insert_many(DATA)
    
    pipeline = Dataprocess(DATA)
    
    pipeline.create_students(db)
    pipeline.create_careers()
    pipeline.create_enrollments()

    

    client.close()
        
    if __name__ == "__main__":
        load_dotenv()
        main()