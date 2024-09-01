import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para verificar si los lados forman un triángulo
def verificar_triangulo(lado1, lado2, lado3):
    return (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2)

# Función para identificar el tipo de triángulo
def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "EQUILÁTERO"
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return "ESCALENO"
    else:
        return "ISÓSCELES"

# Función para manejar el evento del botón de verificación
def verificar_y_mostrar():
    try:
        lado1 = int(entry_lado1.get())
        lado2 = int(entry_lado2.get())
        lado3 = int(entry_lado3.get())
        
        if verificar_triangulo(lado1, lado2, lado3):
            tipo = tipo_triangulo(lado1, lado2, lado3)
            etiqueta_resultado.configure(text=tipo, foreground='green')
        else:
            etiqueta_resultado.configure(text="NO ES UN TRIÁNGULO", foreground='red')
    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa números enteros para los lados.")

if __name__ == '__main__':
    # Inicializar la ventana
    ventana = tk.Tk()
    ventana.title("Verificador de Triángulos")
    ventana.geometry('300x250')

    # Agregar una etiqueta de instrucción
    etiqueta_instruccion = ttk.Label(ventana, text="Ingresa los lados del triángulo:")
    etiqueta_instruccion.grid(column=0, row=0, columnspan=2, pady=(10, 5))

    # Agregar entradas para los lados del triángulo
    ttk.Label(ventana, text="Primer lado:").grid(column=0, row=1, sticky=tk.W, padx=10)
    entry_lado1 = ttk.Entry(ventana, width=20)
    entry_lado1.grid(column=1, row=1, padx=10)

    ttk.Label(ventana, text="Segundo lado:").grid(column=0, row=2, sticky=tk.W, padx=10)
    entry_lado2 = ttk.Entry(ventana, width=20)
    entry_lado2.grid(column=1, row=2, padx=10)

    ttk.Label(ventana, text="Tercer lado:").grid(column=0, row=3, sticky=tk.W, padx=10)
    entry_lado3 = ttk.Entry(ventana, width=20)
    entry_lado3.grid(column=1, row=3, padx=10)

    # Agregar un botón para verificar el triángulo
    boton_verificar = ttk.Button(ventana, text="Verificar", command=verificar_y_mostrar)
    boton_verificar.grid(column=0, row=4, columnspan=2, pady=10)

    # Crear un marco (Frame) para el mensaje de resultado
    frame_resultado = ttk.Frame(ventana, borderwidth=2, relief="ridge")
    frame_resultado.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky="ew")

    # Etiqueta para mostrar resultados dentro del Frame
    etiqueta_resultado = ttk.Label(frame_resultado, text="", padding=(10, 10))
    etiqueta_resultado.grid(column=0, row=0)

    # Activar la ventana
    ventana.mainloop()


