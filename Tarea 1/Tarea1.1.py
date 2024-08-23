#Elias Gonzalez Roman

def lectura_datos():
    archivo = open(" SetDePruebas.txt", "r", encoding='utf-8')
    datos = []
    for linea in archivo:
        datos.append(linea.rstrip('\n').split(','))
    archivo.close()
    print(datos)
    return datos




if __name__ == '__main__':
    lectura_datos()