import numpy as np
def llenar(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
             x= x + 1
             if len(str(x))<2:
                 arreglo[f][c]= '0'+str(x)
             else:
                 arreglo[f][c] = str(x)

def mostrar(arreglo):
    for f in range(10):
        fila=''
        for c in range(10):
            if c == 5:
                fila= fila + ' | p | ' +arreglo[f][c]
            else:
                fila = fila + ' | ' + arreglo[f][c]
        print(fila)

def comprarAsiento(arreglo,n_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(n_asiento):
                arreglo[f][c]='XX'
def comprobarAsiento(arreglo,n_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(n_asiento):
                if arreglo[f][c] == 'XX':
                    return False
    return True


