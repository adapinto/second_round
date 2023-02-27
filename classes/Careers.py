
class Careers:
    
    def __init__ (self,nombre,id=""):
        self.nombre=nombre
        self.__id=id
        self.__collection= "Carrera"
        
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
        collection = db["career"]
        carreras = collection.find()

        list_carreras = []
        for e in carreras:
            temp_carrera = Careers(
                e["nombre"]
                , e["_id"] 
            )

            list_carreras.append(temp_carrera)
        return list_carreras
    
    @staticmethod
    def delete_all(db):
        lista_e = Careers.get_list(db)
        for e in lista_e:
            e.delete(db) 