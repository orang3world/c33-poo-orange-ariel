"""
Consigna: ✍️
Crear un pequeño programa que realice una función aritmética
que permita al usuario ingresar datos por la terminal
acorde a distintas opciones.
Para ellos debemos definir una función que reciba parámetros:
Combinar funciones nativas y funciones definidas,
condicionales, y bucles.
Si el usuario ingresa el nro 1, realiza la acción A.
Si el usuario ingresa el nro 2, realiza la acción B.
"""

# Funciones nativas
a = int(input("\ningrese el valor a: "))
b = int(input("ingrese el valor b: "))

# nro 1 : calcular suma
# nro 2 : calcular resta

opcion = int(input(
    "elija la opcion deseada:\
        \n nro 1 : calcular suma\
        \n nro 2 : calcular resta\
        \n opcion elegida: "
))

# Funciones del usuario
def opcion_suma(a, b):
    suma = a + b
    return suma


def opcion_resta(a, b):
    resta = a - b
    return resta

# bucles
def graficar(inicio,fin,paso):
    print()
    for num in range(inicio,fin,paso):
        print("__"+str(num),end="")
    
    

# Condicionales
if (opcion == 1):
    graficar(0,a+1,1)
    print("\t      a = ",a)
    graficar(0,b+1,1)
    print("\t      b = ",b)
    graficar(0,opcion_suma(a,b)+1,1)
    print("\t  suma = ",opcion_suma(a, b))
    
    
elif (opcion == 2):
    
    graficar(0,a+1,1)
    print("\t a = ",a)
    graficar(0,b+1,1)
    print("\t b = ",b)

    if (a<b):
        graficar(opcion_resta(a,b),1,1)
        
    elif (a>b):
        graficar(0,opcion_resta(a,b)+1,1)
    else:
        graficar(0,1,1)
    print("\t resta = ",opcion_resta(a, b))
    print()
    
