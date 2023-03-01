import pymongo
from dotenv import load_dotenv
from classes import DbMongo,DATA



class Dataprocess:

      def __init__(self, data):
        self.__data = data

      def create_careers(self,db):
          collection = db['careers']
          for a in DATA:
            for carrera in a:
                career = {"carrera": carrera}
                collection.insert_one(career)
          return True
      def create_courses(self,db):
          collection = db['courses']
          for e in DATA:
            for cursos_aprobados in e:
                approved_courses = {"cursos_aprobados": cursos_aprobados}
                collection.insert_one(approved_courses)
          
            for e in DATA:
              for cursos_reprobados in e:
                  failed_courses = {"cursos_reprobados": cursos_reprobados}
                  collection.insert_one(failed_courses)
            return True
      def create_students(self,db):
          collection = db['students']
          delete_all = collection.delete_many({})
          collection.insert_many(DATA)
          return True
      def create_enrollments(self,db):
          collection = db['enrollments']
          return True