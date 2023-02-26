import pymongo
from pymongo import MongoClient
from classes import DATA, Dataprocess

def main():
    user = 'Adimari'
    password = '99725478Adimari'
    cluster = 'poounahclase3.v7p4vxg.mongodb.net'
    query_string = 'retryWrites=true&w=majority'


    ## Connection String
    uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
        user
        , password
        , cluster
        , query_string
    )

    client = pymongo.MongoClient(uri)
    db = client['courses-careers-students']
    collection = db['students']
    
    
    collection.insert_many(DATA)
    
    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()

    return True

if __name__ == "__main__":
    main()