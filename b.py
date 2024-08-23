#Autores: Catalina Ibañez y Elías González

    #Funcion que solicita datos
def lados ():
    lado1 = input("Primer lado: ")
    lado2 = input("Segundo lado: ")
    lado3 = input("Tercer lado: ")
    return lado1,lado2,lado3

# Verificar si es triángulo
def verificar(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Es un triángulo")
        return True
    else:
        print("No es un triángulo")
        return False

def calculo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("Equilatero")
    elif lado1 != lado2 and lado1 != lado3:
        print("Escaleno")
    else:
        print("Isosceles")

if __name__ == '__main__':
    lado1,lado2,lado3 = lados()
    verificar(lado1,lado2,lado3)
    calculo(lado1,lado2,lado3)
   