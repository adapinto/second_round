import pymongo
from dotenv import load_dotenv
from classes import DbMongo,DATA



class Dataprocess:

      def __init__(self, data):
        self.__data = data

      def create_careers(self,db):
          collection = db['careers']
          return True
      def create_courses(self,db):
          collection = db['courses']
          return True
      def create_students(self,db):
          collection = db['students']
          collection.insert_many(DATA)
          return True
      def create_enrollments(self,db):
          collection = db['enrollments']
          return True