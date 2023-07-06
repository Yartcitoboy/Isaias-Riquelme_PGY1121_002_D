import numpy as np
from Funciones import *
from Asistente import *
arreglo= np.full((10,10),'---')
lista_asistentes=[]
ciclo=True
def agregarAsistente(lista_asistentes,n_asiento):
    a= Asistente()
    a.rut=int(input("Ingrese rut:"))
    print("-------------------------")
    a.n_asiento=n_asiento
    if n_asiento>=1 and n_asiento<=20:
        a.valor=120000
    if n_asiento>=21 and n_asiento<=50:
        a.valor=80000
    if n_asiento>=51 and n_asiento<=100:
        a.valor=50000
    lista_asistentes.append(a)

def comprarEntradas(arreglo,lista_asistentes):
    try:
        ubicaciones=int(input("Seleccione ubicacion (1-3):"))
        if ubicaciones>=1 and ubicaciones<=3:
            compra=0
            while compra<ubicaciones:
                mostrar(arreglo)
                n_asiento=int(input("Numero de asiento:"))
                if n_asiento>= 1 and n_asiento<=100:
                    disponible= comprobarAsiento(arreglo,n_asiento)
                    if disponible==True:
                        agregarAsistente(lista_asistentes,n_asiento)
                        comprarAsiento(arreglo,n_asiento)
                        compra=compra+1
                    else:
                        print("No esta disponible")
                else:
                    print("Elija de 1 a 100")
        else:
            print("ubicaciones entre 1 y 3")
    except BaseException as error:
        print(f"error{error}")



llenar(arreglo)

def listadoAsistentes(lista_asistentes):
    for a in lista_asistentes:
        print(f"Rut:{a.rut} Valor:{a.valor} Numero de asiento:{a.n_asiento}")
        print("=============================================")
def mostrarGanacias(lista_asistentes,):
    p=0
    g=0
    s=0
    t=0
    tot_p=0
    tot_g=0
    tot_s=0
    total=0
    for a in lista_asistentes:
        if int(a.valor) == 120000:
            p = p + 1
            tot_p = tot_p + 120000
        if int(a.valor) == 80000:
            g = g + 1
            tot_g = tot_g + 80000
        if int(a.valor) == 50000:
            s = s + 1
            tot_s = tot_s + 50000
    t += p+g+s
    total+= tot_p+tot_g+tot_s
    print("=================================")
    print(f"Platinum:   Cantidad:{p} Total: {tot_p}")
    print(f"Gold:       Cantidad:{g} Total: {tot_g}")
    print(f"Silver:     Cantidad:{s} Total: {tot_s}")
    print(f"Total:      Cantidad:{t} Total: {total}")
    print("=================================")


def salir():
    print("Isaias Riquelme")
    return False


while ciclo:
    print("=========Creativos.cl=========")
    print("1) Comprar Entradas")
    print("2) Mostrar")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganacias Totales")
    print("5) Salir")
    print("------------------------------")
    try:
        op=int(input("Seleccione (1-5):"))
        match op:
            case 1:
                comprarEntradas(arreglo,lista_asistentes)
            case 2:
                mostrar(arreglo)
            case 3:
                listadoAsistentes(lista_asistentes)
            case 4:
                mostrarGanacias(lista_asistentes)
            case 5:
                ciclo = salir()
            case _:
                print("Opcion invalida, intente denuevo")
    except BaseException as error:
        print(f"error{error}")

