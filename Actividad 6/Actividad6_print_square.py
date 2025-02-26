print("Hola Adrian, Ingresar un número entero")

try: 
    n = int(input())
    print("El número ingresado es ", n)

    for number in range(n):
        if ((n % 2) == 0):
            print("Residuo es", number % 2)
            print("El número es: ", number)
        else:
            print("El cuadrado del número es: ", pow(number,2))
except:
    print("La entrada no es un entero")
