print('Exercicio 1')
from fractions import Fraction
while True:
    try:
        a=Fraction(input('Introduce una fraccion: '))
        b=float(a)
        if round(b,2)<=0.01:
            print('La cantidad de combustible en el tanque es E')
            break
        elif round(b,2)>=0.99:
            print('La cantidad de combustible en el tanque es F')
            
        else:
            print('La caantidad de combustible en el tanque es',round(b,2)*100,'%')
            break
    
    except ValueError:
        print('Error dado, solo se permiten numeros enteros')
        break  
    except ZeroDivisionError:
        print('Introduce un denominador diferente de cero')

print('Exercicio 2')
try:
    notas=input('Ingrese las notas separadas por comas: ')
    lista=notas.split(',')
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    print(lista)#Con esta linea verificaremos la lista guardada en datos enteros
except:
    print('Los valores introducidos no puede ser convertidos debido a un error')
    
print('Exercicio 3')
class Circulo:
    pi=3.1416

    def __init__(self, radio):
        self.radio = radio

    # Hallar Area
    def Area(self):
        return self.pi*self.radio**2

c=Circulo(5)
print(c.Area())

print('Exercicio 4')
class Rectangulo:
    def __init__(self, base,altura):
        self.base = base
        self.altura=altura

    # Hallar Area
    def Area(self):
        return self.base*self.altura
#creando rectangulo de base 3 con altura 5
r=Rectangulo(3,5)
print(r.Area())

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

