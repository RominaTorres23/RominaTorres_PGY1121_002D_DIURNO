from Container import *
import random as rn
import numpy as np
arreglo = np.array([])

ciclo = True

###################################################################
def salir():
    print("Ha salido del sistema, atentamente Romina Torres, versión 1.0")
    return False


def agregarContainer(arreglo):
    con = Container()
    c = False
    while c == False:
        c = con.setcodigo(input("Ingrese Codigo:"))
#Revisar error que tengo con con.set
    c = False
    while c == False:
        c = con.setproducto(input("Ingrese el Producto: "))
    c = False
    while c == False:
        try:
            c = con.setvalor(int(input("Ingrese el Valor: $")))
        except BaseException as error:
            print(f"Error:{error}")
    con.destino = (input("Ingrese el Destino: "))

    print("Container Agregado")
    return np.append(arreglo, con)

def buscarContainer(arreglo):
    codigo_atencion = input("Ingrese el código: ")
    total = 0
    flag = True
    for container in arreglo:
        if container.codigo == codigo_atencion:
            flag = True
            print(f"Producto:                       {container.producto}")
            print(f"Valor:                          {container.valor}")
            a = container.valor
            if int(container.valor) > 1200000:
                a = (1.1*int(container.valor))
            else:
                a = (1.05*int(container.valor))
            print(f" El valor con impuestos es de : {a}")
            print(f"Destino:                        {container.destino}")
            break
    if flag == False:
        print("El codigo de container no existe")
#mostrar el impuesto

def imprimirCertificado(arreglo):
    codigo = input("Ingrese Codigo de Container:")
    total = 0
    flag = True
    for container in arreglo:
        if  container.codigo == codigo:
            flag = True
            print(f"Producto:                       {container.producto}")
            print(f"Valor:                          {container.valor}")
            a = container.valor
            if int(container.valor) > 1200000:
                a = (1.1 * int(container.valor))
            else:
                a = (1.05 * int(container.valor))
            print(f"El Valor a pagar es de:         {a}")
            print(f"Destino:                        {container.destino}")
            b = a - int(container.valor)
            print(f"Impuesto:                       {b}")
            break
    if flag == False:
        print("El codigo de container no existe")



def imprimirContainer(arreglo):
    print("1) Imprimir Certificado de Embarque")

    print("2) Imprimir Certificado de Producto Original ")
    try:
        op_list = int(input("Seleccione (1-2): "))
        codigo_cert = rn.randint(100,5000)
        match op_list:
            case 1:
                print("CERTIFICADO DE EMBARQUE")
                print("-----------------------")
                imprimirCertificado(arreglo)
                print(f"Certificado por Embarque Folio N°{codigo_cert}")

            case 2:
                print("CERTIFICADO DE PRODUCTO ORIGINAL")
                imprimirCertificado(arreglo)
                print(f"Certificado Producto original Folio N°{codigo_cert}")

            case _:
                print("Selecciono una opción incorrecta, (1-2)")
    except BaseException as error:
        print(f"Error:{error}")




while ciclo:
    print("Exportadora Cholito")
    print("------------------------------------------")
    print("1) Grabar datos de container a exportar ")
    print("2) Buscar container")
    print("3) Imprimir Certificados ")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4): "))
        match op:
            case 1:
                print("Agregar datos de exportación")
                arreglo = agregarContainer(arreglo)
            case 2:
                print("Buscar datos de container")
                buscarContainer(arreglo)
            case 3:
                print("Imprimir Certificados")
                imprimirContainer(arreglo)
            case 4:
                print("Salir del sistema")
                ciclo = salir()
            case _:
                print("Ingreso opción incorrecta, seleccione (1-4)")
    except BaseException as error:
            print(f"Error:{error}")