#Elias Gonzalez Roman


def lectura_datos():
    archivo = open("elección.txt", "r", encoding='utf-8')
    coalicion = []
    votos = []
    # Lee la primera línea del archivo
    primera_linea = archivo.readline().rstrip('\n')
    coalicion.append(primera_linea)
    # Lee la segunda línea del archivo
    segunda_linea = archivo.readline().rstrip('\n')
    votos.append(segunda_linea)
    archivo.close()
    # Imprime los datos y arbol para verificar
    print("Coalición:", coalicion)
    print("Votos:", votos)
    return coalicion,votos

def contador_votos():
    pass

def salida():
    pass
    
if __name__ == '__main__':
    lectura_datos()
    contador_votos()
    salida()






    