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