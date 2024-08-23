# Autores: Catalina Ibañez y Elías González

# Función que solicita datos y valida la entrada
def lados():
    while True:
        try:
            lado1 = int(input("Primer lado: "))
            lado2 = int(input("Segundo lado: "))
            lado3 = int(input("Tercer lado: "))
            return lado1, lado2, lado3
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

# Verificar si es triángulo
def verificar(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
        print("Es un triángulo")
        return True
    else:
        print("No es un triángulo")
        return False

# Identificar el tipo de triángulo
def calculo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("Es un triángulo equilátero")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Es un triángulo escaleno")
    else:
        print("Es un triángulo isósceles")

if __name__ == '__main__':
        # Obtener los lados del triángulo
    lado1, lado2, lado3 = lados()
        # Verificar si los lados forman un triángulo
    if verificar(lado1, lado2, lado3):
        # Si es un triángulo, calcular el tipo
        calculo(lado1, lado2, lado3)
