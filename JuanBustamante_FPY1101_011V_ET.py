import os
import csv
from random import randint
os.system('cls')

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
lista_sueldos=[]

def menu():
    print('1. Asignar sueldos aleatorios')
    print('2. Clasificar sueldos')
    print('3. Ver estadísticas')
    print('4. Reporte de sueldos')
    print('5. Salir del programa')

def asignar_sueldos():
    for i in trabajadores:
        sueldo=randint(300000,2500000)
        diccionario={f'{i}': sueldo}
        lista_sueldos.append(diccionario)
    print(lista_sueldos)
    print('Sueldos registrados')

def clasificar_sueldos():
    for trabajador in lista_sueldos:
        if f'{trabajador}'<800000:
            print('Nombre trabajador'   'Sueldo \n')
            nombre= f'{trabajador}'.ljust(17)
            sueldos=(f'{trabajador}').rjust(10)
            print (f'{nombre}{sueldos}')
           
def ver_estadisticas():

    sueldo_max=max(lista_sueldos)
    sueldo_min=min(lista_sueldos)
    total=sum(lista_sueldos)
    n=len(lista_sueldos)
    sueldo_promedio= total/n
    print('sueldo mas alto: ', sueldo_max)
    print('sueldo mas bajo: ', sueldo_min)
    print('sueldo promedio: ', sueldo_promedio)
    
def media_geometrica(lista_sueldos):

    producto=1
    n=10
    for sueldo in lista_sueldos:
        producto*=sueldo
        return round(producto**(1/n),2)
    resultado=media_geometrica(lista_sueldos)
    print('media geometrica: ', resultado)

def reporte():

    print('Nombre empleado '.ljust(15)+'Sueldo Base '.rjust(15)+'Descuento Salud '.rjust(15)+'Descuento AFP '.rjust(15)+'Sueldo Liquido '.rjust(15))
    print('-'*80)

    with open('reporte.csv', 'w',newline='') as reporte:
        encabezado=(['Nombre Empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])
        escritor_csv=csv.DictWriter(reporte,fieldnames=encabezado)
        escritor_csv.writeheader()
        for trabajador in lista_sueldos:
            escritor_csv.writerow(trabajador)
    print ('Reporte generado')

def salir_programa():
    print('Finalizando programa…')
    print ('Desarrollado por Juan Bustamante')
    print('RUT 12.345.678-9')

inicio=0
while inicio==0:
    try:
        menu()
        opcion=int(input('Seleccione una opcion: '))
        if opcion==1:
            asignar_sueldos()
            inicio=1
        elif opcion==2:
            clasificar_sueldos()
            inicio=1
        elif opcion==3:
            ver_estadisticas()
            media_geometrica()
            inicio=1
        elif opcion==4:
            reporte()
            inicio=1
        elif opcion==5:
            salir_programa()
            inicio=1
    except ValueError:
        print('Ingrese un numero entero')

