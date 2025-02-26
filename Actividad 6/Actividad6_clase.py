class Entero():
    def __init__(self,n):
        self.n = n

    def print_numbers(self):
        for number in range(n):
            if ((n % 2) == 0):
                print("El número ingresado es: ", number)
            else:
                print("El cuadrado del número es: ", pow(number,2))


print("Hola Adrian, Ingresar un número entero")
n = int(input())
try: 
    print("El número ingresado es ", n)

    entero = Entero(n)
    entero.print_numbers()
except:
    print("La entrada no es un entero")

