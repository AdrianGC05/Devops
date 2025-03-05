#Herencia, Polimorfismo, Encapsulacion
class Numeros:
    def __init__(self,n):
        self.n = n
    def print_numeros(self):
        for number in range(self.n):
            if ((self.n % 2) == 0):
                print("El número ingresado es: ", number)
            else:
                print("El cuadrado del número es: ", pow(number,2))
class Racionales(Numeros):
    def __init__(self,n):
        super().__init__(n)
    
    def print_numeros(self):
        print("El numero racional es: ", self.n)
        print("El numero racional en forma de fraccion es: ", self.n.as_integer_ratio())
    
    def print_hello(self):
        return "Hello Adrian" 