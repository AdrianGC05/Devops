#modulos en python
import Actividad7_1_numeros  # type: ignore
import Actividad7_3_abstract_class # type: ignore

print("Ingrese un numero")
n = int(input())
enteros = Actividad7_1_numeros.Numeros(n)
enteros.print_numeros()

print("Ingrese un numero racional: ")
q = float(input())
racionales = Actividad7_1_numeros.Racionales(q)
racionales.print_numeros()

print("Ingrese un numero racional para el modulo abstracto: ")
m = float(input())
racionales = Actividad7_3_abstract_class.Racionales(m)
#racionales = Actividad7_3_abstract_class.AbsNumeros() no se puede instanciar una clase abstract
racionales.print_numeros()