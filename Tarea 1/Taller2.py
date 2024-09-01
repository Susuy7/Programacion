#Author
#Luis Ponce
#Ejemplo para estudiantes.


def lectura_productos(productos):
    lproductos = []
    print(type(lproductos))
    f = open(productos, "r", encoding="utf-8")
    for linea in f:
        lproductos.append(linea.rstrip().split())
    print(lproductos)  # imprimo la lista
    lproductos.pop(0)  # remuevo el primer elemento de la lista
    print(lproductos)  # imprimo la lista
    return lproductos
    f.close()

def lectura_precios(precios):
    lprecios = []
    print(type(lprecios))
    f = open(precios, "r", encoding="utf-8")
    for linea in f:
        lprecios.append(linea.rstrip().split())
    print(lprecios)  # imprimo la lista
    lprecios.pop(0)  # remuevo el primer elemento de la lista
    print(lprecios)  # imprimo la lista
    return lprecios
    f.close()


def lectura_ajuste(ajuste):
    lajuste = []
    print(type(lajuste))
    f = open(ajuste,"r",encoding="utf-8")
    for linea in f:
        lajuste.append(linea.rstrip().split())
    print(lajuste) # imprimo la lista
    lajuste.pop(0) # remuevo el primer elemento de la lista
    print(lajuste)  # imprimo la lista
    return lajuste
    f.close()

if __name__ == "__main__":
    ajuste = lectura_ajuste("ajuste.txt")
