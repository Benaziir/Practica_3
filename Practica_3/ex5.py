print('Exercicio 5')
class Alumno():

    def __init__(self,nombre,registro):
        edad=-1
        nota=-1

        self.nombre=nombre
        self.registro=registro
        self.edad=edad
        self.nota=nota

    def Display(self):
        print(f"Nombre de Alumno: {self.nombre}\nNumero de Registro: {self.registro}")
        #Mostramos el campo edad solo si es ingresado con setAge y es mayor a 3 (asumiendo que puede ser alumno de un jardin)
        if self.edad >3:
            print(f"Edad: {self.edad}")
        #Mostramos el campo Nota solo si es ingresado con setNota y esta en el rango 0-20
        if self.nota>=0 and self.nota<=20:
            print(f"Nota: {self.nota}")

    def setAge(self,edad):
        self.edad=edad

    def setNota(self,nota):
        self.nota=nota
#Ejecucion de Programa
#creacion de alumno sin ingresar edad ni nota
jorge=Alumno("Jorgito Gomez",5557116)
#mostrando informacion de alumno con metodo Display
jorge.Display()
#asignando edad a jorge con metodo setAge
jorge.setAge(15)
#mostrando informacion de jorge, ahora si aparece la edad pues fue ingresada y satisface los parametros
jorge.Display()
#asignando nota a jorge con metodo setNota
jorge.setNota(9)
#mostrando informacion de jorge con los campos edad y nota , pues fueron ingresados y satisfazen los parametros
jorge.Display()        
