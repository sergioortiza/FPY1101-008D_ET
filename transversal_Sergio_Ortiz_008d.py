import csv
import random
import os
import time


TRABAJADORES= [
    'Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez'
]
def sale():
    trabaja2= []
    for trabaja23 in TRABAJADORES:
        sueldo= random.randint(300000, 2500000)
        
        trabaja2.append((trabaja23, sueldo))
    return trabaja2

def guarda(trabaja2, archivo_csv = 'Trabajos.csv'):
    with open(archivo_csv, 'w', newline='')as archivo:
        campos=['Nombres', 'Sueldo Bruto', 'Descuento Salud', 'Descuento AFP', 'Renta Liquida']
        escritor_csv= csv.DictWriter(archivo, fieldnames= campos)
        escritor_csv.writeheader()

        for trabaja23 in trabaja2:
            descuento_sal = trabaja23[1]* 0.07
            descuento_afp = trabaja23[1]* 0.12
            liqui= (trabaja23[1] - descuento_afp-descuento_sal)
        escritor_csv.writerow({
            'Nombres': trabaja2[0],
            'Sueldo Bruto': trabaja2[1],
            'Descuento Salud': descuento_sal,
            'Descuento AFP': descuento_afp,
            'Renta Liquida': liqui
        })

#descsal= (sueldo* 0.07)
        #descafp= (sueldo* 0.12)
        #liqui= (sueldo- descafp-descsal)

def clasi(trabaja2):
    barato=[]
    moderado=[]
    caro=[]
    for trabaja23 in trabaja2:
        if trabaja23[1] < 800000:
            barato.append(trabaja23)
        if trabaja23[1] >= 800000 and trabaja23[1] <= 2000000:
            moderado.append(trabaja23)
        elif trabaja23[1] > 2000000:
            
            caro.append(trabaja23)
    return barato, moderado, caro 

def masalto(trabaja2):
    sueldo_mas_alto= None
    sueldo_alto= 0 
    for trabaja23 in trabaja2:
        if trabaja23[1] > sueldo_alto:
            sueldo_alto = trabaja23[1]
            sueldo_mas_alto = trabaja23
    return sueldo_mas_alto

def masbajo(trabaja2):
    sueldo_mas_bajo= None
    sueldo_bajo= float('inf')
    for trabaja23 in trabaja2:
        if trabaja23[1] < sueldo_bajo:
            sueldo_bajo = trabaja23[1]
            sueldo_mas_bajo= trabaja23
    return sueldo_mas_bajo




def prom(trabaja2):
    prome= 0
    for trabaja23 in trabaja2:
        prome += trabaja23[1]
    return prome *(1/ len(trabaja2))
    

def geo(trabaja2):
    product=1
    for trabaja23 in trabaja2:
       product *= trabaja23[1]
    return product**(1/ len(trabaja2))

def total(trabaja2):
    total= 0
    for trabaja23 in trabaja2:
        total += trabaja23[1]
    return total





def mostrar(archivo_csv ='Trabajos.csv'):
    with open(archivo_csv, 'r', newline='')as archivo:
        lector_csv=csv.reader(archivo)
        next(lector_csv)
        for fila in lector_csv:
            print(f"\nNombre {fila[0]}, Sueldo Bruto= {fila[1]}, Descuento Medico= {fila[2]}, Descuento AFP= {fila[3]}, Liquido= {fila[4]}")

def salir1():
    print("Menu de : Sergio Ortiz")
    print("Rut: 22.111.166-4")

def menu():
    trabaja2=[]
    while True:
        print(" Bienvenido al Analista de Sueldos")
        print("1. Asignar Sueldos Aleatorios")
        print("2. Clasificacion de Sueldos")
        print("3. Ver estadisticas de Sueldo")
        print("4. Reporte de sueldos")
        print("5. Slir")
        try:
            opc=int(input("Ingrese una opcion entre 1-5: "))
        except ValueError:
            print("Ingrese solo numeros")
        if opc <= 5 and opc>= 1:
            if opc ==1: 
                print("Asignando sueldos Aleatorios")
                trabaja2 = sale()
                guarda(trabaja2)
                
            if opc== 2: 
                barato, moderado, caro = clasi(trabaja2)
                print(f"Sueldos menores a 800.000=  ")
                for trabaja23 in barato:
                     
                    
                    print(f"{trabaja23[0]} = {trabaja23[1]}")
                print(f"\nSueldos entre 800.000 y 2.000.000  ")
                for trabaja23 in moderado:
                   
                    
                    print(f"{trabaja23[0]} = {trabaja23[1]}")
                print(f"\nSueldos mayores a 2.000.000  ")
                for trabaja23 in caro:
                    
                    
                    print(f"{trabaja23[0]} = {trabaja23[1]}")


            if opc==3:
                print("Imprimiendo estadisticas de sueldo ")
                sueldo_mas_bajo= masbajo(trabaja2)
                sueldo_mas_alto= masalto(trabaja2)
                promedio= prom(trabaja2)
                medida_geo= geo(trabaja2)
                total_sueldo= total(trabaja2)

                
                print(f"Sueldo mas Bajo= {sueldo_mas_bajo}")
                print(f"Sueldo mas Alto= {sueldo_mas_alto}")
                print(f"Promedio de sueldos =  {promedio}")
                print(f"Medida geometrica = {medida_geo}" )
                print(f"Total de Sueldos= {total_sueldo}")
            if opc ==4:
                
                mostrar()
            if opc==5:
                salir1()
                break
        else:
            print("Valor fuera de rango")
                

menu()