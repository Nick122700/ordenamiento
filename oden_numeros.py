import tkinter as tk
from tkinter import messagebox

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# --- Interfaz gráfica ---
def agregar_dato():
    dato = entrada.get()
    if dato:
        try:
            datos.append(int(dato))  # convierte a número
        except ValueError:
            datos.append(dato)       # si no es número, guarda texto
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Debes ingresar un dato.")

def ordenar_datos():
    if datos:
        merge_sort(datos)
        actualizar_lista()
    else:
        messagebox.showwarning("Aviso", "No hay datos para ordenar.")

def actualizar_lista():
    lista.delete(0, tk.END)
    for d in datos:
        lista.insert(tk.END, d)


ventana = tk.Tk()
ventana.title("Ordenación con Merge Sort")

datos = []

tk.Label(ventana, text="Ingresa un dato:").pack()
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Agregar", command=agregar_dato).pack()
tk.Button(ventana, text="Ordenar", command=ordenar_datos).pack()

lista = tk.Listbox(ventana, width=40, height=10)
lista.pack()

ventana.mainloop()
