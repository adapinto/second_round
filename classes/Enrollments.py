

class Enrollments:
    
    def __init__(self,curso,alumno,estado,id=""):
        self.curso=curso
        self.alumno=alumno
        self.estado=estado
        self.__id=id
        self.__collection="Matricula"
        
    def save(self,db):
        collection=db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        
    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )
    
    @staticmethod
    def get_list(db):
        collection = db["enrollments"]
        matriculas = collection.find()

        list_matriculas = []
        for e in matriculas:
            temp_matricula = Enrollments(
                e["alumno"]
                , e["curso"]
                , e["estado"]
                , e["_id"] 
            )

            list_matriculas.append(temp_matricula)
        return list_matriculas
    
    @staticmethod
    def delete_all(db):
        lista_e = Enrollments.get_list(db)
        for e in lista_e:
            e.delete(db) 