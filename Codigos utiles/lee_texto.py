def lee_datos(nombre):
    ent = open('terr.txt')
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos


def lectura_datos():
    archivo = open("nombre.txt", "r", encoding='utf-8')
    datos = []
    for linea in archivo:
        datos.append(linea.rstrip('\n').split(','))
    archivo.close()
    return datos

if __name__ == '__main__':
    lectura_datos()