print("Hola Adrian, Ingresar un número entero")

try: 
    n = int(input())
    print("El número ingresado es ", n)

    for number in range(n):
        print(number)
except:
    print("La entrada no es un entero")