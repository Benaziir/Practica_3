print('Exercicio 2')
try:
    notas=input('Ingrese las notas separadas por comas: ')
    lista=notas.split(',')
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    print(lista)#Con esta linea verificaremos la lista guardada en datos enteros
except:
    print('Los valores introducidos no puede ser convertidos debido a un error')