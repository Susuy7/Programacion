# Elias Gonzalez Roman
estudiantes = { 
    "Ana":      [8, 9, 7, 10],
    "Julia":    [8, 9, 7, 10],
    "Adriana":  [8, 9, 7, 10],
    "Benjamín": [8, 9, 7, 10],
    "Diego":    [8, 9, 7, 10],
    "Juan":     [8, 9, 7, 10], 
    "María":    [9, 10, 9, 8],
    "Pedro":    [7, 8, 6, 9]
}

# Función para calcular el promedio de una lista de calificaciones
def promedio_calificación(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para calcular la calificación máxima de una lista de calificaciones
def calificación_máxima(calificaciones):
    return max(calificaciones)

# Función para calcular la calificación mínima de una lista de calificaciones
def calificación_mínima(calificaciones):
    return min(calificaciones)

# Función para imprimir los resultados para cada estudiante
def salida_resultados(estudiantes):
    for nombre, calificaciones in estudiantes.items():
        promedio = promedio_calificación(calificaciones)
        maxima = calificación_máxima(calificaciones)
        minima = calificación_mínima(calificaciones)
        
        print(f"Estudiante: {nombre}")
        print(f"  Promedio: {promedio:.2f}")
        print(f"  Calificación Máxima: {maxima}")
        print(f"  Calificación Mínima: {minima}")
        print("---------------------------")

if __name__ == '__main__':
    salida_resultados(estudiantes)
