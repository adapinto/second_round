class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self,nombre,id):
        return nombre, id
    def create_courses(self,nombre,id):
        return nombre,id
    def create_students(self,numero_cuenta,nombre_completo,cursos_aprobados,cursos_reprobados,edad,carrera,id):
        return numero_cuenta,nombre_completo,cursos_aprobados,cursos_reprobados,edad,carrera,id
    def create_enrollments(self,alumno,curso,estado):
        return alumno,curso,estado